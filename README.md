<div align="center">

# 🚀 Zentra AI Platform

### *Intelligent AI Assistant with ML-Powered Analytics*

[![FastAPI](https://img.shields.io/badge/FastAPI-0.109.0-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.4.0-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![JWT](https://img.shields.io/badge/JWT-Authentication-000000?style=for-the-badge&logo=JSON%20web%20tokens&logoColor=white)](https://jwt.io/)

**A comprehensive AI platform backend featuring JWT authentication, user profile management, and ML-powered analytics using Random Forest classification.**

</div>

---

## 🌟 Overview

**Zentra** is a production-ready AI platform backend built with FastAPI, designed to power intelligent chat assistants and ML-driven analytics. The system provides a robust foundation for building conversational AI applications with secure authentication, user management, and machine learning capabilities.

### Core Capabilities

- **JWT Authentication** - Secure token-based authentication with password reset functionality
- **User Profile System** - Comprehensive user data management with automatic validation
- **ML Inference Pipeline** - Random Forest classifier with 95%+ accuracy for predictive analytics
- **Prediction History** - Automatic tracking and storage of all ML predictions
- **PostgreSQL Database** - Production-grade relational database with SQLAlchemy ORM
- **Email Integration** - Transactional emails via Resend API
- **Interactive API Documentation** - Auto-generated Scalar documentation

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

## 💡 Key Features

<table>
<tr>
<td width="50%">

### 🔐 Authentication & Security
- Email-based user registration
- JWT token generation and validation
- Secure password hashing with bcrypt
- Token-based password reset flow
- Protected route middleware
- Stateless session management

</td>
<td width="50%">

### 👤 User Management
- Create and update user profiles
- Automatic data validation
- BMI auto-calculation
- Profile retrieval endpoints
- Comprehensive user metrics (15+ fields)
- Timestamp tracking

</td>
</tr>
<tr>
<td width="50%">

### 🤖 Machine Learning
- Random Forest classifier (95%+ accuracy)
- 7-category classification system
- Real-time inference pipeline
- Automated preprocessing (encoding, scaling)
- Model artifact serialization
- Prediction history logging

</td>
<td width="50%">

### 🗄️ Database Architecture
- PostgreSQL with SQLAlchemy ORM
- User authentication model
- User health profile model
- Prediction history model
- Password reset token model
- Alembic migration support

</td>
</tr>
</table>

---

## 🛠️ Technology Stack

### Backend Framework
| Component | Technology | Version |
|-----------|-----------|---------|
| Web Framework | FastAPI | 0.109.0 |
| ASGI Server | Uvicorn | 0.27.0 |
| API Documentation | Scalar FastAPI | 1.0.3 |

### Database & ORM
| Component | Technology | Version |
|-----------|-----------|---------|
| Database | PostgreSQL | Latest |
| ORM | SQLAlchemy | 2.0.25 |
| Migrations | Alembic | 1.13.1 |
| Driver | psycopg2-binary | 2.9.9 |

### Security
| Component | Technology | Version |
|-----------|-----------|---------|
| JWT | python-jose[cryptography] | 3.3.0 |
| Password Hashing | passlib[bcrypt] | 1.7.4 |
| Email Service | Resend | 0.8.0 |

### Machine Learning
| Component | Technology | Version |
|-----------|-----------|---------|
| ML Framework | scikit-learn | 1.4.0 |
| Data Processing | pandas | 2.2.0 |
| Numerical Computing | numpy | 1.26.3 |
| Model Serialization | joblib | 1.3.2 |

### Data Validation
| Component | Technology | Version |
|-----------|-----------|---------|
| Schema Validation | Pydantic | 2.5.3 |
| Settings Management | pydantic-settings | 2.1.0 |
| Email Validation | email-validator | 2.1.0 |

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- PostgreSQL database
- pip package manager
- Virtual environment (recommended)

### Installation Steps

**1. Navigate to Backend Directory**
```bash
cd backend
```

**2. Create Virtual Environment**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

**3. Install Dependencies**
```bash
pip install -r requirements.txt
```

**4. Configure Environment Variables**

Create `.env` file in `backend/` directory:

```env
# Application
PROJECT_NAME="Zentra AI Platform"
ENVIRONMENT="development"
APP_HOST="127.0.0.1"
APP_PORT=8000

# Security
SECRET_KEY="your-secret-key-here"  # Generate with: openssl rand -hex 32
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=60

# Database
DATABASE_URL="postgresql://username:password@localhost:5432/zentra_db"

# Email (Optional)
RESEND_API_KEY="your-resend-api-key"
```

**5. Initialize Database**
```bash
# Automatic table creation
python create_tables.py

# OR use Alembic migrations (production)
alembic upgrade head
```

**6. Run Application**
```bash
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

**7. Access API Documentation**
- **Scalar Docs**: http://127.0.0.1:8000/scalar
- **OpenAPI Schema**: http://127.0.0.1:8000/openapi.json

---

## 🔌 API Endpoints

### 🔐 Authentication Routes (`/auth`)

| Method | Endpoint | Description | Auth | Body |
|--------|----------|-------------|------|------|
| POST | `/auth/signup` | Register new user | No | `{ email, password }` |
| POST | `/auth/login` | Get JWT token | No | `{ email, password }` |
| POST | `/auth/request-password-reset` | Request reset token | No | `{ email }` |
| POST | `/auth/reset-password` | Reset password | No | `{ token, new_password }` |
| GET | `/auth/me` | Get current user | Yes | - |

### 👤 User Profile Routes (`/profile`)

| Method | Endpoint | Description | Auth | Body |
|--------|----------|-------------|------|------|
| POST | `/profile/create` | Create user profile | Yes | Full profile data |
| PUT | `/profile/update` | Update profile | Yes | Partial profile data |
| GET | `/profile/me` | Get user profile | Yes | - |

**Profile Fields**: `gender`, `age`, `height_m`, `weight_kg`, `family_overweight_history`, `high_calorie_food`, `vegetable_intake_freq`, `main_meals_per_day`, `snack_frequency`, `smokes`, `water_intake_liters`, `calorie_tracking`, `physical_activity_hours`, `screentime_hours`, `alcohol_consumption`, `travel_mode`

### 🤖 Prediction Routes (`/predict`)

| Method | Endpoint | Description | Auth | Body |
|--------|----------|-------------|------|------|
| POST | `/predict/` | Get ML prediction | Yes | Same as profile fields |

**Response Format**:
```json
{
  "prediction": "Category_Name",
  "confidence": 0.87,
  "bmi": 27.55,
  "saved_to_history": true
}
```

### 📚 Documentation Routes

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/scalar` | Interactive API docs |
| GET | `/openapi.json` | OpenAPI schema |

---

## 🤖 ML Pipeline Architecture

### Inference Flow

```
Input Data (15 features)
    ↓
Label Encoding (categorical variables)
    ↓
Robust Scaling (numerical features)
    ↓
Random Forest Classifier (100 estimators)
    ↓
Prediction Output (7 categories)
```

### Model Specifications

- **Algorithm**: Random Forest Classifier
- **Estimators**: 100 trees
- **Accuracy**: 95%+ on test set
- **Training Data**: 2000+ samples
- **Features**: 15 input variables
- **Output Classes**: 7 categories

### Serialized Artifacts

| File | Size | Purpose |
|------|------|---------|
| `random_forest_model.pkl` | 7.9 MB | Trained classifier |
| `label_encoders.pkl` | 1.4 KB | Categorical encoders |
| `robust_scaler.pkl` | 1.0 KB | Feature scaler |
| `target_label_encoder.pkl` | 608 B | Target encoder |
| `feature_columns.pkl` | 517 B | Feature names |

---

## 🗄️ Database Schema

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
│ [15+ health fields]  │
│ updated_at           │
└──────────────────────┘
```

---

## 📖 Usage Examples

### 1. User Registration & Authentication

```bash
# Register
curl -X POST "http://127.0.0.1:8000/auth/signup" \
  -H "Content-Type: application/json" \
  -d '{"email": "user@example.com", "password": "SecurePass123!"}'

# Login
curl -X POST "http://127.0.0.1:8000/auth/login" \
  -H "Content-Type: application/json" \
  -d '{"email": "user@example.com", "password": "SecurePass123!"}'
```

### 2. Profile Management

```bash
# Create Profile
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

# Update Profile
curl -X PUT "http://127.0.0.1:8000/profile/update" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"weight_kg": 78, "physical_activity_hours": 3}'
```

### ML Prediction

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
```

---

## 🔮 Roadmap

### Planned Features

**AI & Chat Capabilities**
- [ ] LLM Integration (GPT-4, Claude, Gemini)
- [ ] Conversational AI Assistant
- [ ] Context-aware chat responses
- [ ] Multi-turn conversation handling
- [ ] Chat history persistence

**Analytics & Insights**
- [ ] Prediction history retrieval API
- [ ] Analytics dashboard backend
- [ ] Data visualization endpoints
- [ ] Trend analysis algorithms
- [ ] Personalized recommendations engine

**Infrastructure**
- [ ] Redis caching layer
- [ ] Rate limiting middleware
- [ ] WebSocket support for real-time chat
- [ ] Batch prediction endpoints
- [ ] Export functionality (CSV/PDF)

**Integrations**
- [ ] Third-party API connectors
- [ ] Webhook support
- [ ] OAuth2 providers (Google, GitHub)
- [ ] Mobile app backend support

**DevOps**
- [ ] Docker containerization
- [ ] CI/CD pipeline
- [ ] Prometheus monitoring
- [ ] Grafana dashboards
- [ ] Automated testing suite

---

## 🧪 Development

### Testing

```bash
pip install pytest pytest-asyncio httpx
pytest
pytest --cov=app --cov-report=html
```

### Database Migrations

```bash
alembic revision --autogenerate -m "Description"
alembic upgrade head
alembic downgrade -1
```

### Code Quality

```bash
black app/
flake8 app/
mypy app/
```

---

## 📄 License

© 2024 Fahad Khan. All rights reserved.

---

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/name`)
3. Commit changes (`git commit -m 'Add feature'`)
4. Push to branch (`git push origin feature/name`)
5. Open Pull Request

**Code Standards**: PEP 8, type hints, docstrings, tests required

---

## 📞 Contact

- **Email**: fahad.khan@example.com
- **GitHub Issues**: [Create an issue](https://github.com/yourusername/zentra/issues)
- **Documentation**: http://127.0.0.1:8000/scalar

---

<div align="center">

**Built with FastAPI, PostgreSQL, and Machine Learning**

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=flat-square&logo=postgresql&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)

</div>
