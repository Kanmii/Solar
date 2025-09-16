from .geo_agent import GeoAgent

class SuperAgent:
    """
    The master orchestrator agent.
    It manages the entire workflow by calling other specialized agents in sequence.
    """
    def __init__(self):
        # Initialize all other agents
        self.geo_agent = GeoAgent()
        # self.sizing_agent = SizingAgent()
        # ...and so on
        print("SuperAgent initialized with all specialized agents.")

    def process(self, user_input: str):
        """
        The main entry point for processing a user request.
        For the walking skeleton, this will just call the Geo-Agent.
        """
        print(f"SuperAgent received input: '{user_input}'")

        # For now, we assume the user_input is the location.
        # In the real app, we'd parse this.
        location = user_input

        print("SuperAgent is calling the GeoAgent...")
        geo_data = self.geo_agent.get_solar_irradiance(location)

        # For now, just return the data from the geo_agent
        return geo_data

# Instantiate a single instance of the SuperAgent
super_agent = SuperAgent()
