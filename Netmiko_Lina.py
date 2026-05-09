from netmiko import ConnectHandler

# This snippet creates a Python dictionary to store the connection parameters for
# the target network device. This includes the device type, IP address (host),
# and the credentials for authentication.
#snippet part 1 ################
# Authentication using username/password
device = {
    'device_type': 'cisco_ios',
    'host': '10.88.15.3',
    'username': 'admin',
    'password': 'cisco!123'
}
################################

# This snippet uses the ConnectHandler class from the Netmiko library to establish
# an SSH connection to the device. The `**device` syntax unpacks the dictionary
# of parameters we defined above into the function call.
#snippet part 2 ################
connection = ConnectHandler(**device)
################################

# Once the connection is active, this snippet uses the `send_command()` method
# to execute a command on the remote device. It sends 'show version', waits for
# the output, and stores the response in the `output` variable.
#snippet part 3 ################
output = connection.send_command('show version')
print( "Output:", output)
################################

# This final snippet demonstrates the best practice of gracefully closing the
# connection. The `disconnect()` method terminates the SSH session with the
# network device.
#snippet part 4 ################
connection.disconnect()
################################
