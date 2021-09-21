import pyglmp


def test_hello(capfd):
    pyglmp.hello("World")
    captured = capfd.readouterr()
    assert captured.out == "Hello, World!\n"


def test_elevation():
    assert pyglmp.elevation() == 21463
