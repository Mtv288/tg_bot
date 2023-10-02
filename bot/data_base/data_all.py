import csv

with open('C:/TrueShop2site/All.csv', encoding='utf-8') as df:
    reader = csv.DictReader(df, delimiter=';')
    for i in reader:
        print(i['group_name'])


