
from my_data import MyOwnData as data
from time import sleep

def send_rpi(info):

	
	for _ in range(5):
		print()



def encode(info,field):
	return int(str(data.block_available+1)+'0'+str(field)+'0'+str(info))
def send_mydata():
	for f,i in enumerate(data.my_info):
		send_rpi(encode(i,f))
		

