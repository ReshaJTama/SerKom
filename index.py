from os import system
import time


arr = []
n = 1

def optionmenu(i):
	if i == "1":
		input_angka()	
		mainmenu()	
	elif i == "2":
		urutan_angka()
		mainmenu()
	elif i == "3":
		print("Selamat Tinggal")
		time.sleep(3)
		system('cls')
	elif i >= "3":
		system('cls')
		print('==================================================')
		print('=           Pilihan anda Tidak Sesuai            =')
		print('==================================================')
		time.sleep(3)
		mainmenu()

def input_angka():
	head()
	global arr,n
	jml = input("Masukkan jumlah angka yang akan diinput : ")
	while n <= int(jml):
		arr.insert(n,int(input("Masukan Angka "+str(n)+" :")))
		n += 1	
	return arr


def urutan_angka():
	global arr
	n=0
	sort = arr.sort()
	while n < len(arr):
		f = open("list_nomor.txt", "a")

		print("Nilai "+str(n+1)+" :"+str(arr[n]))
		f.write("Nilai "+str(n+1)+" :"+str(arr[n]))
		f.close()
		n += 1

	time.sleep(3)

def head():
	system('cls')
	print('==================================================')
	print('=                Program SERKOM                  =')
	print('=           V.1  By.Resha Jullyantama            =')
	print('==================================================')
	

def mainmenu():
	head()
	print("Main Menu : \n")
	print("1. Masukan Angka \n")
	print("2. Tampil hasil pengurutan \n")
	print("3. Selesai \n")

	optionmenu(input("Pilihan Anda :"))


mainmenu()