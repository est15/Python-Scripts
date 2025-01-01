# Uses beenpwn-api venv
import requests
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

# initialize colorama
colorama_init()

# HIBP Connection Variables
hibp_apk = "api-key-here" # CHANGE THIS
hibp_user_agent = "custom user-agent header" # CHANGE THIS

hibp_domain = "haveibeenpwned.com"
hibp_path = "api/v3"
request_headers = {'user-agent': hibp_user_agent, 'hibp-api-key':hibp_apk}
services={0:"Exit", 1:"breachedaccount", 2:"pasteaccount", 3:"subscription"} 
runner = True

# Run's the Select Service && Gets Necessary Parameters
def getService(serviceID:int) -> str:
    """Runs the user's selected service and then gets the necessary parameters."""
    hibp_service = services[serviceID]
    hibp_parameter = ""
    try:
        # Emails
        if hibp_service == "breachedaccount":
            hibp_parameter = input("\nEnter Email: ")
        # Pastes 
        elif hibp_service == "pasteaccount":
            hibp_parameter = input("\nEnter Email: ")
        # Subscription Status 
        elif hibp_service == "subscription":
            hibp_parameter = "status"
            # Execute API Request with Correct Parameters:
            url = f"https://{hibp_domain}/{hibp_path}/{hibp_service}/{hibp_parameter}"
            r = requests.get(url, headers=request_headers)
            print(r.json())
            return
        # Exiting 
        elif hibp_service == "Exit":
            print("Goodbye!")
            exit()
        
        else:
            print("Sorry that option is not available yet :(")
            return    
        # Execute API Request with Correct Parameters:
        url = f"https://{hibp_domain}/{hibp_path}/{hibp_service}/{hibp_parameter}?truncateResponse=false"
        r = requests.get(url, headers=request_headers)
        
        # Store the Reponse:
        # HIBP API returns a list containing dictionaries where each
        # dictionary is a breach the account was found in
        content = r.json()

        if r.status_code == 200:
            print(f"{Fore.YELLOW}*****{Style.RESET_ALL}  {Fore.RED}BREACHES FOR {hibp_parameter}{Style.RESET_ALL} {Fore.YELLOW}*****{Style.RESET_ALL} \n")
            # Return Formatted Information for Our Query Parameters
            for breach in range(len(content)):
                print(f"{Fore.RED}Breach #{breach+1}: {Fore.BLUE}{Style.BRIGHT}{r.json()[breach]['Name']}{Style.RESET_ALL}", end=" ")
                print(f"({r.json()[breach]['BreachDate']})")
        else:
            print(f"No data found for {hibp_parameter}\n")
    except Exception as e:
        print(e)

def runHIBPCheck():
    global runner
    while runner:
        # Get User Service to Execute:
        print("""
Select the service that you would like to execute:
    [1]  Breached Account (email address)
    [2]  Pastes (email address)
    [3]  API Subscription Status

    [0]  Exit
            """)
        service = getService( int( input("\nService: ") ) )

if __name__ == "__main__":
    runHIBPCheck()