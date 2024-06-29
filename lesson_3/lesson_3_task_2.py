from smartphone import Smartphone

catalog = []
phone1 = Smartphone("Apple", "iPhone 3", "+79040301123")
phone2 = Smartphone("Sumsang", "Glaxay DUO", "+79203456789")
phone3 = Smartphone("RUSphone", "1", "+79204445561")
phone4 = Smartphone("Fly", "Note 10 Pro", "+79005527200")
phone5 = Smartphone("Nokia", "3310", "+79000000001")

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog:
    print(f"{phone.brand}' - {phone.model}, {phone.phone_number}")