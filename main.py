import requests
from datetime import datetime

# GENDER = "male"
# WEIGHT_KG = 60
# HEIGHT_CM = 168
# AGE = 29

APP_ID = "c9731833"
API_KEY = "7a549161f2a7694e7ef2bedc78f6f95e"

TOKEN = "GVHhhhhh62fff4fIGIGIGIGIGitititicgf58400001"

NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com"
NATURAL_LANGUAGE_FOR_EXERCISE = "/v2/natural/exercise"
POST_ENDPOINT = f"{NUTRITIONIX_ENDPOINT}{NATURAL_LANGUAGE_FOR_EXERCISE}"
SHEET_ENDPOINT = "https://api.sheety.co/f34ae5bff87e0200b3b4b3eef4f978de/myWorkouts/workouts"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

post_params = {
    "query": input("Tell me which exercises you did: ")
}

response = requests.post(url=POST_ENDPOINT, json=post_params, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

bearer_headers = {
    "Authorization": f"Bearer {TOKEN}",
}


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
