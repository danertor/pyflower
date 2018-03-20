from unittest import TestCase, mock, main
import json
import time
from threads_temperatures import CITIES, TempGetter
from urllib.request import urlopen

jweather_example = """
{"coord":{"lon":-0.13,"lat":51.51},"weather":[{"id":801,"main":"Clouds","description":"few clouds","icon":"02d"}],"base":"stations","main":{"temp":284.65,"pressure":999,"humidity":58,"temp_min":284.15,"temp_max":285.15},"visibility":10000,"wind":{"speed":7.7,"deg":140},"clouds":{"all":12},"dt":1521040800,"sys":{"type":1,"id":5093,"message":0.0055,"country":"GB","sunrise":1521008140,"sunset":1521050660},"id":2643743,"name":"London","cod":200}
"""

def test_get_temperatures():
    with mock.patch('threads_temperatures.urlopen') as uo:
        a = mock.Mock()
        a.read.return_value = jweather_example
        a.called
        # a.read.side_effect = [jweather_example for x in range(len(CITIES)+1)]
        uo.return_value = a
        threads = [TempGetter(c) for c in CITIES]
        test_thread = TempGetter('Dummy city')
        test_thread.start()
        test_thread.join()
        print("Test: it is {0.temperature:.0f}°C in {0.city}".format(test_thread))
        start = time.time()
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        for thread in threads:
            print("it is {0.temperature:.0f}°C in {0.city}".format(thread))
        print("Got {} temps in {} seconds".format(len(threads), time.time() - start))

test_get_temperatures()