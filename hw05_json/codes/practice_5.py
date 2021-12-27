import json

with open('example.json') as json_file:
    json_data = json.load(json_file)
json_string = json_data["cars"] 
print(json_string)
