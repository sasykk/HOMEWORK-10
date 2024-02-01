from collections import UserDict


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
        return False


class Record:

    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, value):
        phone = Phone(value)
        self.phones.append(phone)

    def remove_phone(self, phone):
        self.phones = [ph for ph in self.phones if ph.value != phone]

    def edit_phone(self, phone, new_phone):
        for ph in self.phones:
            if ph.value == phone:
                if ph.is_valid(new_phone):
                    ph.value = new_phone
                    break
                else:
                    raise ValueError("Invalid phone number")
        else:
            raise ValueError("Phone not found in record")

    def find_phone(self, phone):
        for ph in self.phones:
            if ph.value == phone:
                return ph
        return None

    def __str__(self):
        return f"Name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name, None)

    def delete(self, name):
        if name not in self.data:
            return None

        self.data.pop(name)
