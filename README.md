# restapi

#Requirements:
	pip install httpie

#All the commands return json.

#Gives all the stored cities:
	http http://saiyan.pythonanywhere.com/places/

#To add a city:
	http http --json POST http://saiyan.pythonanywhere.com/places/ city="City_Name" latitude=value longitude=value
	
	eg. http --json POST http://saiyan.pythonanywhere.com/places/ city="Varanasi" latitude=25.3176 longitude=82.9739

#To search for a city (this also gives cities nearby):
	http http://saiyan.pythonanywhere.com/places_near/<searchKeyword>/
	
	eg. http http://saiyan.pythonanywhere.com/places_near/noida/

