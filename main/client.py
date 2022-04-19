
from multiprocessing.sharedctypes import Value
from nis import match
from unittest import case
from click import option
import requests
import sys

def main(operation , *args ):
    
    if(operation == '-p'):
        url = 'http://127.0.0.1:8000/data'
        payload = '{"key": "32", "value": "Lucia"}'
        headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
        r = requests.post(url, data=payload, headers=headers)
        
    if(operation == '-g'):
        url = 'http://127.0.0.1:8000/data/' + args[2]
        headers = {'accept': 'application/json'}
        r = requests.post(url, headers=headers)

    if(operation == '-u'):
        print("update")
        
    if(operation == '-d'):
        print("delete")

        
    
    



if __name__ == "__main__":
    operation = sys.argv[1]
    main(operation , sys.argv )