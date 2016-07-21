import time
now = time.localtime()
hour = now.tm_hour
print(hour)
if hour < 8:
    print ('sleep')
elif hour < 17:
    print ('work')
elif hour < 20:
    print ('eat')
else:
    print ('sleep')

