from collections import UserDict

class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        record = None if name not in self.data else self.data[name]
        return record

    def delete(self, name):
        if name not in self.data:
            return None
        self.data.pop(name)

class Record:

    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, value):
        phone = Phone(value)
        self.phones.append(phone)

    def remove_phone(self, phone):
        for idx, ph in enumerate(self.phones):
            if ph.value == phone:
                self.phones.pop(idx)

    def change_phone(self, phone, new_phone):
        for idx, ph in enumerate(self.phones):
            if ph.value == phone:
                if ph.is_valid(new_phone):
                    self.phones[idx].value = new_phone
                    break
        else:
            raise ValueError("Phone not found")

    def find_phone(self, phone):
        for ph in self.phones:
            if ph.value == phone:
                return ph
        return None

    def __str__(self):
        return f"Contact: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class Field:

    def __init__(self, value):
        if self.is_valid(value):
            self.value = value
        else:
            raise ValueError

    def is_valid(self, _):
        return True

    def __str__(self):
        return str(self.value)

class Name(Field):

    pass

class Phone(Field):

    def is_valid(self, value):
        if value.isdigit() and len(value) == 10:
            return True
