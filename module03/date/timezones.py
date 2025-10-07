

from datetime import datetime 
import pytz

print(pytz.all_timezones)
  
timeZ_Kl = pytz.timezone('Asia/Kolkata')  
timeZ_Ny = pytz.timezone('America/New_York') 
timeZ_Po = pytz.timezone('Poland') 
  
dt_Kl = datetime.now(timeZ_Kl) 
dt_Ny = datetime.now(timeZ_Ny) 
dt_Ma = datetime.now(timeZ_Po) 

print("Kolkata", dt_Kl)
print("New_York", dt_Ny)
print("Poland", dt_Ma)