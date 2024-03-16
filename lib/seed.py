from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Dev, Company, Freebie, Base


engine = create_engine('sqlite:///your_database_name.db')  


Session = sessionmaker(bind=engine)
session = Session()


dev1 = Dev(name='Developer 1')
dev2 = Dev(name='Developer 2')


company1 = Company(name='Company 1', founding_year=2000)
company2 = Company(name='Company 2', founding_year=2010)


freebie1 = Freebie(item_name='Laptop', value=1000, dev=dev1, company=company1)
freebie2 = Freebie(item_name='T-shirt', value=20, dev=dev1, company=company2)
freebie3 = Freebie(item_name='Mouse', value=50, dev=dev2, company=company1)


session.add_all([dev1, dev2, company1, company2, freebie1, freebie2, freebie3])
session.commit()
