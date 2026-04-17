from lib.task_planner import *
import pytest
"""
list outstanding tasks returns empty list
if no tasks yet added to list
"""
def test_empty_task_list():
    tasks = Taskplanner()
    assert tasks.list_outstanding_tasks() == []

"""
list outstanding tasks returns task 
if one tasks added to list
"""
def test_add_to_task_list():
    tasks = Taskplanner()
    tasks.add_task('my task')
    assert tasks.list_outstanding_tasks() == ['my task']

"""
list outstanding tasks returns task 
if three tasks added to list
"""
def test_add_multiple_to_task_list():
    tasks = Taskplanner()
    tasks.add_task('my task 3')
    tasks.add_task('my task 1')
    tasks.add_task('my task 2')
    assert tasks.list_outstanding_tasks() == ['my task 3', 'my task 1', 'my task 2']

"""
exception raised when the same task is added twice
"""
def test_add_same_task():
    tasks = Taskplanner()
    tasks.add_task('my task 1')
    with pytest.raises(Exception) as error:
        tasks.add_task('my task 1')
    error_message = str(error.value)
    assert error_message == 'task already in task list'

"""
mark task complete removes task from list
"""
def test_remove_task():
    tasks = Taskplanner()
    tasks.add_task('my task 3')
    tasks.add_task('my task 1')
    tasks.add_task('my task 2')
    tasks.mark_task_complete('my task 3')
    assert tasks.list_outstanding_tasks() == ['my task 1', 'my task 2']

""" 
all tasks can be removed from list
"""
def test_remove_all_tasks():
    tasks = Taskplanner()
    tasks.add_task('my task 3')
    tasks.add_task('my task 1')
    tasks.mark_task_complete('my task 3')
    tasks.mark_task_complete('my task 1')
    assert tasks.list_outstanding_tasks() == []