import requests


TIMEOUT = 10  # max. time will wait for a server response before stopping the request
BASE_URL = "https://jsonplaceholder.typicode.com"


# Usage: pytest tests/test_api.py
class TestJSONPlaceholderAPI:
    """JSONPlaceholder (https://jsonplaceholder.typicode.com) is a free fake REST API service for API testing.
    - Data is mocked (fake)
    - Responses are consistent and predictable
    - Does not persist data
    - Accepts default HTTP requests (No headers required)
    Test and Validate the following endpoints:
    - GET /users/1
    - POST /posts
    - GET /users/999
    """

    def test_fetch_user_successfully(self):
        """Test GET /users/1
        Validate:
        - Status code is 200 OK (success)
        - Required fields exist in response
        """
        url = f"{BASE_URL}/users/1"
        print(f"\nSending GET request to {url}")
        try:
            response = requests.get(url, timeout=TIMEOUT)
            response.raise_for_status()  # raise an HTTPError for bad responses (4xx and 5xx)
        except requests.exceptions.RequestException as e:
            assert False, f"Request failed: {e}"

        # Validate HTTP 200 OK status code (server successfully processed the request)
        assert response.status_code == 200, "Expected HTTP status code 200 OK SUCCESS"

        # Parse response JSON
        data = response.json()

        # List of fields expected in the API response
        for field in ["id", "name", "email"]:
            assert field in data, f"Response missing field: {field}"  # verify each field exists in the response data

    def test_create_new_post(self):
        """Test POST /posts
        Validate:
        - Status code is 201 (created)
        - Response contains sent data, and id is generated for the new resource
        """
        url = f"{BASE_URL}/posts"
        payload = {
            "title": "foo",
            "body": "bar",
            "userId": 1
        }

        print(f"\nSending POST request to {url} with JSON payload={payload}")
        try:
            response = requests.post(url, json=payload, timeout=TIMEOUT)
            response.raise_for_status()  # raise an HTTPError for bad responses (4xx and 5xx)
        except requests.exceptions.RequestException as e:
            assert False, f"Request failed: {e}"

        # # Validate HTTP 201 Created status code (request successfully create a new resource on the server)
        assert response.status_code == 201, "Expected HTTP status code 201 Created"

        # Parse response JSON
        data = response.json()

        # Loop through each key in the request payload to validate API response
        for key in payload:
            assert key in data, f"Response missing field: {key}"    # verify that the response contians the expected field
            assert data[key] == payload[key], f"{key} mismatch"     # compare the actual resposne value with the expected payload value

        # Validate id is generated
        assert "id" in data, "Response missing required field: id"

    def test_handle_nonexistent_user(self):
        """
        Test GET /users/999
        Validate:
        - Status code is 404 (Not Found)
        - HTTP response data should be empty
        """
        url = f"{BASE_URL}/users/999"

        print(f"\nSending GET request to {url}")
        try:
            response = requests.get(url, timeout=TIMEOUT)
        except requests.exceptions.RequestException as e:
            assert False, f"Request failed: {e}"

        # Validate status code
        assert response.status_code == 404, "Expected HTTP status code 404 Not Found"

        # Validate response data is empty
        data = response.json()
        assert not data, "Expected empty response body"
        