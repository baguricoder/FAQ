# FAQ
1. Setting Up the Environment
Install Python :
sudo apt update
sudo apt install python3 python3-pip
Install Virtual Environment:
pip install virtualenv
virtualenv venv
source venv/bin/activate
2. Install Django and Dependencies
Navigate to the project directory:
cd path_to_extracted_folder/faq_project
Install Django:
pip install django
If there's a requirements.txt file:
pip install -r requirements.txt
3. Database Migrations
Since there's already a db.sqlite3 file, migrations might not be necessary unless you’ve made changes to models.
Run migrations :
python manage.py makemigrations
python manage.py migrate
4. Running the Server
Start the development server:
python manage.py runserver
Access the app: Open a browser and go to http://127.0.0.1:8000/
5. Project Structure Overview
Based on typical Django conventions:
manage.py: Used to manage the project (runserver, migrations).
faq_project/: Project settings (URLs, settings.py).
faq/: The core app, containing models, views, templates, etc.
db.sqlite3: The database file.
6. Common Commands
Create a superuser (for admin panel):
python manage.py createsuperuser
Access admin panel: Go to http://127.0.0.1:8000/admin


  







