import logging
import azure.functions as func
import jwt
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('JWT key query request received.')

    token_header = req.headers.get('Authorization')
    if not token_header or 'Bearer ' not in token_header:
        return func.HttpResponse("JWT key is required.", status_code=401)

    token = token_header.split('Bearer ')[1]

    try:
        secret_key = 'my_s_key'  # The secret key for JWT
        decoded_jwt = jwt.decode(token, secret_key, algorithms=['HS256'])
        username = decoded_jwt['username']
        return func.HttpResponse(json.dumps({'username': username}), mimetype="application/json")
    except jwt.ExpiredSignatureError:
        return func.HttpResponse("The JWT key has expired.", status_code=401)
    except jwt.InvalidTokenError:
        return func.HttpResponse("Invalid JWT key.", status_code=401)
    except Exception as e:
        return func.HttpResponse(f"Someting went wrong: {e}", status_code=500)