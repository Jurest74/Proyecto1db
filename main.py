# main.py
from fastapi import FastAPI, Response, status
from pydantic import BaseModel
import csv
import json

class DataBaseModel(BaseModel):
    key: str
    value: str

app = FastAPI()



@app.get("/", status_code=200)
async def get_data(key):
    csv_file = csv.reader(open('D:/DATOS DE USUARIO/Desktop/main/node.csv', "r"), delimiter='"')
    for row in csv_file:
        row_str = str(row)
        if('key: '+key in row_str):
            print("key value find", row_str)
    return {"Hello": "World"}

@app.post("/", status_code=201)
async def set_data(item: DataBaseModel):
    print(item.key)
    with open('D:/DATOS DE USUARIO/Desktop/main/node.csv', 'a', encoding='UTF8', newline='') as f:
        text = json.dumps(item.__dict__)
        text = text.replace('"', '')
        print("text", text)
        writer = csv.writer(f)
        writer.writerow([text])
    return {"status": 200}

@app.delete("/", status_code=200)
async def delete_data(key: str, response: Response):
    return "delete"

@app.put("/", status_code=200)
async def update_data(key: str, response: Response):
    return "update"


#@app.api_route("/data", methods = ['GET', 'POST'])
#def handle_data(item):
#    print(item)
#    return item