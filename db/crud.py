from sqlalchemy import create_engine
import sqlalchemy
import pandas

# from __main__ import df_places

url = "postgres://fqkycpttcymxzy:14eda175d6e47f63b26b5902de2738b0a5498a4dbb217e29ee30be6f0e33bba8@ec2-54-170-123-247.eu-west-1.compute.amazonaws.com:5432/d7tvo5scif1ebn"
engine = create_engine(url)
con = engine.connect()
print(engine.table_names())

metadata = sqlalchemy.MetaData()
# census = Table('firm_creation', metadata, autoload=True, autoload_with=engine)

# print(repr(census))

# df_places.to_sql('test2', con=engine, if_exists='append')
# engine.execute("SELECT * FROM test").fetchall()
