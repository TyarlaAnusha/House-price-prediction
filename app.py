# install libraries ---
# pip install fastapi uvicorn scikit-learn

# 1. Library imports
import uvicorn
from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware
import pickle

# 2. Create the app object
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 3. load the model
rgModel = pickle.load(open("1024.pkl", "rb"))

# 4. Index route, opens automatically on http://127.0.0.1:80
@app.get('/')
def index():
    return {'message': 'Hello, World'}

# 5. Run the API with uvicorn
if __name__ == '__main__':
    uvicorn.run(app, port=80, host='0.0.0.0')
#---------------------------
@app.get("/predictPrice")
def gePredictPrice(area: int, bedRooms: int, bathRooms: int,stories:int,parking:int,mainroad_n:int,guestroom_n:int,basement_n:int,hotwaterheating_n:int,airconditioning_n:int,prefarea_n:int,furnishingstatus_n:int):
    prediction = rgModel.predict([[area,bedRooms,bathRooms,stories,parking,mainroad_n,guestroom_n,basement_n,hotwaterheating_n,airconditioning_n,prefarea_n,furnishingstatus_n]])
    return {'Price': prediction[0]}
    
# uvicorn app:app --host 0.0.0.0 --port 80
# http://127.0.0.1/predictPrice?area=8960&bedRooms=4&bathRooms=3&stories=3&parking=2&mainroad_n=1&guestroom_n=0&basement_n=0&hotwaterheating_n=0&airconditioning_n=1&prefarea_n=0&furnishingstatus_n=0

