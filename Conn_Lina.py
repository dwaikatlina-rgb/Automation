from netmiko import ConnectHandler

# Define the connection parameters for the target network device.
# Replace placeholders with your specific environment details.
device = {
    'device_type': 'cisco_ios',
    'host': '10.88.15.3',
    'username': 'admin',
    'password': 'your_password_here'
}

# Establish the SSH connection to the device using Netmiko.
try:
    connection = ConnectHandler(**device)
    print(f"Successfully connected to {device['host']}")

    # Execute the command to view interface status.
    # 'show ip interface brief' provides a summary of all interfaces.
    command = 'show ip interface brief'
    output = connection.send_command(command)
    
    print("-" * 30)
    print(f"Output for '{command}':")
    print(output)
    print("-" * 30)

    # Gracefully close the connection.
    connection.disconnect()
    print("Connection closed.")

except Exception as e:
    print(f"An error occurred: {e}")
    
