import re

text = "The quick brown fox jumps over the lazy brown dog"
pattern = r"brown"

replacement = "red"

new_text = re.sub(pattern, replacement, text)
print("Modified text:", new_text)

##Explanation of the code:
##1. We import the `re` module, which provides support for regular expressions in Python.
##2. We define a text string, a pattern to search for, and a replacement string.
##3. We use `re.sub()` to replace all occurrences of the pattern in the text with the replacement string.
##4. Finally, we print the modified text.   