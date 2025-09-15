class GeoAgent:
    """
    Handles all location-based calculations.
    """
    def get_solar_irradiance(self, location: str):
        """
        Takes a location string and returns a dummy dictionary of solar irradiance data.
        """
        print(f"GeoAgent received location: '{location}'")
        # In the future, this will involve real data lookups.
        # For now, return a hardcoded response.
        dummy_response = {
            "location_received": location,
            "dry_season_psh": 5.5,
            "rainy_season_psh": 4.0,
            "data_source": "dummy"
        }
        print(f"GeoAgent returning dummy data: {dummy_response}")
        return dummy_response
