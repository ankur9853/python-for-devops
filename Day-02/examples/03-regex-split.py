import re

text = "apple,banana,orange,grape"
pattern = r","

split_result = re.split(pattern, text)
print("Split result:", split_result)


##Explanation of the code:
##1. We import the `re` module, which provides support for regular expressions in Python.
##2. We define a text string that contains items separated by commas and a pattern to split the string (in this case, a comma).
##3. We use `re.split()` to split the text based on the specified pattern.      
##4. Finally, we print the result of the split operation, which is a list of the individual items.