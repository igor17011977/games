from collections import namedtuple

Parts = namedtuple('Parts', 'id_num desc cost amount')
Parts.__new__.__defaults__ = (None, None, False, None)
#auto_parts = Parts(None, None, False, None)

def test_defaults():
    """Без использования параметров, следует ссылаться на значения по умолчанию."""
    t1 = Parts()
    t2 = Parts(None, None, False, None)
    assert t1==t2, "fgfghfg"
    print("ff,gjfk")
    x = "hello"

    # if condition returns False, AssertionError is raised:
    assert x == "hello", "x should be 'hello'"
z=test_defaults()