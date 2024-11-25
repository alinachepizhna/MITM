from flask import Flask, send_file

app = Flask(__name__)

@app.route('/data', methods=['GET'])
def send_secret_file():
    # Path to the secret.txt file in the server
    return send_file('/app/secret.txt', as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Server listens on port 5000
