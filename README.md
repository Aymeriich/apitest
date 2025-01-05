# Car Booking API

This project provides a REST API to manage vehicle availability and bookings. It is built using **FastAPI** for the API creation and **Pydantic** for data validation.

## Description

The API allows managing available vehicles for booking, as well as creating bookings for the vehicles. The data is stored in a JSON file and managed through endpoints to list available vehicles, create new bookings, etc.

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn
- Pydantic

## Installation

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/your_username/your_repository.git
    cd your_repository
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the necessary dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Start the development server:

    ```bash
    uvicorn api-test:app --reload
    ```

## Usage

Once the server is running, you can access the interactive API documentation at `http://127.0.0.1:8000/docs`.
