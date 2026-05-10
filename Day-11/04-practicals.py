# Server configurations dictionary
server_config = {
    'server1': {'ip': '192.168.1.1', 'port': 8080, 'status': 'active'},
    'server2': {'ip': '192.168.1.2', 'port': 8000, 'status': 'inactive'},
    'server3': {'ip': '192.168.1.3', 'port': 9000, 'status': 'active'}
}

# Retrieving information
def get_server_status(server_name):
    # Breaking this down makes it easier to set breakpoints and inspect intermediate values
    config = server_config.get(server_name)
    if not config:
        return 'Server not found'
    return config.get('status', 'Status unknown')

# Example usage
server_name = 'server3'
status = get_server_status(server_name)
print(f"{server_name} status: {status}")