import re

text = "Hi @mr_alex ! My name is John and I love coffee. #coffeelover #2021"

print(re.sub(r"[.!?\\-]", '', text))
print([e for e in re.finditer(r"#[A-Za-z0-9]*", text)])
print(re.split(r"[.!?\\-]", text))
