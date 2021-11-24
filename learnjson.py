import json

# Opening JSON file
f = open('file.json', )

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list
for i in data['emp_details']:
    print(i)

# Closing file
f.close()

##########################################################################################
from urllib.request import urlopen
import json

url = "https://api.github.com"

response = urlopen(url)

data_json = json.loads(response.read())

print(data_json)
##########################################################################################
import json

# JSON data:
x = '{ "organization":"GeeksForGeeks", ' \
    ' "city": "Noida",' \
    ' "country": "India"}'

# python object to be appended
y = {"pin": 110096}

# parsing JSON string:
z = json.loads(x)

# appending the data
z.update(y)

# the result is a JSON string:
print(json.dumps(z))
#{“pin”: 110096, “organization”: “GeeksForGeeks”, “country”: “India”, “city”: “Noida”}

##########################################################################################

# Python program to update
# JSON

import json

def write_json(new_data, filename='file.json'):
    with open(filename, 'r+') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data["emp_details"].append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent=4)

    # python object to be appended


y = {"emp_name": "Nikhil",
     "email": "nikhil@geeksforgeeks.org",
     "job_profile": "Full Time"
     }

write_json(y)

##########################################################################################