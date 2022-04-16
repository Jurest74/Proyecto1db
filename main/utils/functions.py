import os
import json

def initDirectory(directory):
    if os.path.exists(directory + '/data') == False:
        print("Creating data directory")
        os.mkdir(directory + '/data')
    else:
        print("Data directory already exists")
        pass

# Create a json file with the data
def createJsonFile(directory, file_name, data):
    if os.path.exists(directory + '/' + file_name) == False:
        print("Creating file: " + file_name)
        with open(directory + '/' + file_name, 'w') as outfile:
            json.dump(data, outfile)
    else:
        print("File already exists: " + file_name)
        pass

def loadDataFromJson(directory, new_data):
    print('json.load(f)')
    hashed_key = (hash(new_data.key) % 3)
    hashed_key += 1
    print('hashed_key loaddata', hashed_key)
    with open( directory + '/data/nodo' + str(hashed_key) + '/base.json') as f: #specify the file name
        return json.load(f)

def saveDataToJson(directory, data, new_data):
    print('data', data)
    print('newdata', new_data)
    hashed_key = (hash(new_data.key) % 3)
    hashed_key += 1
    print('hashed_key', hashed_key)
    with open( directory + '/data/nodo'+str(hashed_key)+'/base.json', 'w') as f: #specify the file name
        json.dump(data, f)