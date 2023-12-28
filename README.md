Make sure you have Python 3.x installed and the latest version of pip installed before running these steps.

To contribute, please follow the guidelines process.

Clone the repository using the following command
git clone https://github.com/swamypotharaveni/expert-parakeet.git

Create a virtual environment where all the required python packages will be installed

# Use this on Windows
python -m venv env
# Use this on Linux and Mac
python -m venv env

Activate the virtual environment


# Windows
.\env\Scripts\activate
# Linux and Mac
source env/bin/activate

Install all the project Requirements

pip install -r requirements.txt

-Apply migrations and create your superuser (follow the prompts)

# apply migrations and create your database
python manage.py migrate

# Create a user with manage.py
python manage.py createsuperuser
