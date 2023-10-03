import sqlalchemy as db


engine = db.create_engine('sqlite:///data_all.db')
connection = engine.connect()
metadata = db.MetaData()

product = db.Table('all', metadata,
                   db.Column('id', db.Integer, primary_key=True),
                   db.Column('code', db.Integer),
                   db.Column('name', db.String),
                   db.Column('photo', db.String),
                   db.Column('price', db.Integer),
                   db.Column('quantity', db.Integer),
                   db.Column('size', db.Integer)
                   )

metadata.create_all(engine)
