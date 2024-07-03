value_str = "hello"
result = None if not value_str else value_str
print(result)
another_way = value_str if value_str else None
print(another_way)
