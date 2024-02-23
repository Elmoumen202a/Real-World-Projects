# tests.py
import unittest
from main import get_weather, get_location, is_good_day_to_grow_plant

class TestWeatherAndPlantGrowth(unittest.TestCase):
    def test_get_weather(self):
        # Test get_weather with a known city (replace with your city)
        api_key = 'YOUR_OPENWEATHER_API_KEY'
        city = 'YourCity'
        weather = get_weather(api_key, city)
        self.assertTrue(isinstance(weather, str))  # Assuming weather is a string

    def test_get_location(self):
        # Test get_location with a known address (replace with your address)
        api_key = 'YOUR_GOOGLE_MAPS_API_KEY'
        address = 'YourPlantingLocation'
        location = get_location(api_key, address)
        self.assertTrue(location is not None)  # Assuming location is a tuple of lat, lng

    def test_is_good_day_to_grow_plant(self):
        # Test is_good_day_to_grow_plant with different weather conditions
        self.assertTrue(is_good_day_to_grow_plant('clear'))
        self.assertFalse(is_good_day_to_grow_plant('rain'))
        self.assertFalse(is_good_day_to_grow_plant('cloudy'))

if __name__ == "__main__":
    unittest.main()
