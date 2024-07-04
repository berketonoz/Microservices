# Microservices

This repository contains a microservices-based project, showcasing various services interacting to form a cohesive application. It serves as an example of implementing a microservices architecture using modern technologies.

## Table of Contents

- [About](#about)
- [Technologies Used](#technologies-used)
- [Setup](#setup)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## About

The Microservices project demonstrates the creation and interaction of multiple independent services. Each service is responsible for a specific functionality and communicates with other services via APIs.

## Technologies Used

- **Services:**
  - Python (Flask)
- **Database:**
  - SQLite
- **Containerization:**
  - Docker

## Setup

To set up this project locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/berketonoz/Microservices.git
    ```
2. Navigate to the project directory:
    ```bash
    cd Microservices
    ```
3. Build and run the Docker containers:
    ```bash
    docker-compose up --build
    ```

## Usage

Each service can be accessed via its respective endpoint. Ensure all services are running before making requests. The services interact to perform operations such as creating, reading, updating, and deleting records.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch:
    ```bash
    git checkout -b feature-branch
    ```
3. Make your changes and commit them:
    ```bash
    git commit -m "Description of the feature"
    ```
4. Push to the branch:
    ```bash
    git push origin feature-branch
    ```
5. Open a pull request describing your changes.

## License

This project is licensed under the Apache-2.0 License. See the [LICENSE](LICENSE) file for details.

