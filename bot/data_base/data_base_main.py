import sqlalchemy as db
import sqlite3

engine = db.create_engine('sqlite:///data_all.db')
conn = engine.connect()
metadata = db.MetaData()

data_all = db.Table('data_all', metadata,
                    db.Column('id', db.Integer, primary_key=True),
                    db.Column('code', db.Integer),
                    db.Column('name', db.Text),
                    db.Column('photo', db.Text),
                    db.Column('price', db.Integer),
                    db.Column('quantity', db.Integer),
                    db.Column('size', db.Integer)
                    )

metadata.create_all(engine)
insertion_query = data_all.insert().values([{'code': 546464, 'name': 'gfdgdfg', 'photo': 'dghdh',
                                             'price': 5465, 'quantity': 45346767, 'size': 346546}])

conn.execute(insertion_query)
select_all_query = db.select([data_all])
select_all_result = conn.execute(select_all_query)
print(select_all_result.all())
