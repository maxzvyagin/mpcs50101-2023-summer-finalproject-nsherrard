# MPCS 50101 - Summer 2023
# Final Project
# Nick Sherrard


import argparse
import pickle
import uuid
import datetime

def column_prepper(task_list):
    """Looks at the length of strings in each field and calculates the necessary amount of spaces between column headers.
    Returns a list of strings of spaces corresponding tasks.report() headers.
    """
    # Set spaces between columns
    buffer = 2

    # Compute ID spaces
    id_spaces = max(buffer + len("ID"),buffer + max(len(str(tasks.unique_id)) for tasks in task_list))

    # Compute Age spaces
    longest_age = 0
    for task in task_list:
        age = str((datetime.datetime.now() - task.created).days) + "d"
        print("TEST ", age)
        if len(age) > longest_age:
            longest_age = len(age)
    age_spaces = max(buffer + len("Age"), buffer + longest_age)

    # Compute Due Date
    longest_due = 0
    for task in task_list:
            try:
                due = datetime.datetime.strftime(task.due_date, '%m/%d/%Y')
            except:
                # For NoneTypes
                due = str(task.due_date)
            if len(due) > longest_due:
                longest_due = len(due)
    due_date_spaces = max(buffer + len("Due Date"), buffer + longest_due)

    # Compute Priority
    priority_spaces = max(buffer + len("Priority"),max(len(str(tasks.priority)) for tasks in task_list))
    print("PRIORITY: ",priority_spaces)
    # Compute Name
    name_spaces = max(buffer + len("Task"),buffer + max(len(tasks.name) for tasks in task_list))

    # Compute Created
    longest_created = 0
    for task in task_list:
            created = datetime.datetime.strftime(task.created, '%m/%d/%Y')
            if len(created) > longest_created:
                longest_created = len(created)
    created_spaces = max(buffer + len("Created"),buffer + longest_created)

    # Compute Completed
    longest_completed = 0
    for task in task_list:
            try:
                completed = datetime.datetime.strftime(task.completed, '%m/%d/%Y')
            except:
                # For NoneTypes
                completed = str(task.completed)
            if len(completed) > longest_completed:
                longest_completed = len(completed)
    completed_spaces = max(buffer + len("Completed"),buffer +  longest_completed)

    # Return spaces list
    out = [id_spaces, age_spaces, due_date_spaces, priority_spaces, name_spaces, created_spaces, completed_spaces]
    return out

def task_reporter(task_list):
    """Prints to terminal all input tasks with all headers for tasks.report() method."""
    space_count = column_prepper(task_list)
    header_space_count = [space_count[0] - len("ID"), space_count[1] - len("Age"), space_count[2] - len("Due Date"), space_count[3] - len("Priority"), space_count[4] - len("Task"), space_count[5] - len("Created")]
    spaces = [" " * space for space in header_space_count]
    print(f"ID{spaces[0]}Age{spaces[1]}Due Date{spaces[2]}Priority{spaces[3]}Task{spaces[4]}Created{spaces[5]}Completed")
    print(f"--{spaces[0]}---{spaces[1]}--------{spaces[2]}--------{spaces[3]}----{spaces[4]}-------{spaces[5]}---------")
    for task in task_list:
        age = datetime.datetime.now() - task.created
        created = datetime.datetime.strftime(task.created, '%m/%d/%Y')
        if task.completed == None:
            completed = "None"
        else:
            completed = datetime.datetime.strftime(task.completed, '%m/%d/%Y')
        if task.due_date == None:
            due_date = "None"
        else:
            due_date = datetime.datetime.strftime(task.due_date, '%m/%d/%Y')
        task_space_count = [space_count[0] - len(str(task.unique_id))-2, space_count[1] - len(str(age.days)+"d")-2, space_count[2] - len(due_date)-2, space_count[3] - len(str(task.priority))-2, space_count[4] - len(task.name)-2, space_count[5] - len(created)-2]
        task_spaces = [" " * space_count for space_count in task_space_count]
        print(str(task.unique_id), task_spaces[0], str(age.days)+"d", task_spaces[1], due_date, task_spaces[2], task.priority, task_spaces[3], task.name, task_spaces[4], created, task_spaces[5], completed)

def task_lister(task_list):
    """Prints to terminal all input tasks with selected headers for tasks.list() method"""
    print("ID\tAge\tDue Date\tPriority\tTask")
    print("--\t---\t--------\t--------\t----")
    for task in task_list:
        age = datetime.datetime.now() - task.created
        print(task.unique_id, "\t", str(age.days)+"d", "\t", task.due_date, "\t\t", task.priority, "\t\t", task.name)

def query_tasks(task_list,query_list):
    """
    Searches for queried key words in task list objects' name attribute. Returns a list of task ids.
    O(N*M) time complexity where N is queried key words, and M is task list length"""
    output_ids = []
    for query in query_list:
        for task in task_list:
            if query.lower() in task.name.lower():
                output_ids.append(task.unique_id)
    return output_ids

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
        """Writes list from Tasks object to pickle file if one exists, or creates a new one."""
        try:
            with open('.todo.pickle', 'wb') as f:
                pickle.dump(self.tasks,f)
        except:
            print("Encountered unexpected error while saving. To-Do list not updated.")

    # Complete the rest of the methods, change the method definitions as needed
    def list(self):
        task_lister(filter(lambda x: x.completed == None,self.tasks))

    def report(self):
        task_reporter(self.tasks)

    def query(self, query_list):
        matched_ids = query_tasks(self.tasks, query_list)
        task_lister([task for task in self.tasks if task.unique_id in matched_ids])

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

    # Initialize tasks list
    tasks = Tasks()   

    # Process arguments
    if args.add:
        print(f"We have added {args.add} to our to-do list with a priority of {args.priority}.")
        print("Add:", args.add)
        print("Due:", args.due)
        print("Priority:", args.priority)
        print("List:", args.list)
        print("Query:", args.query)
        tasks.add(args.add, args.priority, args.due)
    elif args.report:
        tasks.report()
    elif args.list:
        tasks.list()
    elif args.delete:
        tasks.delete(int(args.delete))
    elif args.done:
        tasks.done(args.done)
    elif args.query:
        tasks.query(args.query)

    # Re-pickle tasks
    tasks.pickle_tasks()

if __name__ == "__main__":
    main()
