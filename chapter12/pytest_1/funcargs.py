from stats import StatsList
import pprint

pp = pprint.PrettyPrinter(indent=4)

#pytest_funcarg__<identifier>
def pytest_funcarg__valid_stats(request):
    #pp.pprint(request.__dict__)
    print('Function with parameters: {0}'.format(request._pyfuncitem.name)) ## function that requested the valid_stats parameter
    return StatsList([1,2,2,3,3,4])

def test_mean(valid_stats):
    assert valid_stats.median() == 2.5
    valid_stats.append(4)
    assert valid_stats.median() == 3

def test_mode(valid_stats):
    assert valid_stats.mode() == [2,3]
    valid_stats.remove(2)
    assert valid_stats.mode() == [3]

