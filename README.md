
# Chakula Chetu website

## Description

Chakula Chetu ('our food' in swahili) is a one of a kind website exclusively dedicated to amazing African Recipes. While African cuisine is the most delicious,nutritious and healthy, it is not explored because of lack of knowhow on how to prepare it and the nutritional value.Chakula Chetu is changing that. Now Users are allowed to sign up and share their sacred African cuisines passed down from generations. Recipes can be sorted by categories and users can search for particular dishes. Users can also update and delete their recipes. Let's make African food cool again! 


## Author

Sandra 

You can view the site at:[Chakula Chetu](https://recipe-nyumbani.fly.dev/)

## Screenshot
![Chakula Chetu](static/photos/Screenshot from 2022-06-27 13-11-10.png)


## User Stories
As a user I can:
* Signup and log in  
* See various recipes from other users
* Create a recipe and post
* Update my profile
* See all my cuisines on my profile page
* See details of a recipe
* See dishes from various categories
* Search for recipes 


## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| On log in | **On page load** | List of various recipes posted by other users|
| On home page | **Click on category bar** | see all recipes from a particular category|
| Search recipe using names | **On search bar click submit** | see recipes serach for with details |
| Update profile| **On profile page** | update profile with prodile picture, details and see all my posts|
| Create recipe| **on navbar click on create recipe tab** |  create a recipe and post on timeline|
|update and delete recipe| **click on delete and update buttons** |update and delete recipes  


## SetUp / Installation Requirements
### Prerequisites
* python3.10
* pipenv


### Cloning
* In your terminal:

        $ git clone https://github.com/Dindihub/recipe-site.git
        $ cd recipe

## Running the Application
* Creating the virtual environment

        $ pip3 install pipenv 
        $ pipenv install 
        $ pipenv install requests
        $ pipenv shell
        
       


* To run the application, in your terminal:

        $ python manage.py runserver
        

## Testing the Application
* To run the tests for the class files:

        $ python  manage.py tests 

## Technologies Used
* Python3.10
* Django 4.0.4
* fly.io
* HTML
* CSS frameworks

## Known Bugs
No known bugs

### License
MIT (c) 2022 **[Sandra Dindi](https://recipe-nyumbani.fly.dev/)**
