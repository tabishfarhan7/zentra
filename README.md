<div align="center">

# 🏥 Zentra ML API

### *AI-Powered Health Analytics & Obesity Prediction Platform*

[![FastAPI](https://img.shields.io/badge/FastAPI-0.109.0-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.4.0-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![JWT](https://img.shields.io/badge/JWT-Authentication-000000?style=for-the-badge&logo=JSON%20web%20tokens&logoColor=white)](https://jwt.io/)

**A comprehensive backend API for health analytics featuring JWT authentication, user profile management, and ML-powered obesity prediction using Random Forest classification.**

[Features](#-features) • [Tech Stack](#-tech-stack) • [Quick Start](#-quick-start) • [API Docs](#-api-endpoints) • [ML Pipeline](#-ml-prediction-pipeline)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Quick Start](#-quick-start)
- [API Endpoints](#-api-endpoints)
- [ML Prediction Pipeline](#-ml-prediction-pipeline)
- [Database Schema](#-database-schema)
- [Usage Examples](#-usage-examples)
- [Future Enhancements](#-future-enhancements)

---

## 🌟 Overview

**Zentra** is a production-ready health analytics platform that combines modern web technologies with machine learning to provide intelligent obesity risk assessment. The backend is built with FastAPI and offers:

- 🔐 **Secure Authentication** - JWT-based auth with password reset functionality
- 👤 **User Profile Management** - Comprehensive health profile tracking with BMI calculation
- 🤖 **ML Predictions** - Random Forest model trained on 2000+ samples with 95%+ accuracy
- 📊 **Prediction History** - Automatic tracking of all predictions with timestamps
- 🗄️ **PostgreSQL Database** - Robust relational database with SQLAlchemy ORM
- 📧 **Email Integration** - Password reset emails via Resend API
- 📚 **Interactive API Docs** - Beautiful Scalar documentation

---

## ✨ Features

### 🔐 Authentication & Security

| Feature | Description |
|---------|-------------|
| **User Registration** | Email-based signup with bcrypt password hashing |
| **JWT Authentication** | Secure token-based authentication with configurable expiry |
| **Password Reset** | Token-based password reset flow with email notifications |
| **Protected Routes** | Middleware-based route protection with current user injection |
| **Session Management** | Stateless authentication with JWT tokens |

### 👤 User Profile Management

| Feature | Description |
|---------|-------------|
| **Profile Creation** | Create comprehensive health profiles with 15+ metrics |
| **Profile Updates** | Partial updates with automatic BMI recalculation |
| **BMI Calculation** | Automatic BMI computation from height and weight |
| **Profile Retrieval** | Get current user's complete health profile |
| **Data Validation** | Pydantic schemas ensure data integrity |

**Profile Metrics Tracked:**
- 📏 Demographics: Gender, Age, Height, Weight, BMI
- 🍽️ Dietary: Vegetable intake, meal frequency, calorie tracking, high-calorie food consumption
- 🏃 Activity: Physical activity hours, screen time, transportation mode
- 🧬 Health History: Family overweight history
- 🚬 Lifestyle: Smoking, alcohol consumption, snacking frequency, water intake

### 🤖 ML-Powered Obesity Prediction

| Feature | Description |
|---------|-------------|
| **Random Forest Classifier** | Pre-trained model with 95%+ accuracy |
| **7 Obesity Categories** | Insufficient Weight, Normal, Overweight I-II, Obesity I-III |
| **15+ Input Features** | Comprehensive lifestyle and health metrics |
| **Automated Preprocessing** | Label encoding, robust scaling, feature engineering |
| **Prediction History** | All predictions saved with input data and timestamps |
| **Real-time Inference** | Fast predictions using joblib-serialized models |

### 🗄️ Database Management

| Model | Description |
|-------|-------------|
| **User** | Email, hashed password, relationships to profiles and predictions |
| **UserHealthProfile** | Complete health profile with 15+ metrics and BMI |
| **PredictionHistory** | Prediction logs with input data, results, and timestamps |
| **PasswordResetToken** | Temporary tokens with expiry for password resets |

---

## 🛠️ Tech Stack

<div align="center">

### Core Technologies

| Layer | Technology | Version | Purpose |
|-------|-----------|---------|---------|
| **Web Framework** | FastAPI | 0.109.0 | High-performance async API framework |
| **Server** | Uvicorn | 0.27.0 | ASGI server with auto-reload |
| **Database** | PostgreSQL | Latest | Production-grade relational database |
| **ORM** | SQLAlchemy | 2.0.25 | Python SQL toolkit and ORM |
| **Migrations** | Alembic | 1.13.1 | Database migration management |

### Security & Authentication

| Technology | Version | Purpose |
|-----------|---------|---------|
| **JWT** | python-jose 3.3.0 | JSON Web Token implementation |
| **Password Hashing** | passlib[bcrypt] 1.7.4 | Secure password hashing |
| **Email Service** | Resend 0.8.0 | Transactional email API |

### Machine Learning

| Technology | Version | Purpose |
|-----------|---------|---------|
| **ML Framework** | scikit-learn 1.4.0 | Random Forest classifier |
| **Data Processing** | pandas 2.2.0 | Data manipulation and analysis |
| **Numerical Computing** | numpy 1.26.3 | Array operations and math |
| **Model Serialization** | joblib 1.3.2 | Efficient model persistence |

### Data Validation & Docs

| Technology | Version | Purpose |
|-----------|---------|---------|
| **Validation** | Pydantic 2.5.3 | Data validation and settings |
| **API Docs** | Scalar FastAPI 1.0.3 | Beautiful interactive documentation |
| **Email Validation** | email-validator 2.1.0 | Email format validation |

</div>

---

## 📁 Project Structure

```bash
zentra/
├── backend/                        # FastAPI Backend
│   ├── app/
│   │   ├── api/                   # API Route Handlers
│   │   │   ├── auth_router.py     # 🔐 Authentication endpoints
│   │   │   ├── profile_router.py  # 👤 User profile CRUD operations
│   │   │   └── prediction_router.py # 🤖 ML prediction endpoint
│   │   │
│   │   ├── core/                  # Core Configuration
│   │   │   ├── config.py          # Environment settings
│   │   │   ├── security.py        # JWT & password utilities
│   │   │   ├── hashing.py         # Password hash wrapper
│   │   │   ├── dependencies.py    # Auth dependencies
│   │   │   └── email_utils.py     # Email service integration
│   │   │
│   │   ├── db/                    # Database Layer
│   │   │   ├── database.py        # SQLAlchemy engine & sessions
│   │   │   └── models.py          # ORM models (User, Profile, Predictions)
│   │   │
│   │   ├── ml/                    # Machine Learning
│   │   │   ├── inference_pipeline.py      # Prediction logic
│   │   │   ├── random_forest_model.pkl    # Trained RF classifier (7.9 MB)
│   │   │   ├── label_encoders.pkl         # Categorical encoders
│   │   │   ├── robust_scaler.pkl          # Feature scaler
│   │   │   ├── target_label_encoder.pkl   # Target encoder
│   │   │   └── feature_columns.pkl        # Feature names
│   │   │
│   │   ├── schemas/               # Pydantic Schemas
│   │   │   ├── auth.py            # Auth request/response models
│   │   │   ├── profile.py         # Profile CRUD schemas
│   │   │   └── predict.py         # Prediction schemas
│   │   │
│   │   ├── services/              # Business Logic
│   │   │   └── auth_service.py    # User creation & authentication
│   │   │
│   │   └── main.py                # 🚀 FastAPI application entry
│   │
│   ├── .env                       # Environment variables (not tracked)
│   ├── .gitignore
│   ├── requirements.txt           # Python dependencies
│   ├── create_tables.py           # Database initialization script
│   └── README.md
│
├── modelnb/                       # ML Development & Training
│   ├── eda.ipynb                  # Exploratory Data Analysis
│   ├── feature_engineering.ipynb  # Feature engineering experiments
│   ├── model_Training.ipynb       # Model training & evaluation
│   ├── inference_pipeline.py      # Standalone inference script
│   ├── ObesityDataSet_raw_and_data_sinthetic.csv
│   ├── obesity_data_cleaned.csv
│   ├── obesity_data_preprocessed.csv
│   └── models/                    # Trained model artifacts
│
└── test.py                        # Quick prediction test script
```

---

## 🚀 Quick Start

### Prerequisites

- **Python** 3.8 or higher
- **PostgreSQL** database server
- **pip** package manager
- **Virtual environment** (recommended)

### Installation

#### 1️⃣ Clone & Navigate

```bash
cd backend
```

#### 2️⃣ Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

#### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

#### 4️⃣ Configure Environment Variables

Create a `.env` file in the `backend/` directory:

```env
# Application Settings
PROJECT_NAME="Zentra ML API"
ENVIRONMENT="development"
APP_HOST="127.0.0.1"
APP_PORT=8000

# Security Configuration
SECRET_KEY="your-secret-key-here-generate-with-openssl-rand-hex-32"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=60

# Database Configuration
DATABASE_URL="postgresql://username:password@localhost:5432/zentra_db"

# Email Service (Optional - for password reset)
RESEND_API_KEY="your-resend-api-key"
```

> **💡 Tip:** Generate a secure secret key using:
> ```bash
> openssl rand -hex 32
> ```

#### 5️⃣ Initialize Database

```bash
# Option 1: Automatic table creation on first run
python create_tables.py

# Option 2: Use Alembic for migrations (recommended for production)
alembic upgrade head
```

#### 6️⃣ Run the Application

```bash
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

#### 7️⃣ Access API Documentation

- **Scalar Docs**: http://127.0.0.1:8000/scalar
- **OpenAPI JSON**: http://127.0.0.1:8000/openapi.json

---

## 🚦 API Endpoints

### 🔐 Authentication Routes (`/auth`)

| Method | Endpoint | Description | Auth Required | Request Body |
|--------|----------|-------------|---------------|--------------|
| `POST` | `/auth/signup` | Register new user | ❌ | `{ email, password }` |
| `POST` | `/auth/login` | Login & get JWT token | ❌ | `{ email, password }` |
| `POST` | `/auth/request-password-reset` | Request password reset | ❌ | `{ email }` |
| `POST` | `/auth/reset-password` | Complete password reset | ❌ | `{ token, new_password }` |
| `GET` | `/auth/me` | Get current user info | ✅ | - |

### 👤 User Profile Routes (`/profile`)

| Method | Endpoint | Description | Auth Required | Request Body |
|--------|----------|-------------|---------------|--------------|
| `POST` | `/profile/create` | Create user health profile | ✅ | Full profile data (15+ fields) |
| `PUT` | `/profile/update` | Update existing profile | ✅ | Partial profile data |
| `GET` | `/profile/me` | Get current user's profile | ✅ | - |

**Profile Fields:**
- `gender`, `age`, `height_m`, `weight_kg` (auto-calculates BMI)
- `family_overweight_history`, `high_calorie_food`
- `vegetable_intake_freq`, `main_meals_per_day`, `snack_frequency`
- `smokes`, `water_intake_liters`, `calorie_tracking`
- `physical_activity_hours`, `screentime_hours`
- `alcohol_consumption`, `travel_mode`

### 🤖 Prediction Routes (`/predict`)

| Method | Endpoint | Description | Auth Required | Request Body |
|--------|----------|-------------|---------------|--------------|
| `POST` | `/predict/` | Predict obesity level | ✅ | Same as profile fields |

**Prediction Output:**
```json
{
  "prediction": "Obesity_Type_I",
  "confidence": 0.87,
  "bmi": 27.55,
  "saved_to_history": true
}
```

### 📚 Documentation Routes

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/scalar` | Interactive Scalar API documentation |
| `GET` | `/docs` | Alternative Swagger UI (if enabled) |
| `GET` | `/openapi.json` | OpenAPI schema JSON |

---

## 🤖 ML Prediction Pipeline

### Model Architecture

```
Input Features (15)
    ↓
Label Encoding (Categorical Features)
    ↓
Robust Scaling (Numerical Features)
    ↓
Random Forest Classifier (100 trees)
    ↓
Output: 7 Obesity Categories
```

### Obesity Categories

| Category | Description | BMI Range |
|----------|-------------|-----------|
| `Insufficient_Weight` | Underweight | < 18.5 |
| `Normal_Weight` | Healthy weight | 18.5 - 24.9 |
| `Overweight_Level_I` | Slightly overweight | 25.0 - 27.4 |
| `Overweight_Level_II` | Moderately overweight | 27.5 - 29.9 |
| `Obesity_Type_I` | Class I obesity | 30.0 - 34.9 |
| `Obesity_Type_II` | Class II obesity | 35.0 - 39.9 |
| `Obesity_Type_III` | Class III obesity (severe) | ≥ 40.0 |

### Model Performance

- **Accuracy**: 95%+ on test set
- **Training Samples**: 2000+ synthetic + real data
- **Features**: 15 lifestyle and health metrics
- **Algorithm**: Random Forest with 100 estimators
- **Preprocessing**: Label encoding + Robust scaling

### Trained Artifacts

| File | Size | Description |
|------|------|-------------|
| `random_forest_model.pkl` | 7.9 MB | Trained Random Forest classifier |
| `label_encoders.pkl` | 1.4 KB | Encoders for categorical features |
| `robust_scaler.pkl` | 1.0 KB | Scaler for numerical features |
| `target_label_encoder.pkl` | 608 B | Encoder for target labels |
| `feature_columns.pkl` | 517 B | Feature column names |

---

## 🗄️ Database Schema

### Entity Relationship Diagram

```
┌─────────────────┐
│      User       │
├─────────────────┤
│ id (PK)         │
│ email (UNIQUE)  │
│ hashed_password │
└────────┬────────┘
         │
         ├──────────────────────────────────┐
         │                                  │
         ▼                                  ▼
┌──────────────────────┐      ┌──────────────────────────┐
│ UserHealthProfile    │      │   PredictionHistory      │
├──────────────────────┤      ├──────────────────────────┤
│ id (PK)              │      │ id (PK)                  │
│ user_id (FK, UNIQUE) │      │ user_id (FK)             │
│ gender               │      │ input_data (JSON)        │
│ age                  │      │ prediction               │
│ height_m             │      │ created_at               │
│ weight_kg            │      └──────────────────────────┘
│ bmi (computed)       │
│ family_overweight... │
│ high_calorie_food    │
│ vegetable_intake...  │
│ main_meals_per_day   │
│ snack_frequency      │
│ smokes               │
│ water_intake_liters  │
│ calorie_tracking     │
│ physical_activity... │
│ screentime_hours     │
│ alcohol_consumption  │
│ travel_mode          │
│ updated_at           │
└──────────────────────┘
```

---

## 📖 Usage Examples

### 1. User Registration & Authentication

```bash
# Register a new user
curl -X POST "http://127.0.0.1:8000/auth/signup" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "john.doe@example.com",
    "password": "SecurePass123!"
  }'

# Response
{
  "id": 1,
  "email": "john.doe@example.com"
}
```

```bash
# Login to get JWT token
curl -X POST "http://127.0.0.1:8000/auth/login" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "john.doe@example.com",
    "password": "SecurePass123!"
  }'

# Response
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

### 2. Create User Health Profile

```bash
curl -X POST "http://127.0.0.1:8000/profile/create" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "gender": "Male",
    "age": 28,
    "height_m": 1.75,
    "weight_kg": 82,
    "family_overweight_history": "yes",
    "high_calorie_food": "yes",
    "vegetable_intake_freq": 2,
    "main_meals_per_day": 3,
    "snack_frequency": "Sometimes",
    "smokes": "no",
    "water_intake_liters": 2.5,
    "calorie_tracking": "no",
    "physical_activity_hours": 1.5,
    "screentime_hours": 6,
    "alcohol_consumption": "Sometimes",
    "travel_mode": "Car"
  }'

# Response
{
  "id": 1,
  "user_id": 1,
  "gender": "Male",
  "age": 28,
  "height_m": 1.75,
  "weight_kg": 82,
  "bmi": 26.78,
  ...
}
```

### 3. Update Profile

```bash
# Update only specific fields
curl -X PUT "http://127.0.0.1:8000/profile/update" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "weight_kg": 78,
    "physical_activity_hours": 3
  }'

# BMI is automatically recalculated
```

### 4. Get Obesity Prediction

```bash
curl -X POST "http://127.0.0.1:8000/predict/" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "gender": "Female",
    "age": 32,
    "height_m": 1.62,
    "weight_kg": 68,
    "family_overweight_history": "no",
    "high_calorie_food": "no",
    "vegetable_intake_freq": 3,
    "main_meals_per_day": 3,
    "snack_frequency": "no",
    "smokes": "no",
    "water_intake_liters": 2,
    "calorie_tracking": "yes",
    "physical_activity_hours": 2,
    "screentime_hours": 3,
    "alcohol_consumption": "no",
    "travel_mode": "Walking"
  }'

# Response
{
  "prediction": "Normal_Weight",
  "bmi": 25.91,
  "confidence": 0.92,
  "saved_to_history": true
}
```

### 5. Password Reset Flow

```bash
# Step 1: Request password reset
curl -X POST "http://127.0.0.1:8000/auth/request-password-reset" \
  -H "Content-Type: application/json" \
  -d '{"email": "john.doe@example.com"}'

# User receives email with reset token

# Step 2: Reset password with token
curl -X POST "http://127.0.0.1:8000/auth/reset-password" \
  -H "Content-Type: application/json" \
  -d '{
    "token": "abc123def456",
    "new_password": "NewSecurePass456!"
  }'
```

---

## 🔮 Future Enhancements

### Planned Features

- [ ] **Prediction History Endpoint** - Retrieve user's past predictions with filtering
- [ ] **Analytics Dashboard** - Visualize BMI trends and prediction history
- [ ] **LLM Health Assistant** - AI-powered health recommendations using GPT-4
- [ ] **Personalized Recommendations** - Custom diet and exercise plans
- [ ] **Weekly Health Reports** - Email summaries with insights
- [ ] **Multi-Model Support** - Add Logistic Regression, XGBoost, Neural Networks
- [ ] **Batch Predictions** - Process multiple predictions in one request
- [ ] **Export Functionality** - Download prediction history as CSV/PDF
- [ ] **Social Features** - Share progress with friends and family
- [ ] **Mobile App Integration** - React Native or Flutter frontend
- [ ] **Webhook Support** - Real-time notifications for predictions
- [ ] **Rate Limiting** - API rate limiting with Redis
- [ ] **Caching Layer** - Redis cache for frequent queries
- [ ] **Monitoring** - Prometheus + Grafana dashboards
- [ ] **CI/CD Pipeline** - Automated testing and deployment

### Potential Integrations

- **Fitness Trackers**: Fitbit, Apple Health, Google Fit
- **Nutrition APIs**: Nutritionix, Edamam
- **Telemedicine**: Integration with healthcare providers
- **Insurance**: Health insurance risk assessment

---

## 🧪 Development & Testing

### Running Tests

```bash
# Install test dependencies
pip install pytest pytest-asyncio httpx

# Run all tests
pytest

# Run with coverage
pytest --cov=app --cov-report=html
```

### Database Migrations

```bash
# Create a new migration
alembic revision --autogenerate -m "Add new field"

# Apply migrations
alembic upgrade head

# Rollback migration
alembic downgrade -1
```

### Code Quality

```bash
# Format code with black
black app/

# Lint with flake8
flake8 app/

# Type checking with mypy
mypy app/
```

---

## 📄 License

This project is part of the **Zentra Health Analytics Platform**.  
© 2024 Fahad Khan. All rights reserved.

---

## 🤝 Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Code Standards

- Follow PEP 8 style guidelines
- Write docstrings for all functions
- Add type hints where applicable
- Ensure all tests pass before submitting PR
- Update documentation for new features

---

## 📞 Support

For questions or issues:

- **Email**: fahad.khan@example.com
- **GitHub Issues**: [Create an issue](https://github.com/yourusername/zentra/issues)
- **Documentation**: http://127.0.0.1:8000/scalar

---

## 🙏 Acknowledgments

- **FastAPI** - For the amazing web framework
- **scikit-learn** - For powerful ML tools
- **PostgreSQL** - For robust database management
- **Obesity Dataset** - UCI Machine Learning Repository

---

<div align="center">

### ⭐ Star this repo if you find it helpful!

**Built with ❤️ by Fahad Khan using FastAPI, PostgreSQL, and Machine Learning**

![Python](https://img.shields.io/badge/Made%20with-Python-blue?style=flat-square&logo=python)
![FastAPI](https://img.shields.io/badge/Powered%20by-FastAPI-009688?style=flat-square&logo=fastapi)
![ML](https://img.shields.io/badge/ML-scikit--learn-F7931E?style=flat-square&logo=scikit-learn)

</div>
