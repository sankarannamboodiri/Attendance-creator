
## Attendance creator

This application can be used to automatically update attendance of a particular excel sheet. This application can intake two files and mark  'A'and 'P'corresponding to the people who are absent and present respectively.(As the same excel sheet is used repeatedly the attendance will get added with the day's date as the heading)

## Code Requirements

- Make sure that you have installed python on your pc. You can install python from [Python's official website](https://www.python.org)
- Install the browser extension [Google Meet Attendance List](https://chrome.google.com/webstore/detail/google-meet-attendance-li/appcnhiefcidclcdjeahgklghghihfok?hl=en)
#### Python libraries required
- pandas (```pip install pandas```)
- easygui (```pip install easygui```)
- openpyxl(```pip install openpyxl```

## Usage
- Make an excel file with extension .xlsx  containing the names of people on the meeting (CLASS LIST).
- Ensure that the first row of the excel is labelled "names" 
- A column named "\present" and "\absent" must be added at the end of the excel sheet
- This application is optimised to work with the chrome extension  [Google Meet Attendance List](https://chrome.google.com/webstore/detail/google-meet-attendance-li/appcnhiefcidclcdjeahgklghghihfok?hl=en) which is available on the chrome web store
- The list of people present in the meeting (TODAYS LIST) must be in ".csv" format. Ensure that the first row of this excel is labelled "'Full Name'". (These requirements will be automatically met if the above mentioned extension is used to save the list of peoples present in the meeting)
- The program can be executed by the command
``` attendance_creator.py```
