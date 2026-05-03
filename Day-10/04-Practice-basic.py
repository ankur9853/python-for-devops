###########TASK1############

def main():

    server_list = ["Server1", "Server2", "Server3", "Server4", "Server5"]
    print("Server list:", server_list)

    server_list.append("Server6")
    print("Server list after appending:", server_list)

    try:
        server_list.remove("Server7")
        print("Server list after removing:", server_list)   
    except ValueError: # this will give an error because "Server7" is not in the list
        print("Server7 not found in the list")

if __name__ == "__main__":
    main()


###########TASK2############

#Task 2: Create a list of IP addresses. Write a function that:

#Checks if an IP exists in the list
#Raises a custom exception if IP is invalid (doesn't have 4 parts)
                                            

class InvalidIPError(Exception):
    pass
    
def check_ip(ip_list, ip):
    if ip in ip_list:
        print(f"{ip} exists in the list.") # this will print if the IP exists in the list. f is used for string formatting to include the value of ip in the output message.
    else:
        print(f"{ip} does not exist in the list.")
    
    if len(ip.split('.')) != 4: # this will check if the IP address has 4 parts separated by dots. If not, it will raise an InvalidIPError. 
        raise InvalidIPError(f"{ip} is an invalid IP address.")

ip_addresses = ["192.168.1.1", "10.0.0.1", "172.16.0.1", "192.168.1.2",]

check_ip(ip_addresses, "192.168.1.1")
check_ip(ip_addresses, "10.0.0.2")
check_ip(ip_addresses, "172.16.0.1")
check_ip(ip_addresses, "192.168.1.2")
check_ip(ip_addresses, "10.0.0.1")
check_ip(ip_addresses, "172.16.0.2")

