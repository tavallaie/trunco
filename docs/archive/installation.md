 # Installation Guide

 This document will help you install **Trunco** and get it set up in your Python environment.

 ## Requirements

 Before installing Trunco, make sure you have the following prerequisites:

 - **Python 3.6+**: Trunco requires Python version 3.6 or higher.
 - **pip**: Python's package installer.

 ## Installation via pip

 The easiest way to install Trunco is using `pip`, the Python package manager. Run the following command in your terminal:

 ```bash
 pip install trunco
 ```

 This will download and install Trunco and its dependencies.

 ## Verifying the Installation

 After installation, you can verify that Trunco was installed correctly by starting a Python interactive shell and importing the package:

 ```bash
 python
 ```

 Then, in the Python shell, type:

 ```python
 >>> import trunco
 >>> print(trunco.__version__)
 ```

 If Trunco is installed correctly, this command should display the version number of Trunco.

 ## Installing from Source

 If you prefer to install Trunco from source, you can clone the repository and install it manually:

 1. Clone the repository:

    ```bash
    git clone https://github.com/your-repo/trunco.git
    cd trunco
    ```

 2. Install the package:

    ```bash
    pip install .
    ```

 This will install Trunco from the local copy of the repository.

 ## Installing in a Virtual Environment

 It's a good practice to install Python packages in a virtual environment to avoid conflicts with other projects. Here's how you can do it:

 1. Create a virtual environment:

    ```bash
    python -m venv env
    ```

 2. Activate the virtual environment:

    - On macOS/Linux:

      ```bash
      source env/bin/activate
      ```

    - On Windows:

      ```bash
      .\env\Scripts\activate
      ```

 3. Install Trunco within the virtual environment:

    ```bash
    pip install trunco
    ```

 ## Upgrading Trunco

 If you already have Trunco installed and want to upgrade to the latest version, you can do so with pip:

 ```bash
 pip install --upgrade trunco
 ```

 ## Uninstalling Trunco

 If you need to remove Trunco from your environment, you can uninstall it using pip:

 ```bash
 pip uninstall trunco
 ```

 This will remove Trunco and its associated files from your Python environment.

 ## Troubleshooting

 If you encounter any issues during installation, consider the following:

 - Ensure that you're using Python 3.6 or higher.
 - Check that `pip` is up to date:

   ```bash
   pip install --upgrade pip
   ```

 - If you're installing from source, ensure that all dependencies are met.

 For further assistance, please refer to the [documentation](index.md) or open an issue on our [GitHub repository](https://github.com/your-repo/trunco/issues).
