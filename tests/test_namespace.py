# test_namespace_detailed.py
import sys
import os
import importlib

print("Python Path:")
for path in sys.path:
    print(f"  - {path}")

try:
    import trunco

    print("\nSuccessfully imported trunco namespace")
    print(
        f"  trunco.__path__: {trunco.__path__ if hasattr(trunco, '__path__') else 'Not a package'}"
    )

    try:
        import trunco.html

        print("\nSuccessfully imported trunco.html")
        print(f"  Module location: {trunco.html.__file__}")
    except ImportError as e:
        print(f"\nFailed to import trunco.html: {e}")

    try:
        import trunco.franken

        print("\nSuccessfully imported trunco.franken")
        print(f"  Module location: {trunco.franken.__file__}")
    except ImportError as e:
        print(f"\nFailed to import trunco.franken: {e}")

except ImportError as e:
    print(f"\nFailed to import trunco: {e}")

    # Try looking for installed modules
    print("\nChecking for installed modules:")
    for finder, name, ispkg in importlib.metadata.distributions():
        if "trunco" in name.lower():
            print(f"  Found distribution: {name}")
