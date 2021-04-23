from collections import namedtuple
Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
Task.__new__.__defaults__ = (None, None, False, None)

# def test_asdict():
#     """_asdict() должен возвращать словарь."""
#     t_task = Task('do something', 'okken', True, 21)
#     # print((t_task[3]))
#     t_dict = t_task._asdict()
#     expecte = {'summary': 'do something',
#                 'owner': 'okken',
#                 'done': True,
#                 'id': 21}
#     # print (t_dict)
#     assert t_dict == expecte