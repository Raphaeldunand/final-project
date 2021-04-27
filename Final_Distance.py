# Final document to simplify the indication of variables
#python -m pip install haversine
from haversine import haversine, Unit
import urllib.request
import json
from pprint import pprint
import urllib.parse

#Developped by Raphael
#example locations
'Boston'
'newyork'
'Paris'

def lat_long(location1, location2): 
    """
    Function that gets the information of a location based on its name. 
    """
    # global data_latlong
    print(f"Your departure location is {location1} and destination is {location2}")
    #Imports data from the mapquestapi
    MAPQUEST_API_KEY = 'XxtdAMBvWmSKhAKu0wu0kMXQT8gbOp6b'
    # url = f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location=Babson%20College'
    url1 = (f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location={location1}')
    f1 = urllib.request.urlopen(url1)
    response_text1 = f1.read().decode('utf-8')
    data_latlong1 = json.loads(response_text1)
    MBTA_API_KEY = '78c78742ffb14c3cb6b22071c0986b51'

     #Gets the latitude and longitude
    lat1 = data_latlong1["results"][0]["locations"][0]['displayLatLng']['lat']
    long1 = data_latlong1["results"][0]["locations"][0]['displayLatLng']['lng']
    # print(location1)
    # print('lat',lat1)
    # print('long',long1)

    coor1 = (lat1, long1)
    # print(coor1)

    url2 = (f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location={location2}')
    f2 = urllib.request.urlopen(url2)
    response_text2 = f2.read().decode('utf-8')
    data_latlong2 = json.loads(response_text2)


     #Gets the latitude and longitude
    lat2 = data_latlong2["results"][0]["locations"][0]['displayLatLng']['lat']
    long2 = data_latlong2["results"][0]["locations"][0]['displayLatLng']['lng']
    # print(location2)
    # print('lat',lat2)
    # print('long',long2)
    
    coor2 = (lat2, long2)
    # print(coor2)

    # pprint(response_data)

    # boston = (42.358894,-71.056742)
    # boston = (lat, long)'Chelsea,MA'
    # global distance
    dist = haversine(coor1, coor2)
    distance = round(dist, 2)
    # distance = dist
    print(f"The distance between {location1} and {location2} is {distance}km")
    return distance
    # print(haversine(boston, paris))

# lat_long(name)
#The values that are indicated in this function are averages that are in the initial distance.py documet. In order to simplyfy the code
# to get the variable to fit this was the change that was made.  
def travel(typer, distance, people):
    # global em
    # if typer == 'train' or typer == 'Train':
    #     em = 41* distance
    em = 0
    if typer == 'train' or typer == 'Train':
            em = 28 * distance
    elif typer == 'bus' or typer == 'Bus':
        em = 104* distance
    elif typer == 'plane' or typer == 'Plane':
        em = 224.5 * distance 
    elif typer == 'car' or typer == 'Car':
        em = 161.73 * distance
        em = em/people
        
    em = round(em, 2)
    em_round = round(em * 2, 2)
    print(f'You produced {em}g of CO2 on your trip and {em_round}g of CO2 for a round trip')
    return em, em_round


def saved(typer, distance, em):
    if typer == 'train' or typer == 'Train': 
        maxi = distance * 272.55
        saved = round(maxi - em,2)
        percent = round(saved/maxi *100,2)
        print(f"You saved {saved}g of CO2 compared to taking a car. You saved {percent}% of your emissions")
    elif typer == 'bus' or typer == 'Bus':
        maxi = distance * 272.55
        saved = round(maxi - em,2)
        mini = round(distance * 6,2)
        extra_saved = em - mini
        percent = round(saved/maxi *100,2)
        extra_percent = (1-round(mini/extra_saved,2))*100
        print(f"You saved {saved}g of CO2 compared to taking a car. You saved {percent}% of your emissions")
        print(f"You could have only produced {mini}g of CO2 if an electric train alternative was possible, saving an additional {extra_saved}g of CO2 or {extra_percent}%.")
    elif typer == 'plane' or typer == 'Plane':
        maxi = distance * 272.55
        saved = round(maxi - em,2)
        mini = round(distance * 6,2)
        extra_saved = em - mini
        percent = round(saved/maxi *100,2)
        extra_percent = (1-round(mini/extra_saved,2))*100
        print(f"You saved {saved}g of CO2 by taking a plane compared to taking a car alone. You saved {percent}% of your emissions")
        print(f"You could have only produced {mini}g of CO2 if an electric train alternative was possible, saving an additional {extra_saved}g of CO2 or {extra_percent}%.")
    elif typer == 'car' or typer == 'Car':
        maxi = distance * 272.55
        saved = round(maxi - em,2)
        mini = round(distance * 6,2)
        extra_saved = em - mini
        percent = round(saved/maxi *100,2)
        extra_percent = (1-round(mini/extra_saved,2))*100
        print(f"You saved {saved}g of CO2 compared to taking a car alone. You saved {percent}% of your emissions")
        print(f"You could have only produced {mini}g of CO2 if an electric train alternative was possible, saving an additional {extra_saved}g of CO2 or {extra_percent}%.")
    return saved, percent, mini, extra_saved, extra_percent

# stop(data_latlong)
# print('lat2', lat)
# print('long2', long)

def distance_calc():
    """
    Function that adds the input at the beggining and puts the two previous functions together
    """
    # global name1
    # global name2
    # global name3
    # print('Input your departure location')
    name1 = input()
    # name1 = 'Boston,MA'

    # print('Input your departure location')
    name2 = input()
    # name2 = 'Paris'
    distance = lat_long(name1, name2)
    # stop(data_latlong)
    # print("Were you travelling by car, bus, train or plane")
    name3 = input()
    em = travel(name3, distance)
    saved(name3, distance, em)


def main():
    distance_calc()


if __name__ == "__main__":
    main()
