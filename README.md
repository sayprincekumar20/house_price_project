### House Price Prediction Website

This repository contains a House Price Prediction web application built using the Django framework. The application allows users to input features of a house and get a predicted price using a Machine Learning model.

The project is fully containerized with Docker and deployed on Render for live hosting.

   🚀 Features

   * Machine Learning Model: Predicts house prices based on input features.

   * Django Framework: Backend developed using Python and Django.

   * REST API: Provides endpoints for fetching predictions.

   * Docker Support: Easily deployable using Docker.

Live Deployment: Hosted on Render.

📂 Project Structure

├── app/                  # Django Application
│   ├── models.py         # ML Model Integration
│   ├── views.py          # API and Web View Handling
│   ├── urls.py           # URL Routing
│   ├── templates/        # Frontend Templates
│   ├── static/           # CSS, JS, Images
├── Dockerfile            # Docker Configuration
├── requirements.txt      # Python Dependencies
├── manage.py             # Django Management Script
└── README.md             # Project Documentation

🛠️ Installation & Setup

Prerequisites

Python 3.x

Docker (optional for containerization)

Render account (for deployment)

1️⃣ Clone the Repository

git clone https://github.com/your-username/house-price-prediction.git
cd house-price-prediction

2️⃣ Install Dependencies

pip install -r requirements.txt

3️⃣ Run Migrations

python manage.py migrate

4️⃣ Start the Django Server

python manage.py runserver

Visit http://127.0.0.1:8000/ in your browser.

🐳 Running with Docker

Build and run the Docker container:

docker build -t house-price-app .
docker run -p 8000:8000 house-price-app

🌍 Deployment on Render

This application is deployed on Render for live access. Follow these steps to deploy:

Push your code to a GitHub repository.

Create a new Web Service on Render.

Connect your GitHub repository.

Set up Python environment and necessary build commands.

Deploy the application and access it via the live URL.

📝 License

This project is licensed under the MIT License.

📧 Contact

For queries or contributions, feel free to reach out!

Happy coding! 🚀

