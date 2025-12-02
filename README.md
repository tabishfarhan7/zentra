# 🚀 Zentra ML API — Backend

**FastAPI • PostgreSQL • JWT Auth • ML Prediction Pipeline**

Zentra is a comprehensive health analytics and obesity prediction platform. This backend handles user authentication, JWT-based authorization, database management, and machine learning-powered obesity level predictions based on lifestyle and health metrics.

---

## 📁 Project Structure

```bash
backend/
├── app/
│   ├── api/
│   │   ├── auth_router.py          # Authentication & password reset endpoints
│   │   └── prediction_router.py    # ML prediction endpoint
│   │
│   ├── core/
│   │   ├── config.py               # Application settings & environment config
│   │   ├── security.py             # JWT token & password hashing utilities
│   │   ├── hashing.py              # Password hash wrapper class
│   │   ├── dependencies.py         # Auth dependencies & current user resolver
│   │   └── email_utils.py          # Email service integration (Resend)
│   │
│   ├── db/
│   │   ├── database.py             # SQLAlchemy engine & session management
│   │   └── models.py               # Database models (User, PredictionHistory, PasswordResetToken)
│   │
│   ├── ml/
│   │   ├── inference_pipeline.py   # ML preprocessing & prediction logic
│   │   └── *.pkl                   # Trained models & encoders
│   │
│   ├── schemas/
│   │   ├── auth.py                 # Auth request/response schemas
│   │   └── predict.py              # Prediction request/response schemas
│   │
│   ├── services/
│   │   └── auth_service.py         # User creation & authentication logic
│   │
│   └── main.py                     # FastAPI application entry point
│
├── .env                            # Environment variables (not tracked)
├── .gitignore
├── requirements.txt                # Python dependencies
└── README.md
```

---

## ✅ Features Implemented

### 🔐 User Authentication & Authorization
- **User Signup** - Email-based registration with secure password hashing
- **User Login** - JWT token-based authentication
- **Password Reset Flow** - Token-based password reset with expiry
- **Protected Routes** - JWT validation for secure endpoints
- **Current User Endpoint** - Retrieve authenticated user information

### 🤖 ML-Powered Obesity Prediction
- **Obesity Level Classification** - Predicts obesity category based on:
  - Demographics (age, gender, height, weight)
  - Family history & lifestyle factors
  - Dietary habits (vegetable intake, meal frequency, calorie tracking)
  - Physical activity & screen time
  - Behavioral patterns (smoking, alcohol, transportation mode)
- **Prediction History** - Automatically saves all predictions with timestamps
- **Random Forest Model** - Pre-trained classifier with robust preprocessing

### 🗄️ Database Management (PostgreSQL)
- **User Model** - Stores user credentials & relationships
- **Prediction History** - Tracks all user predictions with input data
- **Password Reset Tokens** - Manages temporary reset tokens with expiry
- **Automatic Table Creation** - SQLAlchemy ORM handles schema

---

## 🛠️ Tech Stack

| Category | Technology |
|----------|-----------|
| **Web Framework** | FastAPI |
| **Database** | PostgreSQL |
| **ORM** | SQLAlchemy |
| **Authentication** | JWT (python-jose) |
| **Password Hashing** | bcrypt (passlib) |
| **Data Validation** | Pydantic |
| **ML Framework** | scikit-learn (Random Forest) |
| **Server** | Uvicorn |
| **API Docs** | Scalar FastAPI |
| **Email Service** | Resend |

---

## 🚦 API Endpoints

### Authentication (`/auth`)

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| `POST` | `/auth/signup` | Register new user | ❌ |
| `POST` | `/auth/login` | Login & get JWT token | ❌ |
| `POST` | `/auth/request-password-reset` | Request password reset token | ❌ |
| `POST` | `/auth/reset-password` | Complete password reset | ❌ |
| `GET` | `/auth/me` | Get current user info | ✅ |

### Predictions (`/predict`)

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| `POST` | `/predict/` | Predict obesity level | ✅ |

### Documentation

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/scalar` | Interactive API documentation |

---

## ⚙️ Setup & Installation

### Prerequisites
- Python 3.10+
- PostgreSQL database
- Virtual environment (recommended)

### 1. Clone & Navigate
```bash
cd backend
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the `backend/` directory:

```env
# Application
PROJECT_NAME="Zentra ML API"
ENVIRONMENT="development"
APP_HOST="127.0.0.1"
APP_PORT=8000

# Security
SECRET_KEY="your-secret-key-here-generate-with-openssl-rand-hex-32"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=60

# Database
DATABASE_URL="postgresql://username:password@localhost:5432/zentra_db"

# Email (Optional - for password reset emails)
RESEND_API_KEY="your-resend-api-key"
```

### 5. Initialize Database
```bash
# Create tables automatically on first run
# Or use Alembic for migrations (recommended for production)
```

### 6. Run the Application
```bash
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

### 7. Access API Documentation
- **Scalar Docs**: http://127.0.0.1:8000/scalar
- **OpenAPI JSON**: http://127.0.0.1:8000/openapi.json

---

## 🧪 Testing the API

### Example: User Signup
```bash
curl -X POST "http://127.0.0.1:8000/auth/signup" \
  -H "Content-Type: application/json" \
  -d '{"email": "user@example.com", "password": "securepassword123"}'
```

### Example: Login
```bash
curl -X POST "http://127.0.0.1:8000/auth/login" \
  -H "Content-Type: application/json" \
  -d '{"email": "user@example.com", "password": "securepassword123"}'
```

### Example: Predict Obesity Level
```bash
curl -X POST "http://127.0.0.1:8000/predict/" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "gender": "Male",
    "age": 25,
    "height_m": 1.75,
    "weight_kg": 85,
    "family_overweight_history": "yes",
    "high_calorie_food": "yes",
    "vegetable_intake_freq": 2,
    "main_meals_per_day": 3,
    "snack_frequency": "Sometimes",
    "smokes": "no",
    "water_intake_liters": 2,
    "calorie_tracking": "no",
    "physical_activity_hours": 1,
    "screentime_hours": 5,
    "alcohol_consumption": "no",
    "travel_mode": "Public_Transportation"
  }'
```

---

## � Future Enhancements

- [ ] User dashboard with prediction analytics
- [ ] Prediction history retrieval endpoint
- [ ] LLM-powered health assistant
- [ ] Personalized activity recommendations
- [ ] Diet tips & weekly insights
- [ ] Email notifications for password resets
- [ ] Multi-model support (Logistic Regression, XGBoost)
- [ ] Batch prediction capabilities
- [ ] Export prediction history (CSV/PDF)

---

## 📝 License

This project is part of the Zentra health analytics platform.

---

## 🤝 Contributing

Contributions are welcome! Please ensure all tests pass and follow the existing code structure.

---

**Built with ❤️ by fahad khan using FastAPI and Machine Learning**

