# Genderize API

## Overview

A simple REST API that classifies a name by gender using the [Genderize.io](https://genderize.io) API.

## Getting Started

### Prerequisites

- Python 3.8+

### Installation

1. Clone the repository

```bash
   git clone https://github.com/Mastermind-code/Stage_0_API_Integration_Data_Processing.git
   cd Stage_0_API_Integration_Data_Processing
```

2. Create a virtual environment

```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies

```bash
   pip install -r requirements.txt
```

4. Run the server

```bash
   uvicorn main:app --reload
```

The server will start at http://127.0.0.1:8000.

## API Documentation

### Classify Name

`GET /api/classify?name={name}`

**Success Response (200)**

```json
{
  "status": "success",
  "data": {
    "name": "john",
    "gender": "male",
    "probability": 1.0,
    "sample_size": 2692560,
    "is_confident": true,
    "processed_at": "2026-04-14T17:09:19Z"
  }
}
```

**Error Responses**
400 Bad Request: The name parameter is missing or empty.
422 Unprocessable Entity: Name contains non-letter characters.
502 Bad Gateway: The external Genderize service is down or timed out.

## Tech Stack

FastAPI - The web framework.
HTTPX - Async HTTP client.
Pydantic - Data validation.

## Author

Adebowale Adam Adewale
