# test_namespace_detailed.py
import sys
from importlib import metadata

print("Python Path:")
for path in sys.path:
    print(f"  - {path}")

# Try importing trunco.html
try:
    from trunco import html

    print("\nSuccessfully imported from trunco import html")
    print(f"  Module location: {html.__file__}")
except ImportError as e:
    print(f"\nFailed to import from trunco import html: {e}")

# Try importing trunco.franken
try:
    from trunco import franken

    print("\nSuccessfully imported from trunco import franken")
    print(f"  Module location: {franken.__file__}")
except ImportError as e:
    print(f"\nFailed to from trunco import franken: {e}")

# Try looking for installed distributions
print("\nChecking for installed modules:")
for dist in metadata.distributions():
    # Attempt to get the distribution name from metadata, falling back to dist.name if needed.
    name = (
        dist.metadata.get("Name")
        if dist.metadata.get("Name")
        else getattr(dist, "name", None)
    )
    if name and "trunco" in name.lower():
        print(f"  Found distribution: {name}")
