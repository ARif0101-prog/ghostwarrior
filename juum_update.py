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
meetingdetails = {"topic": "The te",
                  "type": 1,
                 # "start_time": "2021-06-25T13: 55: 57",
                 # "duration": "45",
                  "timezone": "Asia/Jakarta",
                  "agenda": "test",
  
                 # "recurrence": {"type": 1,
                  #               "repeat_interval": 1
                 #                },
                  "settings": {"host_video": "true",
                               "participant_video": "true",
                               "join_before_host": "False",
                               "mute_upon_entry": "False",
                               "watermark": "true",
                               "audio": "voip",
                               "auto_recording": "cloud",
                               "breakout_room": {"enable":"true",
                                   "rooms":[
                                       {
                                           "name": "room1",
                                           "participants":[
                                               "jojo@gmail.com"
                                               ]
                                       

                                        },
                                       {
                                           "name":"room2",
                                           "participants":[
                                               "deep.phee@gmail.com"
                                               ]
                                           
                                        }
                                       ]
                                   }
                                    
                                        
                                
                               }
                  }
  
# send a request with headers including 
# a token and meeting details
def createMeeting():
    headers = {'authorization': 'Bearer %s' % generateToken(),
               'content-type': 'application/json'}
    r = requests.patch(
        f'https://api.zoom.us/v2/meetings/71533065542', 
      headers=headers, data=json.dumps(meetingdetails))
  
 #   print("\n creating zoom meeting ... \n")
    # print(r.text)
    # converting the output into json and extracting the details
  #  y = json.loads(r.text)
  #  join_URL = y["join_url"]
  #  meetingPassword = y["password"]
  
   # print(
    #    f'\n here is your zoom meeting link {join_URL} and your \
    #    password: "{meetingPassword}"\n')
  
  
# run the create meeting function
createMeeting()
