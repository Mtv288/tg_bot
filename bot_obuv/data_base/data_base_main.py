from sqlalchemy import create_engine, MetaData, update, exists
from sqlalchemy.orm import Session
from bot_obuv.data_base.table_models import AllData, Base, MenShoes, Catalog
import csv


engine = create_engine('sqlite:///data_all.db')
metadata = MetaData()
session = Session()
Base.metadata.create_all(engine)

d = 'Y:\Обувь\Photo'


def great_all_goods_table():
    with open(r'C:\TrueShop2site\All.csv') as exs:
        reader = csv.DictReader(exs, delimiter=";")
        with Session(engine) as session:
            for i in reader:
                user = AllData(code=i['code'], group_code=i['group_code'], name=(str(i['name'])[:15]), photo=i['photo'],
                               price=i['price'], quantity=i['quantity'], size=i['Размер'])

                session.add(user)
            session.commit()


def add_data_in_table(table_class):
    with Session(engine) as session:
        for i in session.query(AllData).filter(AllData.quantity > 0):
            catalog = table_class(name=i.name, photo="\\".join([d, i.photo]),
                                    price=i.price)
            session.add(catalog)
        session.commit()


def check_table():
    with Session(engine) as session:
        rt = session.query(exists().where(AllData.id.isnot(None))).scalar()
        if rt:
            session.close()
        else:
            great_all_goods_table()
            session.close()





check_table()
add_data_in_table(Catalog)

w = dict()

with Session(engine) as session:
    d = session.query(Catalog.name, Catalog.price, Catalog.photo)
    for i in d:
        g = dict()
        g[i[0]] = i[1], i[2]
        w.update(g)


with Session(engine) as ses:
    for i in w:
        catalog = Catalog(name=i, price=w[i][0], photo=w[i][1])
        ses.add(catalog)
    ses.commit()






