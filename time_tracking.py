import time_block_module
import datetime
import time
'''
notes:

code time blocks:
start time
notes

track end time

track total time
'''

current_time = datetime.datetime.now()
print("Current time is: " + str(current_time))


#print("Current Date: " + current_time.strftime("%m-%d-%Y"))
#print("Current Time: " + current_time.strftime("%H:%M:%S"))

keep_count = 0
try:
    while True:
        raw_input("Press (Enter) when ready to start a time block. Press (ctrl+c) to stop.")
        time_block = time_block_module.TimeBlock()
        print("Start Time = " + time_block.start_time.strftime("%H:%M:%S"))
        raw_input("Press (Enter) when ready to stop this time block.")
        keep_count +=1
except KeyboardInterrupt:
    pass
        

print("\nTotal number of time blocks added = " + str(keep_count))
