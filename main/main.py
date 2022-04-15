import os

from fastapi import FastAPI, HTTPException
from pydantic import  BaseModel, Field
from typing import Optional, Union
from uuid import uuid4, UUID

# Get current directory and go back one level
os.chdir('../')
current_directory = os.getcwd()

#print(current_directory)


app = FastAPI()

#Data Model
class Data(BaseModel):
    id: Optional[UUID] = Field(default_factory=uuid4)
    key: str
    value: Union[str, int, float]


data = []

@app.get("/")
def read_root():
    return {"proyecto": "Proyecto BD distribuida", "version": "1.0", "autores": ["Juan Diego", "Santiago Aguirre", "Ricardo Gottheil", ]}


@app.get("/data")
def read_data():
    return data

@app.post("/data")
def create_data(new_data: Data):
    data.append(new_data.dict())
    return new_data.dict()

@app.get("/data/{data_id}")
def get_data_by_id(data_id: UUID):
    for each_item_data in data:
        if each_item_data['id'] == data_id:
            return each_item_data

    raise HTTPException(status_code=404, detail="Data not found")

@app.delete("/data/{data_id}")
def delete_data_by_id(data_id: UUID):
    for each_item_data in data:
        if each_item_data['id'] == data_id:
            data.remove(each_item_data)
            return {"message": "Data deleted"}

    raise HTTPException(status_code=404, detail="Data not found")

@app.put("/data/{data_id}")
def update_data_by_id(data_id: UUID, new_data: Data):
    for each_item_data in data:
        if each_item_data['id'] == data_id:
            each_item_data['key'] = new_data.key
            each_item_data['value'] = new_data.value
            return each_item_data

    raise HTTPException(status_code=404, detail="Data not found")
