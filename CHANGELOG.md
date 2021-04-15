CHANGELOG
=========

# v1.3.0.0
- Fix
  ---
  - Fixed recursion errors upon calling `stop()`
  - Fixed custom title not showing up when a custom title was specified

- Add
  ---
  - Added a feature which enables the displaying of python errors

- Change
  ------
  - Changed the publicity of the variables under `Console` so that it won't be easy to access

# v1.2.2.0 (9 April 2021)
- Fix
  ---
  - Fixed another printing error in the `print_replace_line()` method (Again)

# v1.2.1.0 (9 April 2021)
- Fix
  ---
  - Fixed another printing error in the `print_replace_line()` method

# v1.2.0.0 (7 April 2021)
- Fix
  ---
    - Fixed potential issues in the `print_replace_line()` method
    - Fixed an issue involving programs crashing upon entering an empty input into the input bar

- Add
  ---
    - Added the ability to schedule tasks via `schedule_task()`
    - Added the ability to schedule recurring tasks via `schedule_recurring_task()`
    - Added the ability to unschedule tasks via `unschedule_task()`
    - Added the ability to enable user input via `enable_input()`
    - Added the ability to disable user input via `disable_input()`
    - Added the ability to close instance of the console via `stop()`

- Remove
  ------
    - Removed comments in `structure.kv`
  
- Change
  ------
    - Changed `arguments` requirement for command functions to `args`

# v1.1.1.0 (6 April 2021)
- Fix
  ---
    - Fixed issues with the `print_replace_line()` method

# v1.1.0.1 (5 April 2021)
- Fix
  ---
    - [ HOTFIX ] Removed debug messages
  
# v1.1.0.0 (5 April 2021)
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

# v1.0.0.2 (3 April 2021)
- Fix
  ---
    - [ HOTFIX ] Fixed "structure.kv" not found error and other potential "final not found" errors
    - [ HOTFIX ] Fixed new lines appearing before greeting message

# v1.0.0.1 (3 April 2021)
- Fix
  ---
    - [ HOTFIX ] Changed default greeting text to fit with current version
  
- Add
  ---
    - Added GitHub and PyPi URLS to README.md

# v1.0.0.0 (3 April 2021)
- First Release!