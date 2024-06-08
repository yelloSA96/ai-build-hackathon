# Backend Application Documentation
This backend application is built using Python and Flask. It uses the `dotenv` package to manage environment variables and `poetry` for dependency management.

## Prerequisites
Before you can run this application, you need to have the following installed:

- Python 3.12 or higher
- Poetry 2.0 or higher

You can check your Python version by running `python --version` in your terminal. If you don't have Python installed or have an older version, you can download it from the [official Python website](https://www.python.org/downloads/).

To check your Poetry version, run `poetry --version`. If you don't have Poetry installed or have an older version, you can install it by following the instructions on the [official Poetry website](https://python-poetry.org/docs/#installation).

## Setup
1. Clone the repository to your local machine.
2. Navigate to the `backend` directory.
3. Install the project dependencies by running `poetry install`.
4. Create a `.env` file in the `backend` directory and add your environment variables. Here's a template you can use:

```dotenv
COHERE_API_KEY = "<your-api-key>"
PROJECT_DIRECTORY = "<path-to-your-project-directory>"
```
Replace `<your-api-key>` with your Cohere API key and `<path-to-your-project-directory>` with the path to the backend directory.  
Cohere API is being used for testing purposes only.

## Running the Application
Activate the Poetry environment by running poetry shell.
Run the application by executing `python main.py`.
The application will start running on `localhost:8080`. You can make POST requests to the /api endpoint.  

## Testing
Currently, there are no specific instructions for testing this application. You can use tools like Postman or curl to manually test the API endpoints.  

