
# Product Server

A simple Flask-based API for managing a list of products. This project demonstrates basic CRUD (Create, Read, Update, Delete) operations with a RESTful API.

## Features

- Retrieve a list of products
- Retrieve a specific product by ID
- Add a new product
- Update an existing product

## Endpoints

### GET /products

Retrieves the list of all products.

**Response:**
```json
[
    {
        "id": 143,
        "name": "Notebook",
        "price": 5.49
    },
    {
        "id": 144,
        "name": "Black Marker",
        "price": 1.99
    }
]
```

### GET /products/<id>

Retrieves a specific product by its ID.

**Response:**
```json
{
    "id": 143,
    "name": "Notebook",
    "price": 5.49
}
```

### POST /products

Adds a new product to the list.

**Request Body:**
```json
{
    "id": 145,
    "name": "Pen",
    "price": 0.99
}
```

**Response:**
- Status: `201 Created` if the product is successfully added.
- Status: `400 Bad Request` if there is an error in the request.

### PUT /products/<id>

Updates an existing product by its ID.

**Request Body:**
```json
{
    "name": "Updated Product Name",
    "price": 2.99
}
```

**Response:**
- Status: `200 OK` if the product is successfully updated.
- Status: `404 Not Found` if the product does not exist.

## Installation

1. Clone the repository:
    ```sh
    git clone <repository_url>
    cd <repository_name>
    ```

2. Create a virtual environment:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Run the application:
    ```sh
    python products.py
    ```

5. Access the API at `http://127.0.0.1:5000`

## Dependencies

- Flask
- Flask-CORS

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Flask](https://flask.palletsprojects.com/) - The web framework used
- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/) - Handling Cross-Origin Resource Sharing (CORS)
