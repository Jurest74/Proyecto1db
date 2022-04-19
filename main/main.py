from fastapi import FastAPI, HTTPException
from pydantic import  BaseModel, Field
from typing import Optional, Union

from utils.hashtable import HashTable
from utils.functions import initDirectory, createJsonFile, loadDataFromJson, saveDataToJson

##################################################
# Get current directory and go back one level
##################################################

numeroNodos = 3

##################################################
# Create app FastAPI instance
##################################################
app = FastAPI()

##################################################
# Create hash_table instance
##################################################

hash_table = HashTable(numeroNodos)

##################################################
#  Data Model
##################################################
class Data(BaseModel):
    key: str
    value: Union[str, int, float]


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
    
    return hash_table.get_all_values()

@app.post("/data")
def create_data(new_data: Data):
    hashed_key = new_data.key
    json_data = loadDataFromJson('../', hashed_key, numeroNodos)
    for each_item_data in json_data:
        if each_item_data['key'] == new_data.key:
            raise HTTPException(status_code=400, detail="Key already exists")

    json_data.append(new_data.dict())
    saveDataToJson('../', json_data, new_data, numeroNodos)
    return new_data.dict()

@app.get("/data/{data_key}")
def get_data_by_id(data_key: str):
    json_data = hash_table.get_all_values()
    for each_item_data in json_data:
        if each_item_data['key'] == data_key:
            return each_item_data

    raise HTTPException(status_code=404, detail="Data not found")

@app.delete("/data/{data_key}")
def delete_data_by_id(data_key: str):
    json_data = hash_table.get_all_values()
    for _, data in enumerate(json_data):
        if data['key'] == data_key:
            print(data_key)
            hash_table.delete_val(data_key)
            return {"message": "Data deleted"}

    raise HTTPException(status_code=404, detail="Data not found")

@app.put("/data/{data_key}")
def update_data_by_id(data_key: str, new_data: Data):
    json_data = loadDataFromJson('../', data_key, numeroNodos)
    for index, data in enumerate(json_data):
        if data["key"] == data_key:
            json_data[index]["key"]= new_data.dict()["key"]
            json_data[index]["value"]= new_data.dict()["value"]
            return {"message": "Data updated"}

    raise HTTPException(status_code=404, detail="Data not found")
