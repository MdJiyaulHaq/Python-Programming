# How to create and publish our own package to PyPI

# Step 1: Create a Package 
 
Step 1.1: Create a PyPI account
Go to https://pypi.org/account/register/ and create an account.

Step 1.2: install setuptools and wheel and twine globally
pip3 install setuptools wheel twine

Step 1.3: Create high-level directory structure with the same name as your package
mkdir pdf-editor
cd pdf-editor

Note: 
There can be other files and directiories like tests, data, etc. in the high-level directory.

Step 1.4: Create a `pdf_editor` directory inside the high-level directory
mkdir pdf_editor
cd pdf_editor

Step 1.5: Create an `__init__.py` file inside the `pdf_editor` directory
touch __init__.py

Step 1.6: Create modules inside the `pdf_editor` directory as needed
Eg: pdf2jpg.py, pdf2text.py, jpg2pdf.py, pdf2word.py, etc.


Step 1.7: Create a `README.md` file and write a brief description of your package
touch README.md

Step 1.8: Create a `LICENSE` file to specify the license for your package
touch LICENSE

# Step 2: Build the package
Step 2.1: Create a `setup.py` file in the root directory of your project.

Step 2.2: Run the following command to build the package:
python3 -m build      

Note: This command builds source and build distributions. build package should be installed first
pip3 install build



# Step 3: Publish/Upload the package to PyPI
twine upload dist/*
                  