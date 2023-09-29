import re
pattern = r"World"
text = "Hello, World!"
search_result = re.search(pattern, text)
if search_result:
    print("Pattern found:", search_result.group())
else:
    print("Pattern not found")
