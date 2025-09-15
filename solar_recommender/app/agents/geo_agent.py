class GeoAgent:
    """
    Handles all location-based calculations.
    """
    def get_solar_irradiance(self, location: str):
        """
        Takes a location string and returns solar irradiance data.
        """
        # TODO: Implement robust location parsing
        # TODO: Use API or data to get Peak Sun Hours (PSH) for the location
        # TODO: Return different values for Dry and Rainy seasons
        print(f"GeoAgent getting data for: {location}")
        return {"dry_season_psh": 5.0, "rainy_season_psh": 3.5}
