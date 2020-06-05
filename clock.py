from datetime import datetime
from twilio_whatsapp import send_msg
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

# Schedule job_function to be called every two hours
sched.add_job(send_msg, 'interval', minutes=30)

sched.start()