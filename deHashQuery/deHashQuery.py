import requests # Handle API Requests
from json import loads # Convert JSON Object into iterable object
import pathlib # File Paths
import argparse # CLI Arguments
import logging, sys # Store to File and Print to Terminal
from time import strftime, sleep # rate limit searches (which isnt implemented yet) and get time for log filename

# DeHashed Operator Characters
# Escape the char if detected in search query
# reservedChars = r"+-=&&||><!(){}[]^~*?:\\" // Not Implemented yet

# Key Variables
apiKey = '<change this>' # CHANGE THIS
email = '<change this>' # CHANGE THIS
fieldTypes = ["id", "email", "ip_address", "username", "password", 
              "hashed_password", "hash_type", "name", "vin", 
              "address", "phone", "database_name"]

# LOGGING CONFIGURATION
def configureLog(logFile):
    """Initialize the logging object"""
    logging.basicConfig(
        level=logging.INFO,
        format="%(message)s",
        handlers=[logging.FileHandler(logFile), logging.StreamHandler(sys.stdout)],
    )

# Returns JSON API Request Results
def runQuery() -> dict:
    """ Gets Field Type and Query to Search for then returns the JSON API request's result(s)"""

    # Question Banner
    print(f"""
\n[*] Provide the Following:
    [1]  TYPE   [id, email, ip_address, username, 
                password, hashed_password, hash_type, 
                name, vin, address, phone, database_name]
    
    [2]  QUERY  The item that is going to be searched for against 
                in DeHashed's database (i.e. johnsmith@email.com)
          
    [3]  RSLTS  Control total number of results to be returned 
                [DEFAULT: 100 | MAX: 10,000]
""")
    
    # Reset Variables
    validField = False
    validNum = False
    extraParams = False
    apiSearchString = ""
    dehashFieldParams = []
    dehashQueryParams = []

    # Get and Validatae Field Type
    while not validField:
        fieldTypeInput = input(r"Field Type: ").strip() 
        if not fieldTypeInput or fieldTypeInput not in fieldTypes:
            print("[-] Invalid Field Type")
        else:
            dehashFieldParams.append(fieldTypeInput)
            
            # Ensure They Answer Y or N 
            innerWhile = False
            while not innerWhile:
                fieldAddParams = input("[*] Combine Additional Parameters? [Y/N]: ").lower()
                if fieldAddParams == 'y':
                    extraParams=True
                    break
                elif fieldAddParams == 'n':
                    validField=True
                    innerWhile = True
                    break
                else:
                    print("[-] Response must be y or n")
                    

    # Get Query(s) for each field
    for field in range(len(dehashFieldParams)):
        while True:
            dehashQueryInput = input(f"\n({dehashFieldParams[field]}) Search Query: ").strip()
            if dehashQueryInput:
                dehashQueryParams.append('\"' + dehashQueryInput + '\"')
                break
            else:
                print("[-] Query cannot be empty")
        
    # Build base API Search Query
    apiSearchString = f'{dehashFieldParams[0]}:{dehashQueryParams[0]}'
    
    # Build the Query for Additional Parameters
    if extraParams:
        additionalParams = [fr"&{field}:{value}" for field, value in zip(dehashFieldParams[1:], dehashQueryParams[1:])]
        apiSearchString = apiSearchString + "".join(additionalParams)
        
    # Max number of results restuls to return
    while not validNum:
        userNum = int(input("Results Size: ").replace(",", "").replace(".", ""))
        if userNum <= 0:
            print("[-] Minimum size is 1")
            continue
        elif userNum > 10000:
            print("[-] Minimum size is 1")
            continue
        # Made it here == valid number
        validNum = True
        apiSearchString = apiSearchString + f"&size={userNum}"
        break
    
    # Pretty Log print
    parameters = [param + " " for param in apiSearchString.split("&")] 
    # LOG THIS SEARCH 
    logging.info(fr'{"-"*5} RESULTS FOR: ' + " ".join(parameters) + fr'{"-"*5}')

    # DeHashed Only Accepts application/json
    headers = {"Accept":"application/json"}
    
    # Create Browser Object
    browser = requests.Session()
    
    # Basic Authentication
    browser.auth = (f"{email}", f"{apiKey}")
    queryResults = browser.get(fr'https://api.dehashed.com/search?query={apiSearchString}',
                               headers=headers)
    

    # Return JSON dictionary of DeHashed Items 
    return loads(queryResults.text)

def logResults(jsonData:dict):
    """Iterate through each group of items returned from DeHashed API"""

    # The Entries Name contains a list of dictionaries of our relevant data 
    databaseValues = jsonData['entries']
    logging.info(f"[*] Total Result Groups: {len(databaseValues)}")
    
    # Iterate through returned groups of data that matched search critiera
    for entry in range(len(databaseValues)):
        logging.info(f"\n[*] Query Result #{entry+1}:")
        
        # Iterate through the actual fieldnames and values
        for fieldName in databaseValues[entry]:
            fieldValue = databaseValues[entry][fieldName]
            
            # Skip if field = id
            if fieldName == 'id':
                pass
            
            # Ensure value is not empty (empty strings = False in Python)
            elif fieldValue:
                logging.info(f"{fieldName} : {fieldValue}")
    
    # Print Time to Complete Query
    logging.info(fr"{'-'*5} Query Took: {jsonData['took']} {'-'*5}")
    return

def advancedQueriesHelp():
    print(f"[-] Not Written Yet")
    return

def main():
    status = False
    configureLog(logFile)

    while not status:
        # Print Banner
        print(f"""
\nDeHashed API Search Options:
    [1]  QUERY   Run a query against DeHahsed's Database
    [2]  HELP    Prints more avanced query operations.

    [0]  EXIT
""")
        programDirection = input("[*] CHOICE: ").strip()
        
        if programDirection == '0':
            status=True
            break
        elif programDirection == '1':
            # Send JSON DeHashed Query Results to Log Function 
            logResults(runQuery())
        elif programDirection == '2':
            print("[-] Not Programmed just yet")
        
# Ensure Program is Executed Directyl and not imported
if __name__ == "__main__":
    try:
        # Intialize argparse
        parser = argparse.ArgumentParser(prog="dehashQuery",
                                        description="Quickly gather results and information from Dehashed's database use their API.")
        # Define CLI Arguements
        logFileArg = parser.add_argument('-f', '--file',
                                    help="Specify directory and file to store results in. If no file specified then default naming will be based off timestamp.",
                                    required=True)
        
        # SIZE CONTROLLED THROUGH CLI ARG
        # [!] ran into some issues validating values from the cli position with the argument
        # [!] probably better to also give user the option to change it during execution
        #sizeofResults = parser.add_argument('-s', '--size',
        #                                    help="Number of results to return from query [DEFAULT: 100] [MAX: 10,000]",
        #                                    required=True)
        
        # Store Arguemnts in Program's Namespace:
        args = parser.parse_args() 

        # Ensure logFile is in Global namespace
        global logFile
        global querySize

        # See if Log File is Provided by Checking if the file exists (assuming the directories do)
        logFile = pathlib.Path(args.file)
        if not logFile.exists():
            logFile.touch()
        else:
            # Create the Default Named Log File
            logFile = logFile / strftime(f"%Y-%m-%H%M%S.txt")
            logFile.touch()
        
        # Run the program
        main()
    except Exception as e:
        print(f"[-] Error Occurred: {e}")

    # Good Bye Statement
    print("Buh Bye!")
