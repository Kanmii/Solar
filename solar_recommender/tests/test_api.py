from fastapi.testclient import TestClient
from solar_recommender.app.api.main import app

client = TestClient(app)

def test_chat_endpoint_success():
    """
    Tests the full end-to-end flow of the walking skeleton.
    A request to /chat should go through the Super-Agent to the Geo-Agent
    and return the dummy response.
    """
    # Define the request payload
    request_payload = {"message": "Abuja, Nigeria"}

    # Send the request to the test client
    response = client.post("/api/v1/chat", json=request_payload)

    # Check the status code
    assert response.status_code == 200

    # Check the response body
    response_data = response.json()

    # The outer response should have a "response" key
    assert "response" in response_data

    # The inner response (from the agent) should match the dummy data
    agent_response = response_data["response"]

    assert agent_response["location_received"] == "Abuja, Nigeria"
    assert agent_response["data_source"] == "dummy"
    assert "dry_season_psh" in agent_response
    assert "rainy_season_psh" in agent_response

def test_chat_endpoint_no_message():
    """
    Tests that the endpoint handles a request with no message gracefully.
    """
    response = client.post("/api/v1/chat", json={})
    assert response.status_code == 200
    agent_response = response.json()["response"]
    assert agent_response["location_received"] == ""
