import os
import json

from fastapi import FastAPI, HTTPException
from pydantic import  BaseModel, Field
from typing import Optional, Union
from uuid import uuid4, UUID
from utils.hashtable import HashTable

from utils.functions import initDirectory, createJsonFile, loadDataFromJson, saveDataToJson

##################################################
# Get current directory and go back one level
##################################################



##################################################
# Create app FastAPI instance
##################################################
app = FastAPI()

##################################################
# Create hash_table instance
##################################################

hash_table = HashTable(3)

##################################################
#  Data Model
##################################################
class Data(BaseModel):
    id: Optional[str]
    key: str
    value: Union[str, int, float]

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)


#json_data = loadDataFromJson('../')
data = []

##################################################
# Routes with crud operations
##################################################

@app.get("/")
def read_root():
    return {"proyecto": "Proyecto BD distribuida", "version": "1.0", "autores": ["Juan Diego", "Santiago Aguirre", "Ricardo Gottheil", ]}


@app.get("/data")
def read_data():
    print('gets')
    print('get',hash_table.get_val('nombre'))
    return json_data

@app.post("/data")
def create_data(new_data: Data):
    print('new_data', new_data)
    new_data.id = str(uuid4())
    json_data = loadDataFromJson('../', new_data)
    json_data.append(new_data.dict())
    saveDataToJson('../', json_data, new_data)
    #hash_table.set_val(new_data.key, new_data.value)
    return new_data.dict()

@app.get("/data/{data_id}")
def get_data_by_id(data_id: str):
    for each_item_data in json_data:
        if each_item_data['id'] == data_id:
            return each_item_data

    raise HTTPException(status_code=404, detail="Data not found")

@app.delete("/data/{data_id}")
def delete_data_by_id(data_id: str):
    for index, data in enumerate(json_data):
        if data['id'] == data_id:
            json_data.pop(index)
            saveDataToJson(current_directory, json_data)
            return {"message": "Data deleted"}

    raise HTTPException(status_code=404, detail="Data not found")

@app.put("/data/{data_id}")
def update_data_by_id(data_id: str, new_data: Data):
    for index, data in enumerate(json_data):
        if data["id"] == data_id:
            json_data[index]["key"]= new_data.dict()["key"]
            json_data[index]["value"]= new_data.dict()["value"]
            return {"message": "Data updated"}

    raise HTTPException(status_code=404, detail="Data not found")
