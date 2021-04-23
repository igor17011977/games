from collections import namedtuple
import tasks
Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
Task.__new__.__defaults__= (None, None, False, None)
new_task = Task('sit in chair', owner='me', done=True)
new_task = Task('do something')
task_id = tasks.add(new_task)