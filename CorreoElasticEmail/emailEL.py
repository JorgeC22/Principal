#!/usr/bin/env python 

# Import necessary modules 
import urllib 
import http.client
import re 

# Globals 
#USERNAME = '<Elastic Email Account Username>' 
API_KEY = 'C102757740BCDFEA499F64303492BE858914A352EF72BEF9A94350439293F90F1A680195BA34FC1C0BA572B20D542377' 
API_SERVER = 'api.elasticemail.com' 
API_URI = '/mailer/send' 
SUCCESS_MATCH_PATTERN = '^[0-9|a-f]{8}-[0-9|a-f]{4}-[0-9|a-f]{4}-[0-9|a-f]{4}-[0-9|a-f]{12}$' 
ERROR_MATCH_PATTERN = '^Error:' 
URL_POST = API_SERVER + '/v2/email/send'

# Function to send e-mail 
def send_email(to_addr, subject, body_text, body_html, from_addr, from_name, reply_to_email=None, reply_to_name=None, channel=None): 

    # Build message structure 
    msg_info = {} 
    #msg_info['username'] = USERNAME 
    msg_info['api_key'] = API_KEY 
    msg_info['from'] = from_addr 
    msg_info['from_name'] = from_name 
    msg_info['to'] = to_addr 
    msg_info['subject'] = subject 
    msg_info['body_text'] = body_text 
    msg_info['body_html'] = body_html 
    msg_info['reply_to'] = reply_to_email 
    msg_info['reply_to_name'] = reply_to_name 
    msg_info['channel'] = channel 

    # Prepare the API call 
    params = urllib.parse.urlencode(msg_info) 
    headers = {'Content-type': 'multipart/form-data'} 

    try: 
    # Connect to the API and send the message 
        conn = conn = http.client.HTTPSConnection(API_SERVER) 
        conn.request('POST', URL_POST, params, headers) 
        response = conn.getresponse() 

        # Read the response from the mail server, close the connection, and return the result 
        ret = response.read() 
        conn.close() 
    except Exception as e: 
         ret = str(e)

    return ret 


result = send_email('jcervantes@tecnocengroup.com', 'Mensaje Prueba', 'Body text', '<b>Body</b> <i>HTML</i>', 'jcrivera@vitaebeneficios.com', 'Jose', 'donotreply@donotreply.com', 'Do not reply', 'Channel Name')
print(result)