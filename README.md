# AirBnB Clone
<p align="center">
  <a href="" rel="noopener">
 <img width=500px height=200px src="./hbnb.png" alt="Project logo"></a>
</p>
## Project Description

This is a project from the ALX Software Engineering program. It is a clone for the AirBnB platform. It takes place over several phases. The first one is the creation of a command line using python.

The project has several classes or models
 - BaseModel - which is the base model for other models
 - User - a class for users
 - State - a model class for state
 - City - a model class for city
 - Amenity - a model class for amenity
 - Place - a model class for place
 - Review - a model class for Review

## Command Line Interpreter
### How to start it
The console can easily be started by running the `console.py` file

`$ ./console.py`

### How to use it
From the console you can do several actions

1. show all objects
i. generally all objects without specific class
```bash
(hbnb)all
["[BaseModel] (2e5f4d41-8913-46ea-927f-72699719ec9a) {'id': '2e5f4d41-8913-46ea-927f-72699719ec9a', 'created_at': datetime.datetime(2022, 8, 7, 13, 21, 42, 405349), 'updated_at': datetime.datetime(2022, 8, 7, 13, 21, 42, 405366), 'name': 'My_First_Model', 'my_number': 89}", "[BaseModel] (d5d6bf45-1b29-4c59-8150-0463e852a478) {'id': 'd5d6bf45-1b29-4c59-8150-0463e852a478', 'created_at': datetime.datetime(2022, 8, 7, 13, 21, 43, 671330), 'updated_at': datetime.datetime(2022, 8, 7, 13, 21, 43, 671342), 'name': 'My_First_Model', 'my_number': 89}", "[BaseModel] (032e58fd-d3bb-4892-a610-bdc5d23ffe63) {'id': '032e58fd-d3bb-4892-a610-bdc5d23ffe63', 'created_at': datetime.datetime(2022, 8, 7, 13, 21, 46, 497997), 'updated_at': datetime.datetime(2022, 8, 7, 13, 21, 46, 498008), 'name': 'My_First_Model', 'my_number': 89}" ... ]
(hbnb)
```

ii. with a specific class
```
(hbnb)all Place
["[Place] (2440328a-f4e4-44d8-bb03-07feef678085) {'id': '2440328a-f4e4-44d8-bb03-07feef678085', 'created_at': datetime.datetime(2022, 8, 7, 14, 4, 50, 391795), 'updated_at': datetime.datetime(2022, 8, 7, 17, 37, 16, 723725), 'city_id': '', 'user_id': '', 'name': '', 'description': '', 'number_rooms': 0, 'number_bathrooms': 0, 'max_guest': 0, 'price_by_night': 0, 'latitue': 0.0, 'longitude': '123N', 'amenities_ids': [], 'lattitude': '56.2897345', 'latitude': '54'}"]
(hbnb)
```

2. create an object
```bash
(hbnb)create BaseModel
3eba1762-8964-4b25-b720-6447a2f0cdf7
(hbnb)
```

3. Show an object of a certain class and id
```
(hbnb)show BaseModel 3eba1762-8964-4b25-b720-6447a2f0cdf7
[BaseModel] (3eba1762-8964-4b25-b720-6447a2f0cdf7) {'id': '3eba1762-8964-4b25-b720-6447a2f0cdf7', 'created_at': datetime.datetime(2022, 8, 7, 23, 15, 13, 687760), 'updated_at': datetime.datetime(2022, 8, 7, 23, 15, 13, 687794)}
```

4. destroy an object
```
(hbnb)destroy BaseModel 3eba1762-8964-4b25-b720-6447a2f0cdf7
(hbnb)
```

5. update an object
```
(hbnb)show BaseModel 2e5f4d41-8913-46ea-927f-72699719ec9a
[BaseModel] (2e5f4d41-8913-46ea-927f-72699719ec9a) {'id': '2e5f4d41-8913-46ea-927f-72699719ec9a', 'created_at': datetime.datetime(2022, 8, 7, 13, 21, 42, 405349), 'updated_at': datetime.datetime(2022, 8, 7, 13, 21, 42, 405366), 'name': 'My_First_Model', 'my_number': 89}
(hbnb)update BaseModel 2e5f4d41-8913-46ea-927f-72699719ec9a name "changed_name"
(hbnb)show BaseModel 2e5f4d41-8913-46ea-927f-72699719ec9a
[BaseModel] (2e5f4d41-8913-46ea-927f-72699719ec9a) {'id': '2e5f4d41-8913-46ea-927f-72699719ec9a', 'created_at': datetime.datetime(2022, 8, 7, 13, 21, 42, 405349), 'updated_at': datetime.datetime(2022, 8, 7, 23, 20, 57, 814376), 'name': 'changed_name', 'my_number': 89}
```
