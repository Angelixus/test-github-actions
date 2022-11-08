import json

with open('test.json') as fp:
    data = json.loads(fp.read())
    for player in data.values():
        del player['configId']

with open('test.json', 'w') as fw:
    json.dump(data, fw, indent=4)