
#자바스크립트의 a.jax

import requests

response_data = requests.get("http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99")

city_air = response_data.json()  #json 형태로 바꿔줌

print(type(city_air))
print(city_air)

print(city_air['RealtimeCityAir']['row'][0]['MSRSTE_NM'])

city_list =city_air['RealtimeCityAir']['row']

for city in city_list:
    #todo PM10이 20보다 작은 구 이름만 찎어주세요
    if city['PM10']< 20:
        print(city['MSRSTE_NM'])


