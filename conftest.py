import sys
import os

# Исправление ошибки allure - не видит модуль services
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))