import json

with open("triviaJSON.py", "r") as read_file:
    data = json.load(read_file)
    
print(data[0]["question"])