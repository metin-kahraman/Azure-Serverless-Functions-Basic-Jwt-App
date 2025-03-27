import logging
import azure.functions as func
import jwt
import datetime
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('User registration request received.')

    try:
        req_body = req.get_json()
    except ValueError:
        return func.HttpResponse("Send data in JSON format.", status_code=400)

    username = req_body.get('username')
    password = req_body.get('password')

    if not username or not password:
        return func.HttpResponse("Username and password required.JSON Keys (username,password)", status_code=400)

    # Perform the operation to save the user to the database or other storage here.Space start
    #
    #
    #
    # Perform the operation to save the user to the database or other storage here.Space end

    # Create JWT Key
    payload = {
        'username': username,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7) # 7 days validity period
    }
    secret_key = 'my_s_key'  # The secret key for JWT (Used in GetUserInfo Line : 16 ) 
    encoded_jwt = jwt.encode(payload, secret_key, algorithm='HS256')

    return func.HttpResponse(json.dumps({'token': encoded_jwt}), mimetype="application/json")