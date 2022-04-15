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
    if os.path.exists(directory + '/data/' + file_name) == False:
        print("Creating file: " + file_name)
        with open(directory + '/data/' + file_name, 'w') as outfile:
            json.dump(data, outfile)
    else:
        print("File already exists: " + file_name)
        pass

def loadDataFromJson(directory):
    with open( directory + '/data/base.json') as f: #specify the file name
        return json.load(f)

def saveDataToJson(directory, data):
    with open( directory + '/data/base.json', 'w') as f: #specify the file name
        json.dump(data, f)