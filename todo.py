# MPCS 50101 - Summer 2023
# Final Project
# Nick Sherrard


#PLANNING
# 1. main initializes Tasks() object, called "tasks"
# 2. while initializing, the tasks object loads the pickle as a list
# 3. If we then read arguments (i.e., -add), we edit the list
# 4. We dump back to the file
import argparse
import pickle
import uuid
import datetime

class Task:
    """Representation of a task

    Attributes:
                - created - date
                - completed - date
                - name - string
                - unique id - number
                - priority - int value of 1, 2, or 3; 1 is default
                - due date - date, this is optional
    """
    def __init__(self, id, name, priority = 1, due_date = None):
        self.unique_id = id #uuid.uuid1()
        self.name = name
        self.priority = priority
        self.created = datetime.datetime.now()
        self.completed = None
        self.due_date = due_date


class Tasks:
    """A list of `Task` objects."""
    def __init__(self):
        """Read pickled tasks file into a list"""
        # List of Task objects
        self.tasks = [] 

        # Attempt to read file
        try:
            with open('.todo.pickle', 'rb') as f:
                self.tasks = pickle.load(f)
        except:
            with open('.todo.pickle', 'wb') as f:
                    pickle.dump(self.tasks,f)
            with open('.todo.pickle', 'rb') as f:
                self.tasks = pickle.load(f)


    def pickle_tasks(self):
        try:
            with open('.todo.pickle', 'wb') as f:
                pickle.dump(self.tasks,f)
        except:
            print("Encountered unexpected error while saving. To-Do list not updated.")

    # Complete the rest of the methods, change the method definitions as needed
    def list(self):
        pass

    def report(self):
        pass

    def query(self):
        pass

    def add(self, name, priority, due_date):
        # Create id as 1 + the largest existing ID in the task list
        try:
            id = max(tasks.unique_id for tasks in self.tasks) + 1
        except:
            id = 1
        t = Task(id, name, priority, due_date)
        # NOTE TO SELF - WE CAN IMPROVE THE ADDING OF TASKS TO SORT BY PRIORITY
        self.tasks.append(t)

    def delete(self, id):
        self.tasks = [task for task in self.tasks if task.unique_id != id]
    
    def done(self, id):
        self.tasks.completed[self.tasks.unique_id == id] = datetime.datetime.now()

def task_reporter(task_list):
    print("ID\tAge\tDue Date\tPriority\tTask\t\tCreated\t\tCompleted")
    print("--\t---\t--------\t--------\t----\t\t-------\t\t---------")
    for task in task_list:
        age = datetime.datetime.now() - task.created
        created = datetime.datetime.strftime(task.created, '%m/%d/%Y')
        if task.completed == None:
            completed = None
        else:
            completed = datetime.datetime.strftime(task.completed, '%m/%d/%Y')  
        print(task.unique_id, "\t", str(age.days)+"d", "\t", task.due_date, "\t\t", task.priority, "\t\t", task.name, "\t", created, "\t", completed)
              
def main():
    # Prepare the argument parser
    parser = argparse.ArgumentParser(description="Update to-do list.")

    # Add a task
    parser.add_argument('--add', type = str, required = False, help = 'a task string to add to your list.')
    parser.add_argument('--priority', type = int, required = False, default = 1, help = 'priority of task with default of 1')
    parser.add_argument('--done', type = str, required = False, help = 'mark a task complete using unique identifier')
    parser.add_argument('--due', type = str, required = False, help = 'due date in MM/DD/YYYY format')

    # View tasks
    parser.add_argument('--query', type = str, required = False, nargs = "+", help = 'search for tasks by key words')
    parser.add_argument('--list', action = "store_true", required = False, help = 'list incomplete to-do tasks')
    parser.add_argument('--report', action = "store_true", required = False, help = 'list all to-do tasks')

    # Remove tasks
    parser.add_argument('--delete', type = str, required = False, help = 'permanenty remove task from to-do list')

    # Parse the argument
    args = parser.parse_args()

    # Read the arguments back to the user:
    print("Add:", args.add)
    print("Due:", args.due)
    print("Priority:", args.priority)
    print("List:", args.list)
    print("Query:", args.query)

    # Initialize tasks list
    tasks = Tasks()   

    # Process arguments
    if args.add:
        print(f"We have added {args.add} to our to-do list with a priority of {args.priority}.")
        tasks.add(args.add, args.priority, args.due)
    elif args.report:
        task_reporter(tasks.tasks)
    elif args.list:
        task_reporter(filter(lambda x: x.completed == None,tasks.tasks))
    elif args.delete:
        tasks.delete(int(args.delete))
    elif args.done:
        tasks.done(args.done)

    # OTHERS

    # Re-pickle tasks
    tasks.pickle_tasks()

if __name__ == "__main__":
    main()
