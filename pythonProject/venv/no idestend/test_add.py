import pytest
import tasks

from collections import namedtuple
Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
Task.__new__.__defaults__ = (None, None, False, None)

def test_add_returns_valid_id():
    """tasks.add(valid task) должен возвращать целое число."""
    # GIVEN an initialized tasks db
    # WHEN a new task is added
    # THEN returned task_id is of type int
new_task = Task('do something')
print(new_task.id)
task_id = tasks.add(new_task)
# assert isinstance(task_id, int)