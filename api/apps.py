from django.apps import AppConfig
from django.conf import settings
import joblib
import os


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
    MODEL_FILE = os.path.join(settings.MODELS, "employ_model.joblib")
    
    model = joblib.load(MODEL_FILE)
