import re
# compling of pattern
pattern = re.compile(r"\d{3}-\d{2}-\d{4}")
text = "My SSN is 123-45-6789"
match = pattern.search(text)
if match:
    print("SSN found:", match.group())
else:
    print("SSN not found")

# matching and grouping
pattern = r"(\d{3})-(\d{2})-(\d{4})"
text = "My SSN is 123-45-6789"
match = re.search(pattern, text)
if match:
    print("SSN found:", match.group())
    print("Group 1:", match.group(1))
    print("Group 2:", match.group(2))
    print("Group 3:", match.group(3))
else:
    print("SSN not found")

# Replacing
pattern = r"apple"
text = "I like apple pie and applesauce."
new_text = re.sub(pattern, "banana", text)
print(new_text)

# Remove

text = "I have $100 and €50, but no ¥."
pattern = r"[$€¥]"  # This pattern matches any of the specified currency symbols

# Replace matched patterns with an empty string to remove them
cleaned_text = re.sub(pattern, "", text)

print("Original text:", text)
print("Cleaned text:", cleaned_text)

