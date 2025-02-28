#!/usr/bin/env python3
import requests
import json
import configparser
from colorama import Fore, Style

# Load configuration from file
config = configparser.ConfigParser()
config.read("config.ini")

# Global Variables
TOKEN_URL = "https://identity.filevine.com/connect/token"
CLIENT_ID = config["AUTH"]["CLIENT_ID"]
CLIENT_SECRET = config["AUTH"]["CLIENT_SECRET"]
PAT = config["AUTH"]["PAT"]
SCOPES = config["AUTH"]["SCOPES"]

def get_bearer_token():
    """Requests a bearer token from the Filevine Identity endpoint."""
    
    # Prepare authentication payload
    payload = {
        "grant_type": "personal_access_token",
        "token": PAT,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "scope": SCOPES
    }
    
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    
    # Request token
    response = requests.post(TOKEN_URL, data=payload, headers=headers)
    response.raise_for_status()  # Raise an error for HTTP issues
    print(Fore.GREEN + "Success 200 OK!" + Style.RESET_ALL)  

    return response.json()

def main():
    """Main execution method."""
    try:
        token_response = get_bearer_token()
        print("Bearer Token Response:")
        print(json.dumps(token_response, indent=4))  # Pretty print JSON
    except Exception as e:
        print(Fore.RED + "Error:" + Style.RESET_ALL, e)

if __name__ == "__main__":
    main()