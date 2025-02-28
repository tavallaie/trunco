#!/usr/bin/env python3
import traceback


def safe_import(step, code):
    """
    Execute an import statement (provided as a string) with a label.
    If the import fails, print the step description and the full traceback.
    """
    print(f"Step: {step} - Executing: {code}")
    try:
        exec(code, globals())
    except Exception as e:
        print(f"Error during step: {step}")
        traceback.print_exc()
        raise


def main():
    try:
        # Import html module from the namespace.
        safe_import("Importing 'html' from trunco", "from trunco import html")
        # print(f"Imported html: {html}")

        # Import franken module from the namespace.
        safe_import("Importing 'franken' from trunco", "from trunco import franken")
        # print(f"Imported franken: {franken}")

        # # Import the overall namespace.
        # safe_import("Importing 'trunco' namespace", "import trunco")
        # print("trunco __spec__:", trunco.__spec__)
        # print("trunco __file__:", getattr(trunco, "__file__", None))

        print("Namespace setup is correct!")
    except Exception as e:
        print("Namespace setup failed:", e)


if __name__ == "__main__":
    main()
