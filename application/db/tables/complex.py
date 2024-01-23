# from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table
#
# engine = create_engine(os.getenv("SQLALCHEMY_URL"), echo=True)
#
# metadata = MetaData()
#
# users_table = Table(
#     'users',
#     metadata,
#     Column('id', Integer, primary_key=True),
#     Column('username', String, nullable=True),
#     Column('email', String, nullable=True)
# )
#
# metadata.create_all(engine)
