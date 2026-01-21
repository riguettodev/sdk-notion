import json
from ..QueryFilter import QueryFilter

filter1 = QueryFilter.and_(
    QueryFilter.title("Name", "contains", "Teste"),
    QueryFilter.or_(
        QueryFilter.number("Value", "greater_than", 10),
        QueryFilter.number("Value", "less_than", 5)
    )
)

print(json.dumps({"filter":filter1.to_dict()}))