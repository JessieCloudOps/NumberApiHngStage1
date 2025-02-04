from fastapi import FastAPI, Query, HTTPException
import requests

app = FastAPI()

# Function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Function to check if a number is perfect
def is_perfect(n):
    return sum(i for i in range(1, n) if n % i == 0) == n

# Function to check if a number is Armstrong
def is_armstrong(n):
    digits = [int(d) for d in str(n)]
    return sum(d**len(digits) for d in digits) == n

@app.get("/api/classify-number")
def classify_number(number: str = Query(..., title="Number")):
    # Check if the input number can be converted to an integer
    try:
        # Try to convert number to an integer
        number = int(number)
    except ValueError:
        # If conversion fails, return the required error format
        return {"number": "alphabet", "error": True}

    # Proceed with the number classification logic
    properties = ["odd" if number % 2 else "even"]
    if is_armstrong(number):
        properties.insert(0, "armstrong")

    # Get fun fact from Numbers API
    fun_fact_response = requests.get(f"http://numbersapi.com/{number}/math?json")
    fun_fact = fun_fact_response.json().get("text", "No fun fact available")

    return {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "digit_sum": sum(int(d) for d in str(number)),
        "fun_fact": fun_fact
    }
