from address import Address
from mailing import Mailing


from_address = Address("173009", "Великий Новгород", "Озёрная", 14, 62)
to_address = Address("175400", "Валдай", "Лесная", 10, 24)
cost = 1000
track = 123456


mailing = Mailing(from_address,to_address, cost, track)

print(mailing)