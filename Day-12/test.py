def update_server_config(file_path, key, value):
    # Read the existing content of the server configuration file
    with open(file_path, "r") as file:
        lines = file.readlines()
    
    # Update the configuration value for the specified key
    with open(file_path, "w") as file:
        for i in lines:
            # Check if the line starts with the specified key
            if key in i:
                # Update the line with new value
                file.write(key + "=" + value + "\n")
            else:
                # keep the existig line as it is
                file.write(i)

# Path to the server configuration file
file_path = "server.conf"

# Key and new value for updating the server configuration
key = "MAX_CONNECTIONS"
new_value = "6000"

# Update the server configuration file  
update_server_config(file_path, key, new_value)