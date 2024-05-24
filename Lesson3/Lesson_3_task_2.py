from smartphone import Smartphone

catalog = []

phone1 = Smartphone('apple', 'iphone 3', '+79101777953')
phone2 = Smartphone('nokia', '3310', '+79101777955')
phone3 = Smartphone('sumsang', 'glaxay duo', '+79101777956')
phone4 = Smartphone('rusphone', 'pro13', '+79101777957')
phone5 = Smartphone('fly', 'note16', '+79101777888')

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog:
    print(f'{phone.brand} - {phone.model}. {phone.phone_number}')