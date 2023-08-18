# MPCS 50101 - Summer 2023
# Final Project - Terminal Formatter
# Nick Sherrard

import datetime

def column_prepper(task_list):
    """
    Looks at the length of strings in each field and calculates the necessary amount of spaces between column headers.
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
    # Get column spacers from column_prepper helper function
    space_count = column_prepper(task_list)
    # Deduct length of headers
    header_space_count = [space_count[0] - len("ID"), space_count[1] - len("Age"), space_count[2] - len("Due Date"), space_count[3] - len("Priority"), space_count[4] - len("Task"), space_count[5] - len("Created")]
    # Convert space count into space characters
    spaces = [" " * space for space in header_space_count]
    # Print the headers with underlines
    print(f"ID{spaces[0]}Age{spaces[1]}Due Date{spaces[2]}Priority{spaces[3]}Task{spaces[4]}Created{spaces[5]}Completed")
    print(f"--{spaces[0]}---{spaces[1]}--------{spaces[2]}--------{spaces[3]}----{spaces[4]}-------{spaces[5]}---------")
    # Iterate through tasks
    for task in task_list:
        # Format age, created date, completed date, and due date
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
        # Deduct length of value from the column spacers
        task_space_count = [space_count[0] - len(str(task.unique_id))-2, space_count[1] - len(str(age.days)+"d")-2, space_count[2] - len(due_date)-2, space_count[3] - len(str(task.priority))-2, space_count[4] - len(task.name)-2, space_count[5] - len(created)-2]
        # Convert space counts to space characters
        task_spaces = [" " * space_count for space_count in task_space_count]
        # Print task to terminal
        print(str(task.unique_id), task_spaces[0], str(age.days)+"d", task_spaces[1], due_date, task_spaces[2], task.priority, task_spaces[3], task.name, task_spaces[4], created, task_spaces[5], completed)
    print("")

def task_lister(task_list):
    """Prints to terminal all input tasks with selected headers for tasks.list() method"""
    # Get column spacers from column_prepper helper function
    space_count = column_prepper(task_list)
    # Deduct length of headers
    header_space_count = [space_count[0] - len("ID"), space_count[1] - len("Age"), space_count[2] - len("Due Date"), space_count[3] - len("Priority"), space_count[4] - len("Task")]
    # Convert space count into space characters
    spaces = [" " * space for space in header_space_count]
    # Print the headers with underlines    
    print(f"ID{spaces[0]}Age{spaces[1]}Due Date{spaces[2]}Priority{spaces[3]}Task")
    print(f"--{spaces[0]}---{spaces[1]}--------{spaces[2]}--------{spaces[3]}----")
    # Format age, due date  
    for task in task_list:
        age = datetime.datetime.now() - task.created
        if task.due_date == None:
            due_date = "None"
        else:
            due_date = datetime.datetime.strftime(task.due_date, '%m/%d/%Y')
        # Deduct length of value from the column spacers
        task_space_count = [space_count[0] - len(str(task.unique_id))-2, space_count[1] - len(str(age.days)+"d")-2, space_count[2] - len(due_date)-2, space_count[3] - len(str(task.priority))-2, space_count[4] - len(task.name)-2]
        # Convert space counts to space characters        
        task_spaces = [" " * space_count for space_count in task_space_count]
        # Print task to terminal
        print(str(task.unique_id), task_spaces[0], str(age.days)+"d", task_spaces[1], due_date, task_spaces[2], task.priority, task_spaces[3], task.name, task_spaces[4])
    print("")
