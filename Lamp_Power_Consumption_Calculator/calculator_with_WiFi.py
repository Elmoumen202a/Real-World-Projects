import requests

def get_lamp_data():
    # Implement code to fetch lamp data from the microcontroller over Wi-Fi
    # For example, use HTTP requests to an API endpoint exposed by the microcontroller
    lamp_data_url = "http://microcontroller-ip-address/lamp_data"
    response = requests.get(lamp_data_url)
    return response.json() if response.status_code == 200 else None

def calculate_power_consumption():
    lamp_data = get_lamp_data()

    if lamp_data:
        lamp_wattage = lamp_data.get("wattage", 0)
        lamp_usage_time = lamp_data.get("usage_time", 0)

        power_consumed = (lamp_wattage * lamp_usage_time) / 1000
        return power_consumed
    else:
        return None

# Example Usage
power_consumed = calculate_power_consumption()

if power_consumed is not None:
    print(f"The lamp consumed {power_consumed:.2f} kilowatt-hours of power.")
else:
    print("Failed to retrieve lamp data.")
