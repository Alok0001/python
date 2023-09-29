import re
pattern = r"Hello"
text = "Hello, World!"
match = re.match(pattern, text)
if match:
    print("Pattern found:", match.group())
else:
    print("Pattern not found")
