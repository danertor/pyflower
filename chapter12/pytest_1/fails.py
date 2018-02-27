import py.test

@py.test.mark.xfail(reason="Testing the xfail mark decorator")
def test_python_fails():
    """Expected to fail, python fails with this arithmetic operation:
    See https://github.com/maebert/python-fails
    """
    a = 20
    assert a * a is 400