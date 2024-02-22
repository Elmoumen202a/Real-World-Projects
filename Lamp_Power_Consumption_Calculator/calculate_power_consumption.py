def calculate_power_consumption(wattage, time_hours):
    """
    Calculate power consumption in kilowatt-hours.

    Parameters:
    - wattage (float): Wattage of the lamp
    - time_hours (float): Time the lamp is turned on in hours

    Returns:
    - float: Power consumption in kilowatt-hours
    """
    power_consumption = (wattage * time_hours) / 1000
    return power_consumption

# Example Usage
lamp_wattage = 60  # Replace with the wattage of your lamp
lamp_usage_time = 4  # Replace with the time the lamp is turned on in hours

power_consumed = calculate_power_consumption(lamp_wattage, lamp_usage_time)

print(f"The lamp consumed {power_consumed:.2f} kilowatt-hours of power.")
