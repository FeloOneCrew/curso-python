from urllib import response
import urllib.request

url = 'https://es.wikipedia.org/wiki/Deportivo_Independiente_Medell%C3%ADn'
response = urllib.request.urlopen(url)

print(type(response))
print(response.read())