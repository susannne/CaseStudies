from datafile import read_excel

trips = []

trips = read_excel("/home/runner/case_studies_trips_09-10_2017.xlsx", "Blatt1")
#call function in main and save returned items in trip list

#example to call objects

print(trips[0])  #first trip object
print(trips[4].lat_arr)  #latitude of arrival location of 5th trip

for trip in trips:  # column of required seats
	print(trip.seat_req)
