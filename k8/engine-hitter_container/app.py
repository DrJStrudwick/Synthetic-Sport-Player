import os
import requests                                                              #imports

HOST = os.getenv('HOST')                                                     #insert from pod def, should be 'sspengine'
url = 'http://{host}:2001/progress'.format(host=HOST)                        #create url to request too
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}    #setup headers

r = requests.put(url, headers=headers)                                       #make request
