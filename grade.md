# Final Project Rubric #
## Command Line Task Manager 

## Argument Parsing (2 Points)
-------------------
- [x] 1.0: Uses the `argparse` module to handle all required inputs (`--add`, `--delete`, `--list`, `--report`, `--query`, and `--done`)
- [x] 0.5: Successfully parses the date format inputed by the user
- [x] 0.5: Arguments correctly control the flow of the appplication using conditional statements. Note the handling of "optional" inputs.

## Task Data Objects (2 points)
-------------------------------
- [x] 2.0: OOP `Task` Data object defined with correct attributes. Note that the implemention details are up to the students (eg. set priority as default parameter, uuid, etc.) but they should allow for correct behavior.
    - created - date
    - completed - date
    - name - string
    - unique id - number
    - priority - int value of 1, 2, or 3; 1 is default
    - due date - date, this is optional

## Tasks Data Object (2 points)
--------------------------------
OOP `Tasks` object contains a list of `Task` objects. Uses pickle functionality to save/retrieve `Tasks` objects.
    - [x] 0.5 Opens the pickle file into a list
    - [x] 0.5 Saves list to pickle file on program completion
    - [x] 0.5 Handles the "first run" where there is not pickle file
    - [x] 0.5 Best practices in OOP and file handling (only take off points for gross violations)

## Tasks Methods (12 points)
--------------------------------
These are all 2 points: 1 point for functionality, 1 point for best practices in implementation.
- [x] 2.0: 'Add' task functionality; proper parsing
- [x] 2.0: 'List' task functionality; proper formatting
- [x] 1.5/2.0: 'List' + `Query` task functionality using a query term - error if word isn't present 
- [x] 2.0: 'Done' task functionality
- [x] 2.0: 'Delete' task functionality
- [x] 2.0: 'Report' task functionality; shows all tasks (completed and active)
   
## Overall Application (2 points)
--------------------------
- [x] 0.5: Application uses a `main()` function to run the program
- [x] 0.5: Application makes proper use of OOP and procedural code for the application flow
- [x] 0.5: Application uses best practices in code layout and organization (ie. modules)
- [x] 0.5: Application uses best practices in variable names, function arguments, etc.


## Extra Credit  (1 point)
--------------------------
- [x] 1.0 - Extra Credit: make task manager program an executable program and include a README.md file
    - `chmod` a+x
    - Move to a location in `$PATH` (eg. `/usr/local/`, `/usr/bin'`, etc.)

Total
-----
19.5/20
