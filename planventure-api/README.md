# Planventure API

A RESTful API service for managing travel plans and itineraries.

## Overview

Planventure API is a Flask-based backend service that helps users create, manage, and organize their travel plans. It provides endpoints for handling trips, user management, and itinerary generation.

## Features

- User authentication and authorization
- Trip management (creation, updating, deletion)
- Location-based services with geographical coordinates
- Itinerary storage and management
- Timestamp tracking for all records

## Technical Stack

- **Framework**: Flask
- **Database**: SQLAlchemy ORM
- **Authentication**: JWT (JSON Web Tokens)
- **Data Format**: JSON

## Database Schema

### Users Table
- id (Primary Key)
- email
- password (hashed)
- created_at
- updated_at

### Trips Table
- id (Primary Key)
- user_id (Foreign Key)
- destination
- start_date
- end_date
- latitude
- longitude
- itinerary (JSON)
- created_at
- updated_at

## API Endpoints

### Authentication
- `POST /auth/register` - Register a new user
- `POST /auth/login` - User login
- `POST /auth/logout` - User logout

### Trips
- `GET /trips` - List all trips for a user
- `POST /trips` - Create a new trip
- `GET /trips/<id>` - Get trip details
- `PUT /trips/<id>` - Update trip details
- `DELETE /trips/<id>` - Delete a trip

## Setup and Installation

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up environment variables:
   ```bash
   export FLASK_APP=app.py
   export FLASK_ENV=development
   ```
5. Initialize the database:
   ```bash
   flask db upgrade
   ```
6. Run the application:
   ```bash
   flask run
   ```

## Contributing

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## License

MIT License

## Contact

For support or queries, please open an issue in the repository.
