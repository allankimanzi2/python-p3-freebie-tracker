from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Company(Base):
    __tablename__ = 'companies'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    founding_year = Column(Integer)
    freebies = relationship('Freebie', backref='company')

class Dev(Base):
    __tablename__ = 'devs'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    freebies = relationship('Freebie', backref='dev')

class Freebie(Base):
    __tablename__ = 'freebies'
    id = Column(Integer, primary_key=True)
    item_name = Column(String)
    value = Column(Integer)
    dev_id = Column(Integer, ForeignKey('devs.id'))
    company_id = Column(Integer, ForeignKey('companies.id'))

    def print_details(self):
        return f"{self.dev.name} owns a {self.item_name} from {self.company.name}"
