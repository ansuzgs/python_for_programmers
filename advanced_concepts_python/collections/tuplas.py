from collections import namedtuple

Parts = namedtuple("Parts", "id_num desc cost amount")
auto_parts = Parts(id_num="1234", desc="Ford engine", cost=1200.00, amount=10)
print(auto_parts)

Parts = {"id_num": "1234", "desc": "Ford Engine", "cost": 1200.00, "amount": 10}
parts = namedtuple('Parts', Parts.keys())(**Parts)
print(parts)