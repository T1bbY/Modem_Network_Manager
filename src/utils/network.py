import subprocess
import re

def send_at_command(command):
    result = subprocess.run(['minicom', '-D', '/dev/ttyUSB2', '-b', '115200', '-C', 'output.txt', '-S', 'at-command'], input=command, text=True)
    with open('output.txt', 'r') as file:
        output = file.read()
    return output

def get_available_networks():
    output = send_at_command('AT+COPS=?')
    networks = parse_networks(output)
    return networks

def parse_networks(output):
    networks = []
    for line in output.splitlines():
        match = re.search(r'\((\d+),(\d+),"([^"]+)",(\d+)\)', line)
        if match:
            networks.append({
                'status': int(match.group(1)),
                'act': int(match.group(2)),
                'name': match.group(3),
                'signal_strength': get_signal_strength(match.group(3))
            })
    return networks

def get_signal_strength(network_name):
    output = send_at_command('AT+CSQ')
    match = re.search(r'\+CSQ: (\d+),(\d+)', output)
    return int(match.group(1)) if match else 0

def switch_to_network(network_name):
    send_at_command(f'AT+COPS=1,0,"{network_name}"')
