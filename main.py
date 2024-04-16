import requests

APP_ID = "c9731833"
API_KEY = "7a549161f2a7694e7ef2bedc78f6f95e"
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

response = requests.post(url=POST_ENDPOINT, json=post_params, headers=headers)

print(response.text)
