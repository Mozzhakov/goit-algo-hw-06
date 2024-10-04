from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
         if not value or len(value) < 2:
             raise ValueError('Name is required and must contain more than 2 symbols')
         super().__init__(value)
    
class Phone(Field):
    def __init__(self, value):
         if not value.isdigit() or len(value) != 10:
              raise ValueError('Phone number should contain 10 digits')
         super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, number):
        self.phones.append(Phone(number))

    def delete_phone(self, number):
        self.phones = [phone for phone in self.phones if phone.value != number]

    def find_phone(self, number):
        for phone in self.phones:
            if number == phone.value:
                return phone
        return None
    
    def edit_phone(self, old_number, new_number):
        phone = self.find_phone(old_number)
        if phone:
            try:
                new_phone = Phone(new_number)
            except ValueError as e: 
                raise ValueError(f'Invalid phone number: {e}')
            self.delete_phone(old_number)
            self.phones.append(new_phone)
        else:
            raise ValueError('Phone number not found')

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record
    
    def find(self, name):
        return self.data.get(name, None)

    def delete(self, name):
        if name in self.data:
            del self.data[name]
        else:
            raise ValueError('Contact not found')
    
    def __str__(self):
        return f'Your contacts:\n{'\n'.join(str(record) for record in self.data.values())}'
        

# book = AddressBook()
# john = Record('John')
# john.add_phone('1234567890')
# book.add_record(john)
# john.edit_phone('1234567890', '1111111111')
# john.add_phone('0987654321')
# mark = Record("Mark")
# mark.add_phone('1112223334') 
# print(mark.find_phone('1112223334'))
# mark.edit_phone('1112223334', '1231231231')
# book.add_record(mark)
# print(book.find('Mark'))
# print(book)