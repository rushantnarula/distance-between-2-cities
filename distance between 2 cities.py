from geopy.geocoders import Nominatim
import geopy.distance

geoLocator = Nominatim(user_agent="my-application")

# Enter two points
startPoint = input("Choose starting point: ")
endPoint = input("Choose ending point: ")

# Latitude and Longitude of starting point
locStart = geoLocator.geocode(startPoint)
print("latitude is :", locStart.latitude, "\nlongitude is:", locStart.longitude)

# Latitude and Longitude of ending point
locEnd = geoLocator.geocode(endPoint)
print("latitude is :", locEnd.latitude, "\nlongitude is:", locEnd.longitude)

# Calculating distance between two places using latitudes and longitudes in kilometers
coOrd_1 = (locStart.latitude, locStart.longitude)
coOrd_2 = (locEnd.latitude, locEnd.longitude)
print(geopy.distance.distance(coOrd_1, coOrd_2).km)

