from repository_layer.models.contact_model import Contact
from repository_layer.models.base import Session
from sqlalchemy.exc import IntegrityError

class ContactRepository():
    def __init__(self):
       self.session = Session()

    def list_contacts(self):
        try:
            contacts = self.session.query(Contact).all()
            contact_list = [
            {
                "id": contact.id,
                "nome": contact.name,
                "telefone": contact.phone,
                "email":contact.address
            }
            for contact in contacts
        ]
            return contact_list
        except Exception as e:
            raise e
        finally:
            self.session.close()
    
    def create_contact(self,name: str, phone: str, address: str):
        contact = Contact(name, phone, address)

        try:
            self.session.add(contact)
            self.session.commit()
            return contact.to_dict()
        except IntegrityError:
            self.session.rollback()
            raise ValueError("Este número ou email já existe.")
        except Exception as e:
            self.session.rollback()
            raise e
        finally:
            self.session.close()

    def update_contact(self,contact_id: int, name: str, phone: str, address: str):
        try:
            contato = self.session.query(Contact).filter(Contact.id == contact_id).first()
            print(contato.name)
            if not contato:
                return None

            contato.name = name
            contato.phone = phone
            contato.address = address

            self.session.commit()
            return contato.to_dict()
        except Exception as e:
            self.session.rollback()
            raise e
        finally:
            self.session.close()
    
    def delete_contact(self,contact_id:int):
        try:
            contato = self.session.query(Contact).filter(Contact.id == contact_id).first()
            if not contato:
               return False

            self.session.delete(contato)
            self.session.commit()
            return True
        except Exception as e:
            self.session.rollback()
            raise e
        finally:
            self.session.close()

