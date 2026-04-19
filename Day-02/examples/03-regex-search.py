import re

text = "The quick brown fox"
pattern = r"brown"

search = re.search(pattern, text)
if search:
    print("Pattern found:", search.group())
else:
    print("Pattern not found")

##Explanation of the code:
##1. We import the `re` module, which provides support for regular expressions in Python
##2. We define a text string and a pattern to search for.
##3. We use `re.search()` to search for the pattern anywhere in the text.
##4. If a match is found, we print it; otherwise, we print a message indicating that the pattern was not found.
