import random

print ("Selamat Datang Di LOVEMETER")

namadia = input ("Masukkan Nama Dia : ")

cocok= random.random()
print ("Kecocokan Anda", cocok * 100, "%")

if cocok > 0.8:
    print ("Anda Sangat Cocok Dengan " + namadia + "!")
elif 0.5 <= cocok <= 0.8:
    print ("Anda Lumayan Cocok Dengan " + namadia + "!")
else:
    print ("Anda Tidak Cocok Dengan " + namadia + " :(")