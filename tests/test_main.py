from fastapi.testclient import TestClient
from app.main import app

# Create a TestClient instance
client = TestClient(app)

def test_predict_sentiment():
    # Prepare a sample text input
    data = {
        "text": "I love this product! It's amazing."
    }

    # Send a POST request to the /predict endpoint
    response = client.post("/predict", json=data)

    # Check that the response status code is 200 (OK)
    assert response.status_code == 200

    # Parse the response JSON
    response_data = response.json()

    # Verify that 'sentiment' and 'score' are present in the response
    assert "sentiment" in response_data
    assert "score" in response_data

    # Verify the types of 'sentiment' and 'score'
    assert isinstance(response_data["sentiment"], str)
    assert isinstance(response_data["score"], float)

    # Check that the score is between 0 and 1
    assert 0.0 <= response_data["score"] <= 1.0
