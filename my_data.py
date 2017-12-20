

class MyOwnData():
	protocol=1
	pulselength=350

	my_uid=0
	got_signal=False
	initial_check_timeout=2
	all_data_received=False
	at_the_end=999999
	block_available=0
	slot_available=0
	block1_timeout=1

	all_block_timeout=2
	my_info=[
		5666,
		8999,
		96,
		361,
		123,
		2]
	#long,lat,speed,direction,uid,time_slot
	sotdma=[[0 for _ in range(6)] for i in range(5)]