CHANGELOG
=========

v1.2.0.0
--------
- Fix
  ---
    - Fixed potential issues in the `print_replace_line()` method

- Add
  ---
    - Added a scheduler task method called `schedule_task()`
    - Added a recurring scheduler task method called `schedule_recurring_task()`
    - Added an unscheduler method called `unschedule_task()`
    - Added a user input enabler method called `enable_input()`
    - Added a user input disabler method called `disable_input()`

- Remove
  ------
    - Removed comments in `structure.kv`

v1.1.1.0 (6 April 2021)
-----------------------
- Fix
  ---
    - Fixed issues with the `print_replace_line()` method

v1.1.0.1 (5 April 2021)
-----------------------
- Fix
  ---
    - [ HOTFIX ] Removed debug messages
  
v1.1.0.0 (5 April 2021)
-----------------------
- Fix
  ---
    - Fixed code commenting inconsistencies
    - Fixed debug messages appearing in the console
  
- Add
  ---
    - Added `print_replace_line()` method in `Console()` to allow for replacing of text
    - Added a feature that upon specifying an empty string to the `greeting_text` parameter in `Console()`, no new lines 
      are produced
    - Added a requirement so that functions assigned to a command need to have an `arguments` parameter
    - Added the ability to use custom fonts
  
- Change
  ------
    - Changed `new_line()` method to `print_new_line()` for clarity

v1.0.0.2 (3 April 2021)
-----------------------
- Fix
  ---
    - [ HOTFIX ] Fixed "structure.kv" not found error and other potential "final not found" errors
    - [ HOTFIX ] Fixed new lines appearing before greeting message

v1.0.0.1 (3 April 2021)
-----------------------
- Fix
  ---
    - [ HOTFIX ] Changed default greeting text to fit with current version
  
- Add
  ---
    - Added GitHub and PyPi URLS to README.md

v1.0.0.0 (3 April 2021)
-----------------------
- First Release!