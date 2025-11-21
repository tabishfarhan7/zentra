# 🚀 Zentra ML API — Backend

FastAPI • PostgreSQL • JWT Auth • ML Prediction Pipeline

This repository contains the backend for **Zentra**, a health analytics + obesity prediction platform.  
It handles user authentication, JWT, database models, and will later support ML predictions and user dashboards.



## 📁 Project Structure

```bash
backend/
│── app/
│   │── api/
│   │   │── auth_router.py
│   │   │── prediction_router.py
│   │
│   │── core/
│   │   │── config.py
│   │   │── security.py
│   │   │── dependencies.py
│   │
│   │── db/
│   │   │── database.py
│   │   │── models.py
│   │   │── init_db.py
│   │
│   │── schemas/
│   │   │── auth.py
│   │   │── prediction.py
│   │
│   │── services/
│   │   │── auth_service.py
│   │   │── prediction_service.py
│
│── main.py
│── .env
│── requirements.txt
│── README.md

---
```
## 🔧 Features Implemented

### ✅ User Authentication
- Signup  
- Login  
- Secure password hashing using **bcrypt**

### ✅ JWT Token Auth
- Access tokens  
- Token validation  
- Protected routes using dependencies

### ✅ Database (PostgreSQL + SQLAlchemy)
- User model  
- Prediction history model  
- Auto table creation

### 🔜 Coming Soon
- ML Prediction endpoint  
- User dashboard analytics  
- Full obesity prediction pipeline  
- LLM-powered health assistant  
- Activity recommendations, diet tips, weekly insights

---

## 🛠️ Tech Stack

- **FastAPI**
- **PostgreSQL**
- **SQLAlchemy ORM**
- **bcrypt / passlib**
- **python-jose (JWT)**
- **Uvicorn**

---


