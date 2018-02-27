import datetime
import redis

class FlightStatusTracker:
    ALLOWD_STATUSES = {'CANCELED', 'DELAYED', ' ON TIME'}

    def __init__(self):
        self.redis = redis.StrictRedis()

    def change_status(self, flight, status):
        status = status.upper()
        if status not in self.ALLOWD_STATUSES:
            raise ValueError("{} is not a valid status".format(status))

        key = "flightno:{}".format(flight)
        value = "{}|{}".format(datetime.datetime.now().isoformat(), status)
        self.redis.set(key, value)

