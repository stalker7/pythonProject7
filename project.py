from decimal import Decimal
from yandex_geocoder import Client


client = Client("your-api-key")

coordinates = client.coordinates("Москва Льва Толстого 16")
assert coordinates == (Decimal("37.587093"), Decimal("55.733969"))

address = client.address(Decimal("37.587093"), Decimal("55.733969"))
assert address == "Россия, Москва, улица Льва Толстого, 16"



