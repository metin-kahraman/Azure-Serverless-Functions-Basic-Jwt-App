# Azure Functions with JWT-Based User Registration and Information Retrieval Application

This project is a simple user registration and JWT (JSON Web Token) based user information retrieval application developed using Azure Functions. Users can register and receive a JWT key in return. This key can then be used to query user information (in this example, only the username).

## Project Description

This project demonstrates a basic authentication flow using the serverless capabilities of Azure Functions.

* **RegisterUser Function:** Accepts a username and password (in this example, only the password is received; in a real application, it should be stored securely). Upon successful registration, it generates a JWT key containing the user's username and valid for a specific duration.
* **GetUserInfo Function:** Verifies the JWT key sent in the `Authorization` header with the `Bearer` scheme. If the key is valid, it returns the username from the key.

**Note:** This example is a basic JWT implementation, and production environments may require additional security measures and features (e.g., password hashing, database integration, token refresh mechanism).

## Prerequisites

The following software and tools must be installed on your computer to run this project:

* [Azure Functions Core Tools](https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=windows%2Ccsharp%2Cbash)
* [Python 3.6 or later](https://www.python.org/downloads/)
* [pip](https://pip.pypa.io/en/stable/installing/) (Python package installer)

## Setup and Running

### Local Development

1.  **Clone the Repository:** Clone this project from GitHub (if you haven't already).
    ```bash
    git clone https://github.com/metin-kahraman/Azure-Serverless-Functions-Basic-Jwt-App
    cd Azure-Serverless-Functions-Basic-Jwt-App
    ```

2.  **Install Dependencies:** If a `requirements.txt` file doesn't exist in the project directory, create one with the following content:
    ```
    azure-functions
    PyJWT
    ```
    Then, run the following command to install the necessary libraries:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Functions:** Run the following command from the root of the project directory to start the Azure Functions application locally:
    ```bash
    func start
    ```
    This command will start your functions on a local HTTP server (usually `http://localhost:7071`).

### Deployment to Azure

1.  **Create an Azure Function App:** Create a Function App in the Azure portal. When creating it, consider the following settings:
    * **Runtime stack:** Python
    * **Region:** Select the region closest to you.

2.  **Configure Deployment:** You can deploy your local project to Azure using the Azure Functions Core Tools. Run the following command from the root of your project directory (replace `<function_app_name>` with your Function App name):
    ```bash
    func azure functionapp publish <function_app_name> --build remote
    ```
    This command will deploy your project to your Function App in Azure.

## Function Endpoints

### RegisterUser (EN)

* **Endpoint:** `/api/RegisterUser`
* **HTTP Method:** `POST`
* **Request Body (JSON):**
    ```json
    {
        "username": "your_username",
        "password": "your_password"
    }
    ```
* **Successful Response (Status Code: 200 OK):**
    ```json
    {
        "token": "generated_jwt_key"
    }
    ```
* **Error Responses:**
    * **Status Code: 400 Bad Request:** Returned if the request body is not valid JSON or if the `username` and `password` fields are missing.

### GetUserInfo

* **Endpoint:** `/api/GetUserInfo`
* **HTTP Method:** `GET`
* **Request Header:**
    ```
    Authorization: Bearer <jwt_key>
    ```
* **Successful Response (Status Code: 200 OK):**
    ```json
    {
        "username": "your_username"
    }
    ```
* **Error Responses:**
    * **Status Code: 401 Unauthorized:** Returned if the `Authorization` header is missing, the `Bearer` scheme is not used, or the JWT key is invalid or expired.
    * **Status Code: 500 Internal Server Error:** Returned if an unexpected error occurs.

## Usage

### User Registration 

1.  Use an HTTP client (e.g., Postman, Insomnia, `curl`) to send a `POST` request to the `RegisterUser` endpoint.
2.  Provide your username (`username`) and password (`password`) in the request body as valid JSON.
3.  Upon a successful request, you will receive a JWT key in the `token` field of the response body. Store this key securely.

**Example `curl` request:**

```bash
curl -X POST -H "Content-Type: application/json" -d '{"username": "test_user", "password": "secure_password"}' <register_user_endpoint_url>