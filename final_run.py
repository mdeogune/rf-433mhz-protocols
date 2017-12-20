
from my_data import MyOwnData as data
from time import sleep
from send_data import send_mydata
import time
import initial_run
initial_run
global current_time
global current_block


def update_block():
	current_time=int(time.ctime()[14:16])
	current_block=round(current_time/(data.all_block_timeout))
	return current_time,current_block

current_time,current_block=update_block()
last_current=((current_block-1)*data.all_block_timeout)+data.slot_available

while(1):
	current_time,current_block=update_block()
	if(current_time==last_current):
		break
	last_current=(current_block*data.all_block_timeout)+data.slot_available
	
print("got slot")
send_mydata()

print(data.sotdma)