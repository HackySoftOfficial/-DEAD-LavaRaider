import requests
import json

# Replace with the actual URL of your Flask application
WORKER_URL = 'http://lavapi.hackysoft.xyz:8000/key'  # Change to the correct URL if deployed

# Data and headers to send with the request
data = {'key': "' OR '1'='1", 'hwid': 'D47FD1ED-90D4-0F41-DDF5-0492265C927F'}  # The license key or request body you want to check
headers = {
    'Content-Type': 'application/json',  # Set Content-Type to application/json
    'User-Agent': 'LavaRaider',
    'LavaVersion': '1.0'  # Replace with actual LavaVersion if needed
}

try:
    # Send POST request to the server
    response = requests.post(WORKER_URL, data=json.dumps(data), headers=headers)

    # Print the response details
    print('Status Code:', response.status_code)
    print('Response Text:', response.text)
except requests.exceptions.RequestException as e:
    print(f'An error occurred: {e}')
