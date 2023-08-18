# MPCS 50101 - Summer 2023
# Final Project
# Nick Sherrard

# Import standard packages
import pickle
import datetime

# Import custom packages
import todo_formatter
import todo_argument_prep

def query_tasks(task_list,query_list):
    """
    Searches for queried key words in task list objects' name attribute. Returns a list of task ids.
    O(N*M) time complexity where N is queried key words, and M is task list length
    """
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
        # Create sorting attribute that defaults NoneType due dates to the max date
        if self.due_date == None:
            self.sort_due_date = datetime.date(datetime.MAXYEAR,12,31)
        else:
            self.sort_due_date = self.due_date


class Tasks:
    """A list of `Task` objects. List sorted by priority, due date, then name."""
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
        print("\n--------------- Welcome to Terminal To-Do ---------------\n")
    def pickle_tasks(self):
        """Writes list from Tasks object to pickle file if one exists, or creates a new one."""
        try:
            with open('.todo.pickle', 'wb') as f:
                pickle.dump(self.tasks,f)
        except:
            print("Encountered unexpected error while saving. To-Do list not updated.")

    # Complete the rest of the methods, change the method definitions as needed
    def list(self):
        """List only incomplete tasks"""
        todo_formatter.task_lister(list(filter(lambda x: x.completed == None,self.tasks)))

    def report(self):
        """List all tasks, complete and incomplete"""
        todo_formatter.task_reporter(self.tasks)

    def query(self, query_list):
        """Search for task by key words"""
        matched_ids = query_tasks(self.tasks, query_list)
        todo_formatter.task_lister([task for task in self.tasks if task.unique_id in matched_ids])

    def add(self, name, priority, due_date):
        """Create new task with optional inputs priority and due date"""
        # Create id as 1 + the largest existing ID in the task list
        try:
            id = max(tasks.unique_id for tasks in self.tasks) + 1
        except:
            id = 1
        t = Task(id, name, priority, due_date)
        self.tasks.append(t)
        self.tasks.sort(key=lambda task: (task.priority, str(task.sort_due_date), task.name))
        print("Success!")

    def delete(self, id):
        """Permanently remove task by id from list"""
        self.tasks = [task for task in self.tasks if task.unique_id != id]
    
    def done(self, id):
        """Mark task complete that matches the input unique id"""
        for task in self.tasks:
            if str(task.unique_id) == id:
                if task.completed == None:
                    task.completed = datetime.datetime.now()
                    print("Success!")
                else:
                    print("Success!")
                    print("Updating prior completion date to now.\n")
                    task.completed = datetime.datetime.now()

def main():
    
    # Collect input from terminal
    args = todo_argument_prep.argument_prep()

    # Initialize tasks list
    tasks = Tasks()   

    # Process arguments
    if args.add:
        print("Adding task...")
        print("Task:", args.add)
        print("Due:", args.due)
        print("Priority:", args.priority)
        print("List:", args.list)
        print("Query:", args.query)
        tasks.add(args.add, args.priority, args.due)
    elif args.report:
        try:
            tasks.report()
        except:
            print("Unexpected error while rendering. Please confirm to-do list isn't empty.")
    elif args.list:
        try:
            tasks.list()
        except:
            print("Unexpected error while rendering. Please confirm to-do list isn't empty.")
    elif args.delete:
        print(f"Deleting task id {args.delete} if it exists in the to-do list.")
        tasks.delete(int(args.delete))
    elif args.done:
        print(f"Marking task id {args.done} complete if it exists in the to-do list.")
        tasks.done(args.done)
    elif args.query:
        tasks.query(args.query)

    print("")

    # Re-pickle tasks
    tasks.pickle_tasks()

if __name__ == "__main__":
    main()
