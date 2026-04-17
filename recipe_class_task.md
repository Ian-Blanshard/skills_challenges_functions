# Task Planner Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

## 2. Design the Class Interface

```python
 class Taskplanner():
    def __init__(self):
        # list of tasks
        pass

    def add_task(self, task):
        # arguments - string of task
        # returns nothing
        # side effects add task to list of tasks
        pass

    def list_outstanding_tasks(self):
        # arguements - none
        # returns list of tasks
        # side effects - none
        pass

    def mark_task_complete(self, task):
        # arguments - string of task
        # returns nothing
        # side effects removes task from list of tasks
        pass    

```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
"""
list outstanding tasks returns empty list
if no tasks yet added to list
"""
def test_empty_task_list():
    tasks = Taskplanner
    tasks.list_outstanding_tests == []

"""
list outstanding tasks returns task 
if one tasks added to list
"""
def test_add_to_task_list():
    tasks = Taskplanner
    tasks.add_task('my task')
    tasks.list_outstanding_tests == ['my task']

"""
list outstanding tasks returns task 
if three tasks added to list
"""
def test_add_multiple_to_task_list():
    tasks = Taskplanner
    tasks.add_task('my task 3')
    tasks.add_task('my task 1')
    tasks.add_task('my task 2')
    tasks.list_outstanding_tests == ['my task 3', 'my task 1', 'my task 2']

"""
exception raised when the same task is added twice
"""
def test_add_same_task():
    tasks = Taskplanner
    tasks.add_task('my task 1')
    tasks.add_task('my task 1')
    exception raised - 'task already in task list'

"""
mark task complete removes task from list
"""
def test_remove_task():
    tasks = Taskplanner
    tasks.add_task('my task 3')
    tasks.add_task('my task 1')
    tasks.add_task('my task 2')
    tasks.remove_task('my task 3')
    tasks.list_outstanding_tests == ['my task 1', 'my task 2']

""" 
all tasks can be removed from list
"""
def test_remove_all_tasks():
    tasks = Taskplanner
    tasks.add_task('my task 3')
    tasks.add_task('my task 1')
    tasks.remove_task('my task 3')
    tasks.remove_task('my task 1')
    tasks.list_outstanding_tests == []
``` 
## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
