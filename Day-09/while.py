#while loop in Python is used to execute a block of code repeatedly as long as a given condition is true. The syntax of a while loop is:
# while condition:
    # Code to be executed as long as the condition is true


# Example:
i = 0   
while i < 5:
    print(i)
    i += 1


# Another example:
# Example: while loop to check the status of an EC2 instance
import time
import random
instance_status = "pending"
while instance_status != "running":
    print("Checking instance status...")
    time.sleep(2)  # Simulate waiting for the instance to start
    instance_status = random.choice(["pending", "running"])  # Randomly change status for demonstration 
print("Instance is now running!") 

#Another simple example:
counter = 0
while counter < 3:
    print("Counter:", counter)
    counter += 1
print("Loop finished")