import re

text = "The quick brown fox"
pattern = r"The quick brown fox"

match = re.match(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match")


##Explanation of the code:
##1. We import the `re` module, which provides support for regular expressions in Python
##2. We define a text string and a pattern to search for.
##3. We use `re.match()` to check if the pattern matches the beginning of the text.
##4. If a match is found, we print it; otherwise, we print a message indicating that no match was found.