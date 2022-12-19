REST APIs created using Django Rest Framework to perform CRUD operation for flight reservation.. JWT Authentication is added to all the API's.

# Operations handled by APIs
1. Add, Update, Delete and Read details of a single flight.
2. Read details of all flights.
3. Find flight based on city of departure, city of arrival and date of departure.
4. Add, Update, Delete and Read details of a single passenger.
5. Read details of all passengers.
6. Add and Delete a passenger's reservation on a flight.
7. Read details of all reservations.
8. User registration.
9. User login.
10. User logout.

# Database Model
![Database Model](https://github.com/devbk007/Flight-Reservation-API-using-Django-Rest-Framework/blob/master/database_model.png?raw=true)

# Steps to install application
1. Install packages    
    ```
    pipenv install
    ```

    ```
    pipenv install PyJWT==1.7.1
    ```

2. Activate virtual environment
    ```
    pipenv shell
    ```

3. Delete the file Flight-Reservation-API-using-Django-Rest-Framework/flightServices/db.sqlite3.

4. Perform migrations.
    ```
    python manage.py makemigrations
    ```
    ```
    python manage.py migrate
    ```

5. Create a superuser
     ```
    python manage.py createsuperuser
    ```
  
6. Run the command 
    ```
    python manage.py runserver
    ```
# API's to test
Download [DRF-FLIGHT-RESERVATION-API.postman_collection.json](https://github.com/devbk007/Flight-Reservation-API-using-Django-Rest-Framework/blob/master/DRF-FLIGHT-RESERVATION-API.postman_collection.json) and import the file in Postman as a collection to test the APIs.

# Demo Video
[![Video Thumbnail](https://github.com/devbk007/Flight-Reservation-API-using-Django-Rest-Framework/blob/master/youtube_thumbnail.png)](https://youtu.be/eTJw36TlCp0)