##### Part of Template ############
from netmiko import ConnectHandler

device = {
    'device_type': 'cisco_ios',
    'host': '10.88.15.3',
    'username': 'admin',
    'password': 'cisco!123'
}

connection = ConnectHandler(**device)
command = "show interfaces"
# Added expect_string to prevent the timeout you saw earlier
output = connection.send_command(command, expect_string=r'C8300-2#')

###############################################

alllines = output.splitlines()
print(f"Number of lines in outputs = {len(alllines)}")

# Initialize variables to prevent NameErrors
tx_packets = "0"

for line in alllines:
    # 1. Check if the line is an Interface Header (does NOT start with a space)
    if not line.startswith(" "):
        if line.strip() != "":
            print(f"Interface Details = {line}")
            continue
            
    # 2. Process indented lines (starts with a space)
    else:
        line_clean = line.strip()
        
        # Look for IPv6 Address
        if line_clean.startswith("IPv6 address"):
            print(f"    IPV6 - {line_clean}")
            
        # Look for MAC Address (Cisco format: "Hardware is ..., address is 000c.298b.770a")
        elif "address is" in line_clean:
            parts = line_clean.split("address is ")
            mac_address = parts[1].split()[0] # Get the MAC and ignore the rest of the line
            print(f"    MAC Address - {mac_address.upper()}")
        
        # Look for Input Stats (RX)
        elif "packets input" in line_clean:
            parts = line_clean.split()
            rx_packets = parts[0] # Cisco: "0 packets input"
            rx_bytes = parts[3]   # Cisco: "... input, 0 bytes, ..."
            print(f"    RX stats - Packets: {rx_packets}, Bytes: {rx_bytes}")
        
        # Look for Output Stats (TX)
        elif "packets output" in line_clean:
            parts = line_clean.split()
            tx_packets = parts[0] # Cisco: "0 packets output"
            tx_bytes = parts[3]   # Cisco: "... output, 0 bytes, ..."
            
            print(f"    TX stats - Packets: {tx_packets}, Bytes: {tx_bytes}")
            
            # --- Assignment Requirements: find() and isdigit() ---
            print(f"    Index of the word 'bytes' in this line = {line_clean.find('bytes')}")
            print(f"    Index of 'NoSuchString' = {line_clean.find('NoSuchString')}")
            print(f"    Are all TX packet characters digits? {tx_packets.isdigit()}")