# SS&C Test Framework
A lightweight Python-based test framework for API testing and functional programming, built with pytest.


## Overview
This project demonstrates two core areas:

**1. Functional Programming**
- A function that removes duplicates from a list while preserving order.

**2. API Automation Tests**
- Built using [Python](https://www.python.org/), [pytest](https://docs.pytest.org/en/stable/getting-started.html), and [requests](https://requests.readthedocs.io/en/latest/user/install/)
- Validates REST APIs and error handling

**Target API:** https://jsonplaceholder.typicode.com/

**Test Endpoints**
- **`GET /users/1`** → Retrieve user information
- **`POST /posts`** → Create a new post
- **`GET /users/999`** → Handle non-existent resources (404)


## Testing Philosophy
- Focuses on clarity, correctness, and QA automation fundamentals
- Tests are intentionally simple and readable
- No complex frameworks or additional dependencies
- Uses a mock API, so data is not persisted


## Tech Stack
- Python 3.10+
- pytest
- requests


## Installation
### Prerequisites
- Python 3.10 or higher (recommended: 3.14)
- [pip](https://pypi.org/project/pip/) package manager

### Setup Steps
**1. Clone the repository**
```bash
git clone git@github.com:yoyo4cash/ssnc-test-framework.git
cd ssnc-test-framework
```

**2. Create a virtual environment** _(Optional but recommended - use a virtual environment to isolate dependencies and ensure consistency)_
```bash
python3 -m venv venv
source venv/bin/activate  # MacOS/Linux
```

**3. Install dependencies:**
```bash
pip install -r requirements.txt
```


## Usage
### Running Tests
Run all tests:
```bash
pytest tests
```

Run remove duplicates test:
```bash
pytest tests/test_remove_duplicates.py
```

Run API tests:
```bash
pytest tests/test_api.py
```


## Configuration
### Pytest Configuration `(pytest.ini)`
```ini
[pytest]
addopts = -v --tb=short --capture=no
testpaths = tests
```

**Options:**
- `-v:` Verbose output
- `--tb=short:`  Simplified traceback for readability
- `--capture=no:` Shows print/debug logs in real time
- `testpaths = tests:` Restricts test discovery to `tests/`

### API Constants:
- `BASE_URL = "https://jsonplaceholder.typicode.com"`
- `TIMEOUT = 10 seconds`


## Test Coverage
### Implemented API Test Cases
**GET /users/1**
- Status code validation: `200 OK`
- Required field validation:
    - id
    - name
    - email

**POST /posts**
- Status code validation: `201 Created`
- Request payload validation
- Response data matching
- Auto-generated ID validation

**GET /users/999**
- Status code validation: `404 Not Found`
- Empty response validation


## QA Thinking
**Additional QA scenarios considered but not implemented due to scope:**

- Empty payload in POST request:
    ```json
    {}
    ```
- Missing required fields in request payload:
    ```json
    { "title": "some-title" }
    ```
- Invalid data types in request payload:
    ```json
    { "title": 123, "body": False, "userId": "foo" }
    ```

- Extra unexpected fields in request payload:
    ```json
    { "title": "foo", "body": "bar", "userId": 1, "unexpected_field": "blah" }
    ```

- Special characters in request payload:
    ```json
    { "title": "<script>blah...</script>", "body": "AND =--" }
    ```

- Timeout / slow response handling:
    ```python
    requests.get(url, timeout=1)
    ```
