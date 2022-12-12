import requests
import json
import os
def call_API():
    #Set URI and params for, authentication and extraction
    auth_uri = "https://api.healthjump.com/authenticate"
    demo_uri = "https://api.healthjump.com/hjdw/SBOX02/demographic?first_name=btwn~Patient_A~Patient_C"
    payload={'email': 'sandbox@healthjump.com', 'password': 'R-%Sx?qP%+RN69CS'}

    #Authenticate request
    auth_response = requests.request("POST", auth_uri, data=payload)
    auth_json = auth_response.json()
    
    #Set headers with secret key and authorization token
    demo_headers = {
      'Secretkey': 'yemj6bz8sskxi7wl4r2zk0ao77b2wdpvrceyoe6g',
      'Authorization': "Bearer " + auth_json['token']
    }
    
    #Request for demographic data between Patient_A and Patient_C
    demo_response = requests.request("GET", demo_uri, headers=demo_headers, data=payload)
    
    #Return response formatted as json
    return demo_response.json()


def format_data(data):
    #Sort data by first_name field
    data['data'].sort(key=lambda x: x['first_name'])
    #Format data to make more readable
    return json.dumps(data, indent=2)

def write_to_file(file_name, data):
    #Create and write data file file_name
    outfile = open(file_name, "w")
    outfile.write(data)
    print('API data extracted to ', os.path.abspath(file_name))
    outfile.close()
