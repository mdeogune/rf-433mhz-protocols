
from my_data import MyOwnData as data
from time import sleep
import receive_data as listen_data
import time
current_time=int(time.ctime()[14:16])
current_block_o=round(current_time/(data.all_block_timeout))
current_block=round(current_time/(data.all_block_timeout))
i=0
while(current_block_o+1!=current_block):
	current_block=round(current_time/(data.all_block_timeout))
	
	listen_data.receive(i)
	i+=1
	print("...NO SIGNAL FOUND...")
	sleep(data.initial_check_timeout)
	
slot=[1]*12
if data.all_data_received:
	data.got_signal=False
	for b_a1, a1 in enumerate(data.sotdma):
				
		if a1[0]==0 and a1[1]==0:
			data.block_available=b_a1

			break

	for b_a1, a1 in enumerate(data.sotdma):slot[b_a1]=a1[5]
	slot.sort()
	for a in slot:
		if a==data.slot_available:
			data.slot_available+=1





print(data.block_available)


