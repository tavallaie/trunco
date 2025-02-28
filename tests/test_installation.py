import sys
import importlib


def check_module_location(module_name):
    try:
        module = importlib.import_module(module_name)
        print(f"{module_name} is at {module.__file__}")
        if hasattr(module, "__path__"):
            print(f"  Path: {module.__path__}")
    except ImportError as e:
        print(f"Could not import {module_name}: {e}")


check_module_location("trunco.html")
check_module_location("trunco.franken")
