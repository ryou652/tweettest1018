import twitter_api
import schedule,time,datetime

def job():
    now=datetime.datetime.now()
    twitter_api.main()
    print("<<DONE>>",now.strftime('%Y-%m-%d %H:%M:%S'))
print("please wait a minute")
schedule.every(29).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
