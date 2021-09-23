# Healthy Nutrition V2 🍏

---


## What is this program for ? 

This application was built for my Python developer path at Openclassrooms.

The aim is to create a website that allows people to find healthier products to those considered as too fat, 
too sweetened or too salty.

Healthy Nutrition " *V2* " has two new features : 

* Forgot Password : reset your password.
* Autocompletion : display suggestions to client when he is searching a product.
___


### *Install Python* ★

- Python 3.9
  > Install Python : https://www.python.org/downloads/
  
  > Python Documentation : https://www.python.org/doc/
  
### *Virtualenv*

- **Install** : pip3 install virtualenv
- **Create Virtualenv folder in the project** : virtualenv -p python3 env
- **Activate Virtualenv** : source env/bin/activate


### *Install and run the program* 💻

- **Download or Clone the project** : https://github.com/LekishviliRati/P8_Healthy_Nutrition.git
- **Install requirements** : pip install -r requirements.txt
- **Install and activate Virtualenv**
- **Run** : python3 manage.py runserver

### *Run Tests 👨‍🔬*

- **Overall tests** : python3 manage.py test
- **Coverage report** : coverage run manage.py test -v 2 && coverage report

### *User Journey* 😎

- Research a product to substitute.
- Check given choices of substitutes.
- For complete information click on Open Food Facts link.
- For further information on a product click on product's name and access to product page. 
- Create an account if you want to save your product favorite.
- Login with email and get access to your profile page, and your favorites list.


### *Key Features* 

- Responsive user interface.
- Personal page with list of chosen products.
- Research healthier products according to nutritional scores.

### *Constraints* 👮‍♂️

- Graphic charter :
  > https://company-82435.frontify.com/d/6Yy9WFJdtp8j/pur-beurre-style-guide#/elements-basiques/grille

- Deployment on Heroku :
  > https://www.heroku.com
- Test Driven Development

- Flake8 :
  > https://flake8.pycqa.org/en/latest/
  