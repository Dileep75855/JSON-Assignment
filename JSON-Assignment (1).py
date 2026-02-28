#Task - 1 Build a JSON Structure
import json
user_profile = {
    "name":"Alice",
    "age":21,
    "gmail":"alice@gmail.com",
    "is_active":True,
    "skills":["python","sql","Data Analysis"]
}
json_string = json.dumps(user_profile,indent = 4)
print(json_string)
print("="*30)
#Task - 2 Parse an API Response
response = '''
{
"status":"success",
"data":{"user_id":101,"username":"alexa99","score":87.5}
}
'''
parsed_data = json.loads(response)
username = parsed_data["data"]["username"]
score = parsed_data["data"]["score"]
print("Username : ",username)
print("Score : ",score)
print(f"User {username} scored {score} points")
print("="*30)

#Task - 3 Handle Nested JSON
user = {
    "name":"bob",
    "address":{
        "city":"bengaluru",
        "state":"karnataka",
        "zip":560001
    }
}
city = user["address"]["city"]
zip_code = user["address"]["zip"]
print("City : ",city)
print("Zip Code : ",zip_code)
user["address"]["country"] = "India"
print(json.dumps(user,indent = 4))
