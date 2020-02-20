# Welcome to MedApp!

This is a Django based medical data application built to meet the following requirements:

1. Separate Signup for users and medical practitioners

2. A page where users(only) can fill in their medical information

3. A page that displays the statistical details of the medical records gotten from the users(I used chart.js). 

4. A table that displays all users and their medical records with dropdowns for filtering specific cases, for practitioners view only (I used django tables).


## Installation Instruction:
1. Clone the Repo
2. Create a virtual environment
3. install requirements with `pip install -r requirements.txt`
4. Add a SECRET_KEY to your environment. e.g: on Linux run: `setx SECRET_KEY= <secret-key-of-your-choice>`
5. run migrations with `python manage.py migrate`
6. Run the development server with `python manage.py runserver` 
