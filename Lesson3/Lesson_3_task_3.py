from address import Address
from mailing import Mailing

to_address = Address("600028", "Paris", "Lenina", "18", "1000")
from_address = Address("500014", "Serpuhov", "Kirova", "12", "77")                      
mailing = Mailing(to_address, from_address, 100, "track1234")

print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city},"
      f" {mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} "
      f" в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, "
      f" {mailing.to_address.house} - {mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")