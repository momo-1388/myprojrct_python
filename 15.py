import requests
import re
from bs4 import BeautifulSoup
from sklearn import tree
import mysql.connector

be = ''
vig1 = ''

all_vig_car = list()

clf = tree.DecisionTreeClassifier()

SQL = mysql.connector.connect(
    user='root',
    password='13888',
    host='localhost',
    database='web'
)

r = [requests.get('https://bama.ir/car')]

soups = []

for res in r:
    resp = res.text
    soups.append(BeautifulSoup(resp, 'html.parser'))

for soup in soups:
    all_cars_name_module = soup.find_all('h2', attrs={'itemprop': 'name'})
    all_City_name_car = soup.find_all('span', attrs={'class': 'provice-mobile'})
    all_Kar_car_name = soup.find_all('p', attrs={'class': 'price hiden-xs'})
    for car in all_cars_name_module:
        car_name_module = d = re.sub(r'\s+', ' ', car.text).strip()
        list_on_car_name_module = car_name_module.split('،')
        list_on_car_name_module_Correct = []
        for on_car_name_module in list_on_car_name_module:
            list_on_car_name_module_Correct.append(on_car_name_module.strip())
        if [list_on_car_name_module_Correct[0], list_on_car_name_module_Correct[1]] == be:
            continue
        all_vig_car.append([list_on_car_name_module_Correct[0], list_on_car_name_module_Correct[1]])
    count = 0
    for city_car in all_City_name_car:
        city_car_correct = ''
        all_vig_car[count].append(city_car.text)
        count += 1
    for vig in all_vig_car:
        if vig == vig1:
            continue
        else:
            print(vig)
        vig1 = vig
