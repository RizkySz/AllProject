dictA= {"nama1":"Jane Doe","nama2":"jhon Smith","nama3":"Bob Stone","telp1":"+27 555 5373","telp2":"+27 555 6254","telp3":"+27 555 5689"}

print "Data Nomor Telphone"
print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
print "|   Name   | Telphone Number |"
print "|",dictA["nama1"]," |",dictA["telp1"]," |","\n","|",dictA["nama2"],"|",dictA["telp2"]," |","\n","|",dictA["nama3"]," |",dictA["telp3"]," |"
print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

dictA["telp1"]="+27 555 1024"
print "\nUbah No Telp Jane"
print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
print "|  Name   | Telphone Number  |"
print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
print "|",dictA["nama1"]," |",dictA["telp1"]," |","\n","|",dictA["nama2"],"|",dictA["telp2"]," |","\n","|",dictA["nama3"]," |",dictA["telp3"]," |"

dictA["nama4"]="Anna Copper"
dictA["telp4"]="+27 555 3237"
print "\n Menambah Data Baru "
print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
print "|    Name    | Telephone Number |"
print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
print "|",dictA["nama1"]," |",dictA["telp1"]," |","\n","|",dictA["nama2"]," |",dictA["telp2"]," |","\n","|",dictA["nama3"]," |",dictA["telp3"]," |","\n","|",dictA["nama4"]," |",dictA["telp4"]
print "\n Cetak Nomor Telphone Bob Stone : ",dictA["telp3"]

print "\n Cetak Semua Key : ",dictA.keys()
print "\n Cetak Semua Value : ",dictA.values()
