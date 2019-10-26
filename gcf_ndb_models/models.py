from google.cloud import ndb


class Contact(ndb.Model):
    name = ndb.StringProperty()
    phone = ndb.StringProperty()
    email = ndb.StringProperty()

    @classmethod
    def get_by_name(cls, name='Model'):
        return cls.query(name == name).get()

    @classmethod
    def create_or_update(cls, data):
        if data.get('id'):
            contact = cls.get_by_id(int(data.get('id')))
        else:
            contact = cls()

        contact.name = data.get('name')
        contact.phone = data.get('phone')
        contact.email = data.get('email')

        return contact
