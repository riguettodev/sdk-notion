import json
from ..QuerySort import QuerySort

sort1 = QuerySort.ascending("Teste")

print(json.dumps({"sorts":sort1.to_dict()}))

sort2 = QuerySort.and_(
    QuerySort.ascending("Teste")
)

print(json.dumps({"sorts":sort2.to_dict()}))