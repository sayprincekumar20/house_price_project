# Django Website with Docker and Render Deployment

This is a web application built using the Django framework. The project includes Docker integration and has been successfully deployed on the Render platform for live access.

## Features

- **Django-based Web Application**: Built with the Django framework to ensure scalability and performance.
- **Docker Integration**: The project is containerized using Docker for seamless deployment.
- **Render Deployment**: Hosted on Render, making the website accessible online.
- **Database Support**: Configured with PostgreSQL/MySQL (mention if applicable).
- **Authentication System**: User authentication and authorization features.
- **Responsive UI**: Designed with Tailwind CSS or Bootstrap (mention if applicable).
- **REST API**: Built with Django REST Framework (if applicable).

## Live Demo

🔗 [Live Website](https://house-price-project.onrender.com)

## Installation and Setup

### Prerequisites

Ensure you have the following installed on your system:
- Python (>= 3.8)
- Django (>= 4.0)
- Docker (if using containerization)
- PostgreSQL/MySQL (if applicable)
- Git

### Clone the Repository
```bash
git clone https://github.com/your-github-username/house-price-predictor.git
cd your-repo-name
```

### Install Dependencies
Create a virtual environment and install dependencies:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt
```

### Configure Environment Variables
Create a `.env` file in the root directory and configure the necessary environment variables:
```
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=your_database_url
ALLOWED_HOSTS=your_domain_or_localhost
```

### Apply Migrations
```bash
python manage.py migrate
```

### Run the Development Server
```bash
python manage.py runserver
```
Visit `http://127.0.0.1:8000/` to view the site.

## Docker Setup

### Build and Run the Container
```bash
docker build -t house-price-predictor .
docker run -p 8000:8000 house-price-project
```

## Deployment on Render

### Steps to Deploy
1. Push your code to a GitHub repository.
2. Create a new web service on Render.
3. Connect it to your GitHub repository.
4. Set up environment variables in the Render dashboard.
5. Deploy the application.

## Contributing
If you'd like to contribute, please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License.

---

For any queries, feel free to reach out! 🚀
