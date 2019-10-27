
def byte_designator(M, An, L, O, I1, I2_in, IBP, SBP, LOC, OT, S1, S2):


	OT0,OT1, OT2, OT3,OT4, OT5 = OT
	OS1 = 0
	OS2 = 0
	OS3 = 0
	OS4 = 0
	OS5 = 0
	OS6 = 0


	i1_s=I1.strip("1")
	i2_s=I2_in.strip("2")
	if i1_s != "N" or i2_s != "N":
		stat = 0 ##alarm
	elif i1_s == "N" or i2_s == "N":
		stat = 1 ##"NORMAL"
	if i1_s != "O" and i2_s != "O":
		sd = 1 #"DUAL MON"	
	elif (i1_s == "O" and (not i2_s == "O")) or (not i1_s == "O" and i2_s == "O"):
		sd = 0 #"SINGLE MON"	

	if IBP == 1 :
		bp1= 1 #"ACTIVE"
	elif IBP == 0 :
		bp1= 0 #"OFF"
	
	if SBP == 1 :
		bp2=1 #"ACTIVE"
	elif SBP == 0 :
		bp2=0 #"OFF"	
	if LOC == 1:
		lc = 1 # "LOCAL"
	elif LOC == 0:
		lc = 0 # "REMOTE"

	if OT0 == 1:
		OS1 = 1 #"MAINTENANCE ALERT"
	if OT1 == 1:
		OS2 = 1 # "REMOTE CONTROL FAULT"
	if OT2 == 1:
		OS3 = 1 #"BATTERY FAULT"
	if OT3 == 1:
		OS4 = 1 #"ON BATTERY"
	if OT4 == 1:
		OS5 = 1 #"INTERLOCKED OFF"	
	if OT5 == 1:
		OS6 = 1 #"LCU POWER OK"		


	M_s =int( M.strip("M")) ##main tx
	An_s = int(An.strip("A")) ##tx to ant
	L_s = int(L.strip("L")) ## tx to load
	O_s = int(O.strip("O")) ## tx off
	if i1_s == "N":
		IN_1 = 0

	elif i1_s == "P":
		IN_1 = 1

	elif i1_s == "S":
		IN_1 = 2

	else:
		IN_1 = 3


	if i2_s == "N":
		IN_2 = 0

	elif i2_s == "P":
		IN_2 = 1

	elif i2_s == "S":
		IN_2 = 2

	elif i2_s == "O":
		IN_2 = 3


		
	s1_s=S1.strip("1")
	s2_s=S2.strip("2")

	if s1_s == "N":
		ST_1 = 0

	elif s1_s == "P":
		ST_1 = 1

	elif s1_s == "S":
		ST_1 = 2

	else:
		ST_1 = 3
			
	
	if s2_s == "N":
		ST_2 = 0

	elif s2_s == "P":
		ST_2 = 1

	elif s2_s == "S":
		ST_2 = 2

	elif s2_s == "O":
		ST_2 = 3

	#tp = '{:03b}'.format(1) # 1 for SELEX 1150A
	tp = 1
	#nu = '{:03b}'.format(0) # not use
	dl =38 # datalengt
	nu = 0
	ext= 1
	extl=22
	eq = 9 ## 1001 for VOR



	ots = (OS1<<5)+(OS2<<4)+(OS3<<3)+(OS4<<2)+(OS5<<1)+OS6

	tots2 = (eq<<36)+(stat<<35)+(sd<<34)+(M_s<<32)+(An_s<<30)+(L_s<<28)+(O_s<<26)+(ext<<25)+(IN_1<<23)+(IN_2<<21)+(ST_1<<19)+(ST_2<<17)+(bp1<<16)+(bp2<<15)+(lc<<14)+(tp<<11)+(ots<<5)+nu


	totsbin='{:040b}'.format (tots2)



	bin_chunks = [totsbin[8*i:8*(i+1)] for i in range(len(totsbin)//8)]

	ints = [int(x, 2) for x in bin_chunks]
	for i in ints:
		in0 = bytes([ints[0]]) 
		in1 = bytes([ints[1]])

		in2 = bytes([ints[2]]) 
		in3 = bytes([ints[3]])
		in4 = bytes([ints[4]]) 

	bt2= b''.join([in0,in1, in2, in3, in4])

	chars = [chr(x) for x in ints]

	print(bin_chunks)
	print(bt2)

	return bt2
	
def socket_sender(data):
	HOST, PORT = "192.168.8.201", 9998
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
    		sock.connect((HOST, PORT))
    		sock.sendall(data)
    		print ("data sent")
	finally:
    		sock.close()



while(1):

	

	hasFrame, inputImage= cap.read()
	wrapps = inputImage.copy()

	if not hasFrame:
		break



	data =byte_designator(M, A, L, O, I1, I2, IBP, SBP, LOC, OT, S1, S2)
		
	socket_sender(data)




	if cv2.waitKey(1) & 0xFF == ord("q"): 
		break


cap.release() 
cv2.destroyAllWindows()  

