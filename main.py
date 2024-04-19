import os
import requests
from datetime import datetime

# GENDER = "male"
# WEIGHT_KG = 60
# HEIGHT_CM = 168
# AGE = 29

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]
SHEET_ENDPOINT = os.environ["SHEET_ENDPOINT"]
TOKEN = os.environ["TOKEN"]

NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com"
NATURAL_LANGUAGE_FOR_EXERCISE = "/v2/natural/exercise"
POST_ENDPOINT = f"{NUTRITIONIX_ENDPOINT}{NATURAL_LANGUAGE_FOR_EXERCISE}"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
post_params = {
    "query": input("Tell me which exercises you did: ")
}
bearer_headers = {
    "Authorization": f"Bearer {TOKEN}",
}

response = requests.post(url=POST_ENDPOINT, json=post_params, headers=headers)
result = response.json()

print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    sheet_response = requests.post(url=SHEET_ENDPOINT, json=sheet_inputs, headers=bearer_headers)

    print(sheet_response.text)
