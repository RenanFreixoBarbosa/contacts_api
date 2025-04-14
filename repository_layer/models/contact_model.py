from .base import Base
from sqlalchemy import Column, String, Integer

class Contact(Base):
    __tablename__ = 'contacts'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    phone = Column(String(20), nullable=False)
    address = Column(String(100), nullable=False)

    def __init__(self, name, phone, address):
        self.name = name
        self.phone = phone
        self.address = address

    def to_dict(self):
        return {
            "id":self.id,
            "name":self.name,
            "phone":self.phone,
            "address":self.address
        }