# Student Enrollment Analysis System (SEAS)
A web-based application written in Python (Django) to analyze the enrollment data of university students, particularly students from Independent University, Bangladesh.

![Screenshot 1](Implementation_Screenshots/home.png)
![Screenshot 2](Implementation_Screenshots/home-dark.png)
* Create a virtual environment using the following command `pip install virtualenv myenv`
* Select that environment's python.exe as the interpreter,'path: `myenv/Scripts/python.exe`'
# Dependencies
* Install all the list of dependencies with the specified version: `pip install mysqlclient==2.1.0`
* Django==3.2.9
* mysqlclient==2.1.0
* numpy==1.21.4
* openpyxl==3.0.9
* pandas==1.3.4
* python-decouple==3.5

# Run the project
* Try this command in the terminal [VScode] to run the project `python manage.py runserver`

* The default address [ http://127.0.0.1:8000/ ] will let you login to the web application
# Login Credentials anyone of below:
    username: topurayhan007 password: 12345
    username: zannatchowdhury password: 3451
    username: admin password: 12345
# Alternate Database
* Note that SQLite is used as the default database in this project
* If you choose to use a different database configure it in the Django Settings DATABASE section
* Then migrate to create the tables in the SQL database using the following command `python manage.py makemigrations` followed by `python manage.py migrate`
* Create a user by the following command `python manage.py createsuperuser`
* To populate the database with data run the following script in python shell `populationScript.py` filepath `scripts/populationScript.py`
  * To run the populationScript.py on windows [make sure you have GitBash terminal in VScode]:
      Use the following command `./manage.py shell < scripts/populationScript.py`
  * To run the populationScript.py on Mac:
        Use the following command `python manage.py shell < scripts/populationScript.py`
        
    `NOTE:` The population Script will take a very long time to populate data if you are using SQLite Database (60 minutes +) and the project is in your HDD.
      * It was lot faster in MySQL like around 4/5 minutes
      * These doesn't apply to Mac users, not sure about Linux users
* You should see that your database has successfully populated

![Screenshot 3](Implementation_Screenshots/Screenshot 2021-12-26 at 11.17.58 AM.png)
![Screenshot 4](Implementation_Screenshots/Screenshot 2021-12-26 at 11.18.17 AM.png)
![Screenshot 5](Implementation_Screenshots/Screenshot 2021-12-26 at 11.18.42 AM.png)
![Screenshot 6](Implementation_Screenshots/Screenshot 2021-12-26 at 11.18.46 AM.png)
![Screenshot 7](Implementation_Screenshots/Screenshot 2021-12-26 at 11.19.15 AM.png)
![Screenshot 8](Implementation_Screenshots/Screenshot 2021-12-26 at 11.19.17 AM.png)
![Screenshot 9](Implementation_Screenshots/Screenshot 2021-12-26 at 11.19.33 AM.png)
![Screenshot 10](Implementation_Screenshots/Screenshot 2021-12-26 at 11.19.39 AM.png)
![Screenshot 11](Implementation_Screenshots/Screenshot 2021-12-26 at 11.19.45 AM.png)
![Screenshot 12](Implementation_Screenshots/Screenshot 2021-12-26 at 11.19.48 AM.png)
![Screenshot 13](Implementation_Screenshots/Screenshot 2021-12-26 at 11.20.17 AM.png)
![Screenshot 14](Implementation_Screenshots/Screenshot 2021-12-26 at 11.20.21 AM.png)
![Screenshot 15](Implementation_Screenshots/Screenshot 2021-12-26 at 11.20.50 AM.png)
![Screenshot 16](Implementation_Screenshots/Screenshot 2021-12-26 at 11.20.59 AM.png)
![Screenshot 17](Implementation_Screenshots/Screenshot 2021-12-26 at 11.21.39 AM.png)
![Screenshot 18](Implementation_Screenshots/Screenshot 2021-12-26 at 11.21.49 AM.png)
![Screenshot 19](Implementation_Screenshots/Screenshot 2021-12-26 at 11.21.54 AM.png)
![Screenshot 20](Implementation_Screenshots/Screenshot 2021-12-26 at 11.22.02 AM.png)
![Screenshot 21](Implementation_Screenshots/Screenshot 2021-12-26 at 11.22.05 AM.png)
![Screenshot 22](Implementation_Screenshots/Screenshot 2021-12-26 at 11.22.15 AM.png)
![Screenshot 23](Implementation_Screenshots/Screenshot 2021-12-26 at 11.22.21 AM.png)
![Screenshot 24](Implementation_Screenshots/Screenshot 2021-12-26 at 11.22.26 AM.png)
![Screenshot 25](Implementation_Screenshots/Screenshot 2021-12-26 at 11.22.41 AM.png)
![Screenshot 26](Implementation_Screenshots/Screenshot 2021-12-26 at 11.22.49 AM.png)
![Screenshot 27](Implementation_Screenshots/Screenshot 2021-12-26 at 11.24.23 AM.png)
![Screenshot 28](Implementation_Screenshots/Screenshot 2021-12-26 at 11.24.25 AM.png)

# Thanks for reading. Have a nice day & keep on coding! :)



