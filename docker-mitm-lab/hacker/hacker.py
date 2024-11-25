from flask import Flask, request, Response
import requests
import re

app = Flask(__name__)

SERVER_URL = "http://server:5000/data"  # Address of the server in Docker network

# Patterns for sensitive information
patterns = {
    'Name': r'Name: \S+ \S+',
    'Phone': r'Phone: \+\d{12}',
    'Card': r'Card: \d{4}-\d{4}-\d{4}-\d{4}',
    'PIN': r'PIN: \d{4}',
    'Balance': r'Balance: \d+\.\d{2}\$',
}

@app.route('/data', methods=['GET'])
def intercept_data():
    # Send the request to the server to get the original file
    response = requests.get(SERVER_URL)

    # Read the original content
    original_content = response.text

    # Replace sensitive information using regular expressions
    modified_content = re.sub(patterns['Name'], 'Name: Fake Name', original_content)
    modified_content = re.sub(patterns['Phone'], 'Phone: +000000000000', modified_content)
    modified_content = re.sub(patterns['Card'], 'Card: 0000-0000-0000-0000', modified_content)
    modified_content = re.sub(patterns['PIN'], 'PIN: 0000', modified_content)
    modified_content = re.sub(patterns['Balance'], 'Balance: 0.00$', modified_content)

    # Optionally, you could save this modified content to a new file inside the container
    with open("/app/secret_modified.txt", "w") as f:
        f.write(modified_content)
    
    # Return the modified content as a response
    return Response(modified_content, mimetype='text/plain', headers={"Content-Disposition": "attachment; filename=secret_modified.txt"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)  # Hacker listens on port 5001
