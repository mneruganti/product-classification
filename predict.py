import requests
import logging

API_URL = "http://127.0.0.1:8000/predict"

# Setup logging for client
logging.basicConfig(
    filename="client_logs.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

while True:
    title = input("Enter product title (or type 'exit' to quit): ")
    if title.lower() == 'exit':
        break

    response = requests.post(API_URL, json={"title": title})

    if response.status_code == 200:
        result = response.json()
        print(f"Predicted category ID: {result['predicted_category_id']}")
        logging.info(f"User input: '{title}' → Predicted category: {result['predicted_category_id']}")
    else:
        print(f"Error: {response.status_code} - {response.text}")
        logging.error(f"Failed request for: '{title}' → Status: {response.status_code}")
