from twilio.rest import Client 
import os
from pathlib import Path   # Python 3.6+ only
from dotenv import load_dotenv


# OR, explicitly providing path to '.env'
def load_env():
    load_dotenv()

    # OR, the same with increased verbosity
    load_dotenv(verbose=True)
    env_path = Path('.') / '.env'
    load_dotenv(dotenv_path=env_path)

def send_msg():
    load_env()
    #credential
    account_sid = os.getenv("ACCOUNT_SID")
    auth_token = os.getenv("AUTH_TOKEN")
    phone_no = os.getenv("PHONE_NO")
    
    client = Client(account_sid, auth_token) 
    
    
    #send message
    message = client.messages.create( 
                                from_='whatsapp:+14155238886',        
                                to='whatsapp:'+ str(phone_no),
                                body= "love you"
                            ) 
 
    return message.sid
    
# msg = input("enter Msg to send:\n")
sid = send_msg()
print(sid)


