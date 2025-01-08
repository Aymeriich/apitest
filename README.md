# Car Booking API

This project provides a REST API to manage vehicle availability and bookings. It is built using **FastAPI** for the API creation and **Pydantic** for data validation.

## Description

The API allows managing available vehicles for booking, as well as creating bookings for the vehicles. The data is stored in a JSON file and managed through endpoints to list available vehicles, create new bookings, etc.

## Requirements

- fastapi==0.95.0
- uvicorn==0.23.0
- pydantic==1.11.1
- pytest==7.2.2
- httpx==0.23.0 

## Installation

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/aymeriich/apitest.git
    cd apitest
    ```

2. Install the necessary dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

Once the dependencies are installed you will be able to start the application or start with the unit tests, to start it locally we will use inside the app directory:


    uvicorn app.main:app --reload


To start the tests we will use:


    pytest tests/tests.py


## Design 

The structure of the application has been designed in a modular way for ease of maintenance, scalability and code clarity. The main reasons behind the organisation are detailed below:

### Folder app/:

main.py: 
This is the entry point of the FastAPI application. This is where the app is initialised, logs are configured and endpoints are included. This file is responsible for starting the API and connecting the different components.

endpoints.py: 
Contains the API routes and the logic associated with each endpoint, such as getting available vehicles and creating reservations. The endpoints are separated to maintain clarity and avoid overloading the main.py file.

models.py: 
Defines the data structures that the API expects to receive and return. We use Pydantic to validate requests and responses. This separation allows the models to be reusable and clear.

services.py: 
Contains the data manipulation functions (loading and saving information). By having this logic in a separate file, it can be easily modified without affecting the endpoints, which improves the maintainability of the system.

### Tests/ folder:

Tests are in a separate folder to maintain a clear distinction between production code and test cases. This organisation helps keep the code clean and ensures that tests do not interfere with the application code.

