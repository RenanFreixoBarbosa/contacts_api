from pydantic import BaseModel
from typing import List
from repository_layer.models.contact_model import Contact

#created a contact
class ContactSchema(BaseModel):
    name: str 
    phone: str
    address: str 

# Update a contact
class ContactViewSchema(BaseModel):
    contact_id: int
    name: str
    phone: str
    address: str

# Lista de contatos
class ListContactSchema(BaseModel):
    contacts: List[ContactViewSchema]

# Retorno de exclusão
class ContactDelSchema(BaseModel):
    contact_id:int

# Erro genérico
class ErrorSchema(BaseModel):
    message: str = "Mensagem de erro"


def get_contact(contato: Contact):
    return {
        "id": contato.id,
        "name": contato.name,
        "phone": contato.phone,
        "address": contato.address
    }

def get_contacts(contatos: List[Contact]):
    return {"contacts": [get_contact (c) for c in contatos]}