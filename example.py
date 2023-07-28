import Fertok
from flask import Flask, jsonify, request,send_file # type: ignore

#Using Flask we will create a simple API that will return the username of the user that is logged in. log us in with a token or even authenticate any action

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    token = request.headers.get('token')
    if Fertok.authenticate(token):
        username = Fertok.extractUsernameFromToken(token)
        return jsonify({'username': username}), 200
    else:
        return jsonify({'message': 'Invalid token'}), 401
    
@app.route('/TakeAction', methods=['POST'])
def TakeAction():
    token = request.headers.get('token')
    if Fertok.authenticate(token):
        #Do something
        return jsonify({'message': 'Action taken'}), 200
    else:
        return jsonify({'message': 'Invalid token'}), 401
    
@app.route('/getUsername', methods=['GET'])
def getUsername():
    token = request.headers.get('token')
    if Fertok.authenticate(token):
        username = Fertok.extractUsernameFromToken(token)
        return jsonify({'username': username}), 200
    else:
        return jsonify({'message': 'Invalid token'}), 401
    
@app.route('/getEncryptedInfo', methods=['GET'])
def getEncryptedInfo():
    token = request.headers.get('token')
    if Fertok.authenticate(token):
        encryptedInfo = Fertok.extractTokenEncryptedInfo(token)
        return jsonify({'encryptedInfo': encryptedInfo}), 200
    else:
        return jsonify({'message': 'Invalid token'}), 401

if __name__ == '__main__':
    app.run(debug=True)