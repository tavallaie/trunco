#!/usr/bin/env python3
import os
import re
import sys
import keyword
from pathlib import Path

# Regular expression to match class definitions in a Python file.
CLASS_REGEX = re.compile(r"^\s*class\s+(\w+)", re.MULTILINE)


def ensure_empty_init(directory: Path):
    """
    Ensure that the given directory contains an __init__.py file.
    If it doesn't exist, create one with an auto-generated comment.
    """
    init_path = directory / "__init__.py"
    if not init_path.exists():
        try:
            init_path.write_text(
                "# Auto-generated empty __init__.py\n", encoding="utf-8"
            )
            print(f"Created empty __init__.py in {directory}")
        except Exception as e:
            print(f"Failed to create {init_path}: {e}", file=sys.stderr)


def build_static_init_for_module(module_dir: Path):
    """
    Generate a static __init__.py file in the given module directory.

    - Process all .py files (excluding __init__.py) in this directory to generate import lines
      for class definitions.
      * For each class:
          - If its name ends with "Component", import it with an alias (name without the suffix)
            provided the alias is non-empty and not a reserved keyword.
          - Otherwise, import the class normally.
    - Then, if there is an immediate subdirectory named "components" that contains .py files:
          - Recursively process that subdirectory.
          - Add a single import line:  from . import components
          - Add "components" to the exports.
    - Prepend a snippet to set __path__ explicitly.
    - Finally, if there are any exports, append an __all__ list.
    """
    init_file = module_dir / "__init__.py"
    # Set __path__ to the module's own directory to avoid namespace ambiguity.
    header = [
        "# Auto-generated __init__.py for " + str(module_dir),
        "",
    ]
    import_lines = header.copy()
    exports = set()

    # Process all .py files (non-recursively) in module_dir.
    for py_file in sorted(module_dir.glob("*.py")):
        if py_file.name == "__init__.py":
            continue

        module_name = py_file.stem  # filename without .py extension
        try:
            content = py_file.read_text(encoding="utf-8")
        except Exception as e:
            print(f"Error reading {py_file}: {e}", file=sys.stderr)
            continue

        classes = CLASS_REGEX.findall(content)
        if classes:
            for cls in classes:
                if cls.endswith("Component"):
                    alias = cls[: -len("Component")]
                    if alias and not keyword.iskeyword(alias):
                        line = f"from .{module_name} import {cls} as {alias}"
                        exports.add(alias)
                    else:
                        line = f"from .{module_name} import {cls}"
                        exports.add(cls)
                else:
                    line = f"from .{module_name} import {cls}"
                    exports.add(cls)
                import_lines.append(line)
        else:
            # If no class definitions, import everything from the module.
            line = f"from .{module_name} import *"
            import_lines.append(line)
            exports.add(module_name)
        import_lines.append("")

    # Process immediate subdirectory named "components" only.
    components_dir = module_dir / "components"
    if components_dir.is_dir() and any(components_dir.glob("*.py")):
        # Recursively process its __init__.py.
        build_static_init_for_module(components_dir)
        line = "from . import components"
        import_lines.append(line)
        exports.add("components")
        import_lines.append("")

    # Append __all__ if there are exports.
    if exports:
        import_lines.append("__all__ = [")
        for name in sorted(exports):
            import_lines.append(f"    '{name}',")
        import_lines.append("]")
    else:
        import_lines.append("# No exports found.")

    try:
        init_file.write_text("\n".join(import_lines), encoding="utf-8")
        print(f"Generated __init__.py at {init_file}")
    except Exception as e:
        print(f"Failed to write {init_file}: {e}", file=sys.stderr)


def process_package(package_path: Path):
    """
    For a given workspace package (e.g. packages/{package_name}),
    process its namespace directory at:
      {package_path}/src/trunco
    IMPORTANT: Do not generate an __init__.py in the top-level namespace directory
    (to allow native namespace merging).
    Then, for each immediate subdirectory (representing a module), generate/update its __init__.py.
    """
    namespace_dir = package_path / "src" / "trunco"
    if not namespace_dir.is_dir():
        print(f"No 'src/trunco' directory found in {package_path}", file=sys.stderr)
        return

    # Remove the __init__.py in the top-level namespace (if it exists) to enable native namespace.
    top_init = namespace_dir / "__init__.py"
    if top_init.exists():
        top_init.unlink()
        print(
            f"Removed top-level __init__.py at {top_init} to enable native namespace merging."
        )

    # Process each immediate subdirectory (module) in the namespace directory.
    for module_dir in sorted(namespace_dir.iterdir()):
        if module_dir.is_dir():
            print(f"Processing module {module_dir}")
            build_static_init_for_module(module_dir)


def main():
    # Assume the repository root has a "packages" directory.
    base_packages = Path(__file__).resolve().parent.parent / "packages"
    if not base_packages.is_dir():
        print("No 'packages' directory found.", file=sys.stderr)
        sys.exit(1)
    for pkg in sorted(base_packages.iterdir()):
        if pkg.is_dir():
            print(f"Processing workspace package: {pkg.name}")
            process_package(pkg)


if __name__ == "__main__":
    main()
