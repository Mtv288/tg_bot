from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import Session
from table_models import AllData, Base
import csv

engine = create_engine('sqlite:///data_all.db')
metadata = MetaData()

Base.metadata.create_all(engine)
session = Session(engine)

with open(r'C:\TrueShop2site\All.csv') as exs:
    reader = csv.DictReader(exs, delimiter=";")

    for i in reader:
        user = AllData(code=i['code'], name=i['name'], photo=i['photo'],
                       price=i['price'], quantity=i['quantity'], size=i['Размер'])

        session.add(user)
    session.commit()
    session.close()
