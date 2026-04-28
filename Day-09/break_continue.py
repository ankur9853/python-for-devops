#break and continue and pass statements in Python

# break statement is used to exit a loop prematurely when a certain condition is met. When the break statement is executed, 
# the loop is immediately terminated, and the program continues with the next statement after the loop.
for i in range(10):
    if i == 5:
        break
    print(i)

# continue statement is used to skip the current iteration of a loop and move on to the next iteration. 
# When the continue statement is executed, the rest of the code inside the loop for that iteration is skipped, 
# and the loop proceeds with the next iteration.
for i in range(10):
    if i == 5:
        continue
    print(i)


# The pass statement is a null operation; it does nothing when executed. 
# It is used as a placeholder in situations where a statement is syntactically required but no action is needed or desired. 
# For example, it can be used in loops, functions, or classes that are not yet implemented.
for i in range(10):
    if i == 5:
        pass
    print(i)    