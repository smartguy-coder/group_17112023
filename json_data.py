import json
from pprint import pprint


data = {
    'key': 'моє прізвище',
    'nickname': 'karpo',
    'age': 18,
    'hobbies': [
        'soccer',
        'tennis',
    ]
}

# json_string = json.dumps(data)
# # {"key": "\u043c\u043e\u0454 \u043f\u0440\u0456\u0437\u0432\u0438\u0449\u0435", "nickname": "karpo", "age": 18, "hobbies": ["soccer", "tennis"]}
# pprint(json_string)
#
# data_from_json = json.loads(json_string)
# pprint(data_from_json)


with open('data.json', mode='w') as file:
    # json.dump(data, file)
    json.dump(data, file, indent=4)















