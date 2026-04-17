class Taskplanner():
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        if task in self.tasks:
            raise Exception('task already in task list')
        self.tasks.append(task)
        

    def list_outstanding_tasks(self):
        # arguements - none
        # returns list of tasks
        # side effects - none
        return self.tasks

    def mark_task_complete(self, task):
        # arguments - string of task
        # returns nothing
        # side effects removes task from list of tasks
        self.tasks.remove(task)
