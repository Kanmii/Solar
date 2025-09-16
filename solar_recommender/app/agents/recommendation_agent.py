class RecommendationAgent:
    """
    The "smart selector" that uses ML models to recommend specific components.
    """
    def __init__(self):
        # TODO: Load the trained Scoring model (e.g., RandomForest/XGBoost)
        # TODO: Load the trained Recommendation model (e.g., KNN)
        pass

    def get_recommendations(self, system_specs: dict, component_database: list):
        """
        Takes the required system specs and a component database,
        and returns the top 3 recommended system configurations.
        """
        # TODO: Implement the two-model pipeline:
        # 1. Use Scoring model to score all components.
        # 2. Use Recommendation model (KNN) to find the top 3 best combinations
        #    that meet the specs and budget.
        print(f"RecommendationAgent finding best components for specs: {system_specs}")
        return [
            {"system_score": 0.95, "components": ["Panel A", "Battery B", "Inverter C"]},
            {"system_score": 0.92, "components": ["Panel D", "Battery E", "Inverter F"]},
        ]
