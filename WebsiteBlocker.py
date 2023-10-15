from time import sleep
from datetime import *
print('Enter starting time in format "date:hour:min:sec"')
day1_dt, day1_hr, day1_min, day1_sec=[int(x) for x in input().split(':')]
print('Enter ending time in format "date:hour:min:sec"')
day2_dt, day2_hr, day2_min, day2_sec=[int(x) for x in input().split(':')]
#Windows host file path
hostsPath=r"C:\Windows\System32\drivers\etc\hosts"
ip_address="127.0.0.1"
websites=[]
a=datetime.now()
b=datetime(datetime.now().year,datetime.now().month,day1_dt, day1_hr,day1_min,day1_sec)
c=datetime(datetime.now().year,datetime.now().month,day2_dt,day2_hr,day2_min,day2_sec)
check= False
while True:
   #Durationdatetime
   if(a<b):
      check=True 
      websites=input("enter the websites to block separated by ','").split(',')
      print("Websites will be blocked from the specified beginning time")
      f=datetime.now()
      x=b-f
      time_diff1=x.total_seconds()
      sleep(time_diff1)
      a=datetime.now()
   elif b<c:
       if(check==False):
           websites=input("enter the websites to block separated by ','").split(',')
       with open(hostsPath,'r+') as file:
          content = file.read()
          for site in websites:
             if site in content:
                pass
             else:
                file.write(ip_address+" "+site+"\n")   
       f=datetime.now()
       y=c-f
       time_diff2=y.total_seconds()
       sleep(time_diff2)
       b=datetime.now()
       a=datetime.now()
   else:
        with open(hostsPath,'r+') as file:
          content = file.readlines()
          file.seek(0)
          for line in content:
            if not any(site in line for site in websites):
               file.write(line)
          file.truncate()
          print("All websites are unblocked")
        break
