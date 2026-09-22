import os

import requests

api_key = os.environ["EMAILCHECKPRO_API_KEY"]
base_url = os.getenv("API_BASE_URL", "https://emailcheckpro.com")
identifier = os.getenv("IDENTIFIER", "alex.kim@gmail.com")
batch = os.getenv("MODE", "single") == "batch"
path = "/api/v1/batch-check" if batch else "/api/v1/check"
payload = {"service_type": "email", "identifiers": [identifier, "support@example.com"]} if batch else {"service_type": "email", "identifier": identifier}

response = requests.post(
    f"{base_url}{path}", headers={"X-API-Key": api_key}, json=payload, timeout=60
)
response.raise_for_status()
print(response.json())
