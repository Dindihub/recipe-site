
# Chakula Chetu website

## Description

Chakula Chetu ('our food' in Swahili) is a unique website dedicated to amazing African Recipes. While African cuisine is the most delicious, nutritious, and healthy, it has not been explored because people lack information on how to prepare African foods. Chakula Chetu is changing that. Users can sign up and share their sacred African cuisines passed down through generations. Recipes can be sorted by categories and per food name. Users can also update and delete their recipes. Let's make African food cool again! 


## Author

Sandra 

You can view the site at:[Chakula Chetu](https://recipe-nyumbani.fly.dev/)

## Screenshot
![Chakula Chetu](https://github.com/Dindihub/recipe-site/issues/1#issue-2975197077)


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
