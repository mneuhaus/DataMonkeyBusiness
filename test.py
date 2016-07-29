import quandl
from pandas import DataFrame
from peewee import *
import pandas
import datetime
import shutil
import urllib2
from contextlib import closing

# quandlAuthToken = "xWQ5sNPDYC42JwHzxGkz"
# data = quandl.get("WIKI/data", trim_start = "2000-12-12", authtoken = quandlAuthToken)
# print(data)

db = SqliteDatabase('main.db')

class BaseModel(Model):
    class Meta:
        database = db

class Company(BaseModel):
    name = CharField()
    ticker = CharField(unique=True)
    exchange = CharField()
    industry = CharField()
    sector = CharField()


#class Feature(BaseModel):
#    company = ForeignKeyField(Company, related_name='features')
#    name = CharField()
#    value = CharField()
#    datetime = DateTimeField()
#    #is_positive = BooleanField(default=True)

db.connect()
#db.create_tables([Company, Feature])

russel_3000 = DataFrame.from_csv("Russell_3000_Intraday.txt", sep="\t")
edgar_companies = pandas.read_fwf("edgar-companies.txt")

print(edgar_companies)

#with closing(urllib2.urlopen('ftp://ftp.sec.gov/edgar/data/320193/0001193125-16-439878.txt')) as r:
#    with open('0001193125-16-439878.txt', 'wb') as f:
#        shutil.copyfileobj(r, f)

exit()

for index, row in russel3000.iterrows():
    #print(row, row['Description'])
    #exit()
    company = Company(
        name=row['Description'],
        ticker=row['Symbol'],
        exchange=row['Exchange'],
        industry=row['Industry'],
        sector=row['Sector'])
    company.save()