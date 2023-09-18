from mimesis import Generic
from mimesis.locales import Locale
from mimesis import Person
from mimesis.enums import Gender
from mimesis import Text

text = Text('en')
print(text.text(quantity=5))

# for i in range(3):
#     person.name()



# def generate_email():
#     for i in range(10):
#         p = person.email()
#         print(p)

# generate_email()