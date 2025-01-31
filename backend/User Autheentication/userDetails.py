import functions_framework
from google.cloud import firestore
import json

@functions_framework.http
def userdetails(request):

  if request.method == "OPTIONS":
    # Allows GET requests from any origin with the Content-Type
    # header and caches preflight response for an 3600s
    headers = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "GET",
        "Access-Control-Allow-Headers": "Content-Type",
        "Access-Control-Max-Age": "3600",
    }

    return ("", 204, headers)

  request_json = request.get_json()
  db = firestore.Client()

  try:
    headers = {
      'Access-Control-Allow-Origin': '*',
    }
    username = request_json['username']
    print("username: ", username)
    users_ref = db.collection('Users').where("username", "==", username).get()
    for user in users_ref:
      user.to_dict()
      print("user: ", user)
      if user:
        userData = user.to_dict()
        userData["userId"] = user.id
        return json.dumps(userData), 200, headers
    return json.dumps({"message":"User not available"}), 404, headers
  
  except Exception as e:
    headers = {"Access-Control-Allow-Origin": "*"}
    return str(e), 500, headers
  

