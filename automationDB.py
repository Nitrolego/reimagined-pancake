from random import randint
for number in list(range(1,1001)):
	incrementor_string = str(number).rjust(10, "0")
	random_passID = "%010d" % randint(0,15)
	random_driverID = "%010d" % randint(0,10)
	random_pickupaddress = randint(1,10)
	
	if random_pickupaddress == 1:
	    pickupaddress = str(randint(1,100)) + " Lighthaven Street"
	elif random_pickupaddress == 2:
	    pickupaddress = str(randint(1,100)) + " Southelf Tower"
	elif random_pickupaddress == 3:
	    pickupaddress = str(randint(1,100)) + " Wellwood Avenue"
	elif random_pickupaddress == 4:
	    pickupaddress = str(randint(1,100)) + " Whitemist Road"
	elif random_pickupaddress == 5:
	    pickupaddress = str(randint(1,100)) + " Highrose Way"
	elif random_pickupaddress == 6:
	    pickupaddress = str(randint(1,100)) + " Delllyn Place"
	elif random_pickupaddress == 7:
	    pickupaddress = str(randint(1,100)) + " Westhollow Gardens"
	elif random_pickupaddress == 8:
	    pickupaddress = str(randint(1,100)) + " Summerbarrow Place"
	elif random_pickupaddress == 9:
	    pickupaddress = str(randint(1,100)) + " Crystalholt Walk"
	elif random_pickupaddress == 10:
	    pickupaddress = str(randint(1,100)) + " Raylyn Drive"
	
	random_dropoffaddress = randint(1,10)
		
	if random_dropoffaddress == 1:
	    dropoffaddress = str(randint(1,100)) + " Lighthaven Street"
	elif random_dropoffaddress == 2:
	    dropoffaddress = str(randint(1,100)) + " Southelf Tower"
	elif random_dropoffaddress == 3:
	    dropoffaddress = str(randint(1,100)) + " Wellwood Avenue"
	elif random_dropoffaddress == 4:
	    dropoffaddress = str(randint(1,100)) + " Whitemist Road"
	elif random_dropoffaddress == 5:
	    dropoffaddress = str(randint(1,100)) + " Highrose Way"
	elif random_dropoffaddress == 6:
	    dropoffaddress = str(randint(1,100)) + " Delllyn Place"
	elif random_dropoffaddress == 7:
	    dropoffaddress = str(randint(1,100)) + " Westhollow Gardens"
	elif random_dropoffaddress == 8:
	    dropoffaddress = str(randint(1,100)) + " Summerbarrow Place"
	elif random_dropoffaddress == 9:
	    dropoffaddress = str(randint(1,100)) + " Crystalholt Walk"
	elif random_dropoffaddress == 10:
	    dropoffaddress = str(randint(1,100)) + " Raylyn Drive"
	
	random_hour = "%02d" % randint(00,23)
	random_minute = "%02d" % randint(00,59)
	random_day = "%02d" % randint(1,28)
	random_month = "%02d" % randint(1,12)
	random_year = randint(2017,2018)
	random_distance = randint(0,100)
	
	filename = "filename.txt"
	
	string = f"""INSERT INTO ride VALUES ({incrementor_string}, {random_passID}, {random_driverID}, '{pickupaddress}', '{dropoffaddress}', {random_hour}{random_minute}, {random_day}/{random_month}/{random_year}, {random_distance});\n"""
	
	with open(filename, 'a') as file_object:
	    file_object.write(string)
