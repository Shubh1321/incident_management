import random
import datetime
import requests

def generate_incident_id():
    year = datetime.datetime.now().year
    random_number = random.randint(10000, 99999)
    return f"RMG{random_number}{year}"


def get_address_from_pincode(pincode):
    try:
        # Use a third-party API to fetch location information based on the pincode
        # Example using Zippopotam.us API for a location in the US
        # This can be replaced with an API for other countries as required
        response = requests.get(f'http://api.zippopotam.us/in/{pincode}')
        
        # If the API request is successful (status code 200)
        if response.status_code == 200:
            data = response.json()

            # Extract city and country from the response
            city = data.get('places', [{}])[0].get('place name', 'Unknown City')
            country = data.get('country', 'Unknown Country')

            return {"city": city, "country": country}
        else:
            # If response status is not OK (non-200 code), return a default message
            return {"city": "Unknown", "country": "Unknown"}

    except Exception as e:
        # Handle any exceptions that occur during the request
        print(f"Error occurred: {e}")
        return {"city": "Error", "country": "Error"}

def validate_incident_priority(priority):
    valid_priorities = ['High', 'Medium', 'Low']
    if priority not in valid_priorities:
        raise ValueError(f"Invalid priority: {priority}.")
