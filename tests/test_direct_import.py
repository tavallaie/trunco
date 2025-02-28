# test_direct_import.py
import sys
import os

# Add the src directories directly to the path
sys.path.insert(
    0, os.path.join(os.path.dirname(__file__), "../packages/trunco-core/src")
)
sys.path.insert(
    0, os.path.join(os.path.dirname(__file__), "../packages/trunco-franken/src")
)

# Now try imports
try:
    from trunco import html

    print("Successfully imported trunco.html")
    print(f"  Module location: {html.__file__}")

    from trunco import franken

    print("Successfully imported trunco.franken")
    print(f"  Module location: {franken.__file__}")

except ImportError as e:
    print(f"Import failed: {e}")
