# PwnCheck
A Python script I created to practice working with APIs and retrieving/formatting JSON output. Takes an email as a parameter during program execution to query breach information for that given account. 

## Get API Key
Go to [HIBP API](https://haveibeenpwned.com/API/Key) page, setup an account, and purchase an API key. Now you might be thinking "HIBP is free, why would I pay for this API key...." Very valid point. However: Python. Make sure to update the script with your API Key. 

## Usage:
```markdown
(beenpwn-api) C:\Path\To\Script>python PwnCheck.py

Select the service that you would like to execute:
    [1]  Breached Account (email address)
    [2]  Pastes (email address)
    [3]  API Subscription Status

    [0]  Exit


Service: 1

Enter Email: <email address>
*****  BREACHES FOR <email address> *****

Breach #1: LinkedIn (2012-05-05)
Breach #4: Edmodo (2017-05-11)
Breach #5: Collection1 (2019-01-07)
Breach #6: Houzz (2018-05-23)
Breach #7: PDL (2019-10-16)
Breach #8: Zynga (2019-09-01)
Breach #17: TelegramCombolists (2024-05-28)
Breach #18: BloomsToday (2023-11-11)
```

## Windows Execution Output
![pwnCheck Windows](/assets/pwnCheck/Windows%20Execution.png)

## Linux Execution Output
![pwnCheck Linux](/assets/pwnCheck/Linux%20Execution.png)
