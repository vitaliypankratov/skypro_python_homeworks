from address import Address
from mailing import Mailing

to_address = Address("123456", "Мск", "Академика Королёва", "11", "111")
from_address = Address("654321", "Париж", "Мбаппе", "10", "20")
mailing = Mailing(to_address, from_address, 600, "track1234")

print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, {mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} "
      f"в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, {mailing.to_address.house} - {mailing.to_address.apartment}. "
      f"Стоимость {mailing.cost} рублей.")