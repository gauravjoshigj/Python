# Author : Gaurav
# Weather forecasting organization wants to show is it day or night.
# So, write a program for such organization to findwhether is it dark outside or not

import time
mytime = time.localtime()
if mytime.tm_hour < 6 or mytime.tm_hour > 18:
    print ('It is night-time')
else:
    print ('It is day-time')