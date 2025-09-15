def evaluate_scoring_model(model, test_data):
    """
    Evaluates the scoring model using MAE and R-squared.
    """
    print("Evaluating scoring model...")
    # TODO: Implement evaluation logic
    # - Make predictions on test data
    # - Calculate MAE
    # - Calculate R-squared
    # return {"mae": 0.5, "r2": 0.8}
    pass

def evaluate_recommendation_model(model, test_data):
    """
    Evaluates the recommendation model using Precision@k and nDCG.
    """
    print("Evaluating recommendation model...")
    # TODO: Implement ranking evaluation logic
    # - Generate recommendations for test users
    # - Calculate Precision@k
    # - Calculate nDCG
    # return {"precision_at_3": 0.7, "ndcg": 0.85}
    pass

if __name__ == "__main__":
    # This script can be run from the command line
    # to evaluate all models.
    print("Model evaluation script finished.")
