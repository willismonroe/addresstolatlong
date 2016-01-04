
import googlemaps
import csv

gmaps = googlemaps.Client(key='xxx')

print("Connected to GoogleMaps API.")

print("Reading addresses from adds.csv file.")

addrList = []

with open("adds.csv") as csvfile:
	reader = csv.reader(csvfile, dialect='excel-tab')
	next(reader, None)
	for row in reader:
		addrList.append(row)

print("Got addresses:")
print(addrList)

print("Querying GoogleMaps.")

latlongList = []

for address in addrList:
	result = gmaps.geocode(address)
	if result == []:
		print("No result for {}.".format(address[0]))
		latlongList.append([address[1],address[0],"ERROR","ERROR"])
	else:
		latlong = result[0]["geometry"]["location"]
		latlongList.append([address[1],address[0],latlong["lat"],latlong["lng"]])
		print("Found Latitude and Longitude ({},{}) for: #{} at {}".format(latlong["lat"],latlong["lng"],address[1],address[0]))

print(latlongList)

print("Writing output file.")

with open("latlonglist.csv", "wb") as csvfile:
	writer = csv.writer(csvfile, dialect='excel-tab')
	writer.writerow(["localaddres_ed","rollnumber","Latitude","Longitude"])
	for entry in latlongList:
		writer.writerow(entry)

print("Writing done, open latlonglist.csv.")
