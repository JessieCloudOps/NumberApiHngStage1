# Number Classification API 

This is a FastAPI-based API that classifies numbers based on mathematical properties and provides a fun fact.

## Features
- Checks if a number is **prime, perfect, Armstrong**.
- Determines if a number is **odd/even**.
- Calculates **sum of digits**.
- Fetches a **fun fact** using the Numbers API.

## API Usage
### Endpoint:
`GET /api/classify-number?number=<your_number>`

### Example Request:
`GET https://number-api-679178682037.us-central1.run.app/api/classify-number?number=371`

### Example Response:
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}


# Deployment
Deployed using **Google Cloud Run**.

# Installation (For Local Testing)
### 1. Clone the repository
```bash
git clone https://github.com/yourusername/number-api.git
cd number-api
pip install -r requirements.txt
uvicorn main:app --reload
```


