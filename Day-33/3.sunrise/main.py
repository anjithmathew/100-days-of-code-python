import requests

parameters ={
LATI = 9.796314
LONGI = 77.126793
data =  requests.get(f"https://api.sunrise-sunset.org/json?&lat={LATI}&lng={LONGI}")


print(data.json())

