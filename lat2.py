print "\t\t\t\tTugas"
print "********************"

NAMA  = raw_input("MASUKKAN NAMA ANDA   :")
NIM   = input("MASUKKAN NIM ANDA        :")
UTS   = input("MASUKKAN NILAI UTS ANDA  :")
UAS   = input("MASUKKAN NILAI UAS ANDA  :")
TUGAS = input("MASUKKAN NILAI TUGAS ANDA:")

print "***********************************"

print "NAMA ANDA ADALAH       :",NAMA
print "NIM ANDA ADALAH        :", NIM
print "NILAI UTS ANDA ADALAH  :", UTS
print "NILAI UAS ANDA ADALAH  :", UAS
print "NILAI TUGAS ANDA ADALAH:", TUGAS

akhir =(UTS+UAS+TUGAS)/3

print "NILAI AKHIR ANDA   :", Akhir
print "************************"

if akhir >=80 :
    print "A"
    print "Lulus"
    
elif akhir >=75 :
    print "B"
    print "Lulus"
    
elif akhir >=70 :
    print "C"
    print "Tidak Lulus"
    
elif akhir >=50 :
    print "D"
    print "Tidak Lulus"
    
elif akhir <=30 :
    print "E"
    print "Tidak Lulus"
    
