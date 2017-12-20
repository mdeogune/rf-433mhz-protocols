from my_data import MyOwnData as data
import time
current_time=int(time.ctime()[14:16])
current_block_o=round(current_time/(data.all_block_timeout))

def rpi_module(i):
	print("rpi code") 
	c=0
	lst=[]


	#----------------
	return (str(data.block_available+1)+'0'+str(i+1)+'0'+str(data.my_info[i]))#str(max(lst,key=lst.count))

def receive(i):
	
	dta=rpi_module(i)
	print(dta)
	
	current_block=round(current_time/(data.all_block_timeout))
	if dta:
		data.got_signal=True

		
		if dta==data.at_the_end:
			data.all_data_received=True
		
		block,field,info=dta.split("0")
		data.sotdma[int(block)][int(field)-1]=info
		
		print(data.sotdma)
		
			






