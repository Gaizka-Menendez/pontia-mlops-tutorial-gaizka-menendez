# conftest.py
import sys
import os

# Agrega la carpeta raíz del proyecto al sys.path para que pytest pueda encontrar los módulos
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))