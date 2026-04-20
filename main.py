class FormValidator:
    def __init__(self, data):
        self.data = data

    def validate_name(self):
        if not self.data['name']:
            return False
        if not self.data['name'].isalpha():
            return False
        if len(self.data['name']) < 3:
            return False
        return True

    def validate_email(self):
        if not self.data['email']:
            return False
        if '@' not in self.data['email']:
            return False
        if '.' not in self.data['email']:
            return False
        return True

    def validate_password(self):
        if not self.data['password']:
            return False
        if len(self.data['password']) < 8:
            return False
        if not any(char.isdigit() for char in self.data['password']):
            return False
        if not any(char.isalpha() for char in self.data['password']):
            return False
        return True

    def validate_phone(self):
        if not self.data['phone']:
            return False
        if not self.data['phone'].isdigit():
            return False
        if len(self.data['phone']) != 10:
            return False
        return True

    def validate_form(self):
        if not self.validate_name():
            return 'Name is invalid'
        if not self.validate_email():
            return 'Email is invalid'
        if not self.validate_password():
            return 'Password is invalid'
        if not self.validate_phone():
            return 'Phone is invalid'
        return True

data = {
    'name': 'John Doe',
    'email': 'john@example.com',
    'password': 'password123',
    'phone': '1234567890'
}

validator = FormValidator(data)
print(validator.validate_form())
```

```python
class FormValidator:
    def __init__(self, data):
        self.data = data

    def validate_name(self):
        return self.data.get('name') and self.data['name'].isalpha() and len(self.data['name']) >= 3

    def validate_email(self):
        return self.data.get('email') and '@' in self.data['email'] and '.' in self.data['email']

    def validate_password(self):
        return self.data.get('password') and len(self.data['password']) >= 8 and any(char.isdigit() for char in self.data['password']) and any(char.isalpha() for char in self.data['password'])

    def validate_phone(self):
        return self.data.get('phone') and self.data['phone'].isdigit() and len(self.data['phone']) == 10

    def validate_form(self):
        errors = []
        if not self.validate_name():
            errors.append('Name is invalid')
        if not self.validate_email():
            errors.append('Email is invalid')
        if not self.validate_password():
            errors.append('Password is invalid')
        if not self.validate_phone():
            errors.append('Phone is invalid')
        return errors if errors else True

data = {
    'name': 'John Doe',
    'email': 'john@example.com',
    'password': 'password123',
    'phone': '1234567890'
}

validator = FormValidator(data)
print(validator.validate_form())
