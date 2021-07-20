import time
import os
import sys

print ("Welcome")
time.sleep(2)
os.system("clear")

#banner1
os.system("pkg install figlet")
os.system("pkg install figlet")
os.system("clear")
os.system("figlet Kizz Calculator")

#banner2
awal = input("Nombor pertama: ")
akhir = input("Nombor Kedua: ")
pilih = raw_input("tambah atau tolak: ")
#kedua
if pilih == "tambah":
   c = awal + akhir
   print "Hasil %d + %d = %d" % (awal,akhir,c)

#ketiga
elif pilih == "tolak":
     c = awal - akhir
     print "Hasil %d - %d = %d" % (awal,akhir,c)