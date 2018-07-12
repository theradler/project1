# Project 1

Web Programming with Python and JavaScript


//Site Oveview//

This is my weathersite, from the get go implemented using the ORM models as I found it may interacting with SQL much easier.

Login and logout is accomplished with the flask-login module, found it made managing sessions very straight forward

For search, tried three methods, first attempt I tried to use variable replacement within an ORM query to dynamically set the column = value however could not get that to work, then I tried using methods on the Location model class from models.py but that kept giving me "missing parameter self" (Now realize I need to instantiate the class before calling it). Finally implemented some conditional logic within the view itself, it is not pretty but it works

For the location I realize I am doing way to much processing before the page loads, I did not realize till Wednesday night that Jinja2 allowed for logic on the page itself and moving forward will use that to lessen the amount of redundant variables and calls in the views page. Used Jinja2 logic to ensure that people who had already made a comment could not do so again, seemed easier to just prevent access to the controller than to implement an error page for after the hit the submit button.

The API call was probably the easiest part to implement, created a separate utils file which made testing it way easier

Same with implementing the site API, very straightforward and the use of ORM models made getting the data I needed a breeze

I still suck at css and have accepted that I will probably not be a front end guy. Spent more time than I care to admit trying to get stuff to align on the navbarLink

I had a lot of fun QA-ing the site (its my day job) and implemented error handling to prevent unauthorized access, bad logins, password mismatches and username already in use.


//What I would do differently in the future//
Think it would be way easier to implement a lot of the count functions on the views page as methods, would also like to get way better at bootstrap grids, they have been and endless source of frustration for me
