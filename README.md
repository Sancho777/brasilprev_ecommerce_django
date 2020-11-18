# Brasilprev Test - Application

Source Code for Brasilprev Test

Build a REST API to simulate an online store. This store must have a
registration of your customers, products and orders.

E-commerce REST API to simulate an online store using Django. This store have 
registration of your customers and products. 


# Testing

To make visualization easier the project is deployed in the following link from heroku:

https://brasilprevtestams.herokuapp.com/


# Usage

In the home page you can create new Users clicking in "novo usuário" on the top tab. 

to register new products it is necessary to access the administration page in the link:

https://brasilprevtestams.herokuapp.com/admin/

You can use the superuser: 

\$ User: admin
\$ Password: admin123

# Local installation 

1 - Install python and add the Python installed directory to the PATH environment variable as C:\Python37\ and C:\Python 37\Scripts.

2 - Open windows command prompt on the directory you want to install:

3 - Git clone the "brasilprev_ecommerce_django"

4 - Create a virtual env with this command:

\$ python -m venv env

5 - Activate your virtual env with:

\$ env\Scripts\activate

6 - Install requirements using pip:

\$ cd brasilprev_ecommerce_django
\$ cd ecommerce_brasilprev
\$ pip install -r requirements.txt

7 - Run the development server using manage.py from command prompt:

\$ python manage.py collectstatic
\$ python manage.py runserver

Click on the link presented on the command line:

Ex: http://127.0.0.1:8000
