## deHashQuery
Short Python script to query the DeHashed API and store output into a text file for additional searches. Requires that you have both a [DeHashed subscription](https://dehashed.com/pricing) and purchased access to their [API](https://dehashed.com/api). Which at the time of writing this was about $3 / 100 queries for personal accounts.   

### Usage:
```python
usage: deHashQuery [-h] -f FILE

Quickly gather results and information from DeHashed's database using their API.

options:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Specify directory and/or file to store results in. If no file specified then default naming will
                        be based off current timestamp.
```
### Execution Example Output
![DeHashed API Linux](/assets/deHashQuery/Sample%20Script%20Execution.png)

### To Do:
- Add check to append to file if it already exists
- Add help() function for Advanced Queries to support / explain RegEx
- Add ability to change set variables

