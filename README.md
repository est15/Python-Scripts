# Python-Scripts
Repository to hold my python scripts that don't need an individual repo for.
## Creating Virtual Environments:
For the scripts that depend upon third-party Python modules the use of a virtual environment is recommended for each script. Use the following commands to create a venv:
1. Create the Virtual Environment
```python 
python -m venv <path\to>\<venv-name> 
```
2. Activate Virtual Environment
**WINDOWS (POWERSHELL)**
```powershell
PS C:\>powershell -ep bypass 
PS C:\>. "$env:USERPROFILE\.venv\<venv-name>\Scripts\activate.ps1"
(<venv-name>) PS C:\Users\user>
```

**WINDOWS (CMD)**
```cmd
C:\> python %USERPROFILE%\.venv\<venv-name>\Scripts\activate.bat
(<venv-name>) C:\> 
``` 

**LINUX**
```bash
$ source ~/.venv/<venv-name>/bin/activate
(<venv-name>) $
```
3. Install Python 3rd Party Libraries
```python 
(<venv-name>) $ python -m pip install -r requirements.txt
```

## [Obsidian Vault Attachment Sync](vaultAttachSync/)
Finds all attachments from copied obsidian vault notes and copies them from the original vault into the new vault.
![Script Execution](/assets/vaultAttach/Successful%20Command%20Execution.png)
## [HIBP API Checker](pwnCheck/)
Utilizes HaveIBeenPwned (HIBP)'s API in order to query breach information for requested accounts.  
![pwnCheck Linux](/assets/pwnCheck/Linux%20Execution.png)
## [DeHashed API Query](deHashQuery/)
Utilizes DeHashed's API service in order to query and log results from their database.
![DeHashed API Linux](/assets/deHashQuery/Sample%20Script%20Execution.png) 
