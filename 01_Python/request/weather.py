# pip install virtualenv 
# python -m venv env 
# env\Scripts\activate
# pip install requests
# pip freeze > requirements.txt

import requests
def weather_app():
    info = input("Enter city name: ")
    city = info.capitalize()
    api_url = f"http://api.weatherapi.com/v1/current.json?key=9c9940e9e1bf4e4ca6013952243112&q={city}&aqi=no"
    # response => api .request _. get, post, put/patch, delete
    # data -> json formta 
    response = requests.get(api_url)
    # respons lai convert json()
    originaljson = response.json()
    location = [originaljson['location']['name']]
    temp_c = [originaljson['current']['temp_c']]
    print(location, temp_c)
weather_app()


def currencyConvert():
    info = input("Enter amount: ")
    ints = int(info)
    api_url ="https://api.currencyapi.com/v3/latest?apikey=cur_live_Osd0mW3tddX3YhYiYBbvc1HtnCXcsdRzHd0QQjGC&currencies=USD&base_currency=NPR"
    response = requests.get(api_url)
    # respons lai convert json()
    originaljson = response.json()
    print(originaljson['data']['USD']['value'] * ints)

currencyConvert()