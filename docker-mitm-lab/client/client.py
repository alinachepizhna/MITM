import requests

HACKER_URL = "http://hacker:5001/data"  # Address of the hacker in Docker network

# Send a request to the hacker to get the modified file
response = requests.get(HACKER_URL)

# Save the modified file
with open('secret_modified.txt', 'wb') as f:
    f.write(response.content)

print("File downloaded successfully!")

# Print the contents of the downloaded file
with open('secret_modified.txt', 'r') as f:
    print("Modified file content:")
    print(f.read())
