import sqlalchemy as db
import csv

engine = db.create_engine('sqlite:///data_all.db')
conn = engine.connect()
metadata = db.MetaData()

data_al = db.Table('data_al', metadata,
                   db.Column('id', db.Integer, primary_key=True),
                   db.Column('code', db.Integer),
                   db.Column('name', db.String),
                   db.Column('photo', db.String),
                   db.Column('price', db.Integer),
                   db.Column('quantity', db.Integer),
                   db.Column('size', db.Integer)
                   )

metadata.create_all(engine)

with open(r'C:\TrueShop2site\All.csv') as exs:
    reader = csv.DictReader(exs, delimiter=";")

    for i in reader:
        insertion_query = data_al.insert().values([{'code': i['code'], 'name': i['name'], 'photo': i['photo'],
                                                    'price': i['price'], 'quantity': i['quantity'],
                                                    'size': i['Размер']}])

        conn.execute(insertion_query)
        select_all_query = db.select(data_al)
        select_all_result = conn.execute(select_all_query)
    conn.commit()
