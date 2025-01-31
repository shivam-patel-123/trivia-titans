import functions_framework
from google.cloud import firestore
import json

@functions_framework.http
def set_user(request):
    if request.method == "OPTIONS":
        headers = {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET",
            "Access-Control-Allow-Headers": "Content-Type",
            "Access-Control-Max-Age": "3600",
        }
        return ("", 204, headers)
    
    headers = {'Access-Control-Allow-Origin': '*'}

    request_json = request.get_json()
    db = firestore.Client()

    try:
        
        users_ref = db.collection('Users').where("username", "==",  request_json['username']).get()
        for user in users_ref:
            # user.to_dict()
            if user:
                print("user: ", user)
                user_ref = db.collection('Users').document(user.id)
                user_ref.update(request_json)
                return json.dumps({"message":"User details saved successfully", "userId": user.id}), 200, headers

        time, doc = db.collection('Users').add(request_json)
        
        return json.dumps({"message":"User details added successfully", "userId": doc.id}), 201, headers
    except Exception as e:
        return str(e), 500, headers
