# MPCS 50101 - Summer 2023
# Final Project - Argument Prep
# Nick Sherrard

import argparse
import datetime
import re

def argument_prep():
    """Defines expected arguments from terminal and performs validation on priority and due-date. Returns args object."""
    # Prepare the argument parser
    parser = argparse.ArgumentParser(description="Update to-do list.")

    # Add a task
    parser.add_argument('--add', type = str, required = False, help = 'a task string to add to your list.')
    parser.add_argument('--priority', type = int, required = False, default = 1, help = 'priority of task with default of 1')
    parser.add_argument('--done', type = str, required = False, help = 'mark a task complete using unique identifier')
    parser.add_argument('--due', type = str, required = False, default = None, help = 'due date in MM/DD/YYYY format')

    # View tasks
    parser.add_argument('--query', type = str, required = False, nargs = "+", help = 'search for tasks by key words')
    parser.add_argument('--list', action = "store_true", required = False, help = 'list incomplete to-do tasks')
    parser.add_argument('--report', action = "store_true", required = False, help = 'list all to-do tasks')

    # Remove tasks
    parser.add_argument('--delete', type = str, required = False, help = 'permanenty remove task from to-do list')

    # Parse the argument
    args = parser.parse_args()

    # Perform validation on priority argument
    if args.priority:
        if args.priority > 3:
            print("Priority must be either 1, 2, or 3. Defaulting to 3.")
            args.priority = 3
        elif args.priority < 1:
            print("Priority must be either 1, 2, or 3. Defaulting to 1.")
            args.priority = 1
    
    # Perform validation on due-date argument
    if args.due:
        date_regex = r"([0-9]{1,2})/([0-9]{1,2})/([0-9]{4})$"
        date = re.match(date_regex, args.due)
        if date == None:
            print("Invalid date format. Please retry with MM/DD/YYYY format.")
            due_date = None
        else:
            due_date = date.group(0)
            due_date = datetime.datetime.strptime(due_date, '%m/%d/%Y')
        args.due = due_date

    return args