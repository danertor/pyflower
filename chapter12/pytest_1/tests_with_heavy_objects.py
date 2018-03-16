from unittest.mock import Mock, patch
import py.test
from datetime import datetime


from heavy_objects import FlightStatusTracker


def pytest_funcarg__tracker():
    return FlightStatusTracker()

def test_mock_method(tracker):
    tracker.redis.set = Mock()
    with py.test.raises(ValueError) as ex:
        tracker.change_status("AC101", "lost")
    assert ex.value.args[0] == "LOST is not a valid status"
    assert tracker.redis.set.call_count == 0


# how to set a function to return a specific value on every test, to be consistent,
# like returning time.
def test_patch(tracker):
    tracker.redis.set = Mock()
    fake_now = datetime(2015, 4, 1)
    with patch('datetime.datetime') as dt:
        dt.now.return_value = fake_now
        tracker.change_status("AC102", "on time")
    dt.now.assert_called_once_with()
    tracker.redis.set.assert_called_once_with("flightno:AC102", "2015-04-01T00:00:00|ON TIME")
