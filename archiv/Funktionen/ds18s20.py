def read_DS1820():
	# Die Sensoren müssen mit "modprobe w1-gpio" und "modprobe w1-therm" aktiviert werden!

	# Zeitvariable definieren
	lt = localtime()
	
	
	# 1-Wire Slave-Liste oeffnen
	file = open('/sys/devices/w1_bus_master1/w1_master_slaves') #Verzeichniss evtl. anpassen

	# 1-Wire Slaves auslesen
	w1_slaves = file.readlines()

	# 1-Wire Slave-Liste schliessen
	file.close()

	# Fuer jeden 1-Wire Slave eine Ausgabe
	for line in w1_slaves:
				
		# 1-wire Slave extrahieren
		w1_slave = line.split("\n")[0]

		# 1-wire Slave Datei oeffnen
		file = open('/sys/bus/w1/devices/' + str(w1_slave) + '/w1_slave')

		# Inhalt des 1-wire Slave File auslesen
		filecontent = file.read()

		# 1-wire Slave File schliessen
		file.close()

		# Temperatur Daten auslesen
		stringvalue = filecontent.split("\n")[1].split(" ")[9]

		# Temperatur konvertieren
		temperature = float(stringvalue[2:]) / 1000

		# Temperatur ausgeben
		l.append(str(w1_slave) + ' | %5.3f °C \t  ' % temperature))
	return(l)
