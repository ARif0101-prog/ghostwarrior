import jwt
import requests
import json
from time import time
  
  
# Enter your API key and your API secret
API_KEY = 'c-LJtS__Q2GZtJcx4SL1lg'
API_SEC = 'ZL40SbHpXuk1Kd0vnwz8zdr2usKE1nQTyz3H'
  
# create a function to generate a token 
# using the pyjwt library
def generateToken():
    token = jwt.encode(
        
        # Create a payload of the token containing 
        # API Key & expiration time
        {'iss': API_KEY, 'exp': time() + 5000},
          
        # Secret used to generate token signature
        API_SEC,
          
        # Specify the hashing alg
        algorithm='HS256'
    )
    return token
  
  
# create json data for post requests
meetingdetails = {"action": "recover"
            
  
                  }
  
# send a request with headers including 
# a token and meeting details
def createMeeting():
    headers = {'authorization': 'Bearer %s' % generateToken(),
               'content-type': 'application/json'}
    r = requests.put(
        f'https://api.zoom.us/v2/meetings/75856596095/status', 
      headers=headers, data=json.dumps(meetingdetails))
  
 #   print("\n creating zoom meeting ... \n")
    # print(r.text)
    # converting the output into json and extracting the details
 #   y = json.loads(r.text)
  #  join_URL = y["join_url"]
  #  meetingPassword = y["password"]
  
  #  print(y)
    #    f'\n here is your zoom meeting link {join_URL} and your \
    #    password: "{meetingPassword}"\n')
  
  
# run the create meeting function
createMeeting()
