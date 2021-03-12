import psycopg2
import pandas as pd
from sqlalchemy import create_engine, MetaData, Table, Integer, String, Column, Text, DateTime, ForeignKey, Numeric, Float, \
    Date, and_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.orm import relationship
import random
from datetime import datetime
# pour postgres


logf = open("download.log", "w")

engine = create_engine(
    'postgresql+psycopg2://Cakuva:Collectif33PierreThibaultClementSimplon@cakuva-bodacc.c9yrikhahmsh.eu-west-3.rds.amazonaws.com/postgres')

# Pour sqlite3:
# engine = create_engine('sqlite:///sqlite3.db')  # using relative path and sqlit3

# When using SQLAlchemy ORM, we interact with the database using the Session object.
# The Session object also wraps the database connection and transaction.
# The transaction implicitly starts as soon as the Session starts communicating with the database
# and will remain open until the Session is committed, rolled back or closed.

Session = sessionmaker(bind=engine)

# then connect the engine

engine.connect()

Base = declarative_base()


# Defining Models
# A Model is a Python class which corresponds to the
# database table and its attributes represent the columns.
# see Defining Relationships @ https://overiq.com/sqlalchemy-101/defining-schema-in-sqlalchemy-orm/




class Entreprise(Base):
    __tablename__ = 'entreprises'
    siren = Column(String(100), primary_key=True)
    juridic_form = Column(String(300),nullable=False)
    company_activity = Column(Text, nullable=False)
    insee_activity = Column(Text, nullable=False)
    ape = Column(String(100), nullable=False)
    code_postal = Column(String(100))
    imatriculation_date = Column(Date)



# On exécute cette methode, pour créer les tables dans la DB
def create_tables():
    Base.metadata.create_all(engine)


# Pour supprimer toute les tables
def drop_tables():
    Base.metadata.drop_all(engine)


def add_entreprise(data):

    session = Session()
    compteur = 0
    for entreprise in data:

        try:

            company = Entreprise(siren=entreprise['siren'],
            juridic_form=entreprise['forme_juridique'],
            company_activity=entreprise['activite'],
            insee_activity=entreprise['activite_insee'],
            ape=entreprise['code_ape'],
            code_postal=entreprise['code_postal'],
            imatriculation_date=entreprise['date_immat'])


            print(f'line {compteur} added to session')
            compteur += 1

            session.add(company)
            session.commit()
        # code to process download here
        except Exception as e:  # most generic exception you can catch
            logf.write("Failed to insert in DB {0}: {1}\n".format(str(entreprise), str(e)))
        # optional: delete local version of failed download

    print('the session has been commited, and datas saved in DB ')

 # CRUD

# Create
