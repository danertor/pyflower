import datetime
import redis

class FlightStatusTracker:
<<<<<<< HEAD
    ALLOWD_STATUSES = {'CANCELED', 'DELAYED', 'ON TIME'}

    def __init__(self, redis_instance=None):
        self.redis = redis_instance if redis_instance else redis.StrictRedis()
=======
    ALLOWD_STATUSES = {'CANCELED', 'DELAYED', ' ON TIME'}

    def __init__(self):
        self.redis = redis.StrictRedis()
>>>>>>> b829bcb465b0e32104dbe492037b6da0f67e9948

    def change_status(self, flight, status):
        status = status.upper()
        if status not in self.ALLOWD_STATUSES:
            raise ValueError("{} is not a valid status".format(status))

        key = "flightno:{}".format(flight)
        value = "{}|{}".format(datetime.datetime.now().isoformat(), status)
        self.redis.set(key, value)

