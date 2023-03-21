import requests
import json

info = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "Bingo",
  "photoUrls": [
    "Bingo's photo"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
res = requests.put(f"https://petstore.swagger.io/v2/pet", headers={'accept': 'application/json', 'Content-Type': 'application/json'},
                         data=json.dumps(info, ensure_ascii=False))

print(res.json)
print(res.status_code)