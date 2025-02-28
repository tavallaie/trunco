import sys
import pkgutil

print("Python Path:")
for path in sys.path:
    print(f"  - {path}")

print("\nTrying to find trunco packages:")

for finder, name, ispkg in pkgutil.iter_modules():
    if name.startswith("trunco"):
        print(f"Found module: {name}, is package: {ispkg}")
        print(f"  Path: {finder.path}")

print("\nTrying alternative import approaches:")
try:
    import trunco

    print("Direct trunco import works")
    print(
        f"  trunco.__path__: {trunco.__path__ if hasattr(trunco, '__path__') else 'Not a package'}"
    )

    try:
        import trunco.html

        print("  trunco.html import works")
    except ImportError as e:
        print(f"  trunco.html import fails: {e}")

    try:
        import trunco.franken

        print("  trunco.franken import works")
    except ImportError as e:
        print(f"  trunco.franken import fails: {e}")
except ImportError as e:
    print(f"Direct trunco import fails: {e}")
