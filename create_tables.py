"""
Utility script to create database tables based on SQLAlchemy models.
Run this script to sync your database schema with your models.
"""
from app.db.database import Base, engine
from app.db.models import User, PredictionHistory, passwordResetToken, UserProfile, UserHealthProfile

def create_tables():
    """Create all tables defined in models."""
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("✓ All tables created successfully!")

if __name__ == "__main__":
    create_tables()
