# Database-Project
Student Enrollment Analysis System 

Create a virtual environment [eg: myenv]

Select that environment's python.exe as the interpreter [path: myenv/Scripts/python.exe]

Install all the list of dependencies with the specified verrsion: [eg: pip install mysqlclient==2.1.0]
      asgiref==3.4.1
      Django==3.2.9
      et-xmlfile==1.1.0
      mysqlclient==2.1.0
      numpy==1.21.4
      openpyxl==3.0.9
      pandas==1.3.4
      python-dateutil==2.8.2
      python-decouple==3.5
      pytz==2021.3
      six==1.16.0
      sqlparse==0.4.2

Try this command in the terminal [VScode] to see if the project is running [eg: python manage.py runserver]

The default address [ http://127.0.0.1:8000/ ] will let you login to the web application
  Login Credentials anyone of below:
    username: topurayhan007, password: 12345
    username: zannatchowdhury, password: 3451
    username: admin, password: 12345

Note that SQLite is used as the default database in this project

If you choose to use a different database configure it in the Django Settings DATABASE section

Then migrate to create the tables in the SQL database using the following command [eg: "python manage.py makemigrations" followed by "python manage.py migrate"]

Create a user by the following command [eg. python manage.py createsuperuser]

To populate the database with data run the following script in python shell [ populationScript.py ] filepath [scripts/populationScript.py] 
    To run the populationScript.py on windows [make sure you have GitBash terminal in VScode]:
        Use the following command [eg: ./manage.py shell < scripts/populationScript.py]
    To run the populationScript.py on Mac:
        Use the following command [eg: python manage.py shell < scripts/populationScript.py]
        
    NOTE: The population Script will take a very long time to populate data if you are using SQLite Database [60 minutes +]
          It was lot faster in MySQL like around 4/5 minutes
          These doesn't apply to Mac users, not sure about Linux users
          
You should see that your database has successfully populated


Thanks for reading. Have a nice day and keep on coding! :)
