## Read-It Testing Documentation

# Table Of Contents

1. [Code Validation](#code-validation)
    - [HTML5](#html5)
    - [CSS3](#css3)
    - [Python](#python)
2. [Features and Functionality](#features-and-functionality)
    - [Responsiveness](#responsiveness)
    - [Features (A-Z)](#features)
3. [User Stories](#user-stories)
    - [Users](#users)
    - [Site Owner/Admin](#site-owner-and-admin)
4. [Bugs and Fixes](#bugs-and-fixes)

# Code Validation

### HTML5
[W3C HTML Validator](https://validator.w3.org/#validate_by_input) was used to check my HTML – Only errors found were the Jinja code inputs. All HTML passed.

### CSS3 
[W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) was used to make sure my CSS was compliant – No errors found.

### Python
[PEP8 Online](http://pep8online.com/) was what I used to make sure my Python Code was PEP8 compliant – No errors found.

[Back to contents](#table-of-contents)

# Features and Functionality

### Security Testing

- All pages were tested to make sure that no unauthorised users can access pages they should not have access to.
- If a user is logged out, they have no access to any pages they should not have access to. 
- Redirects are all working as expected, with correct flash messages present.

### Responsiveness

-	The responsiveness of this site was tested using a Dell XPS 15 and an iPhone 8 plus. 

## Features
## (A-Z)

### Add Book Review

-	Form – All inputs work as intended, with requirements being displayed and inputs highlighted red if not filled in and required. 
-	Submit – Submit button correctly sends the data to the database.

### Book Review Cards

-	Hover – I added a hover effect on the book review cards so that the user can easily see which book review they are looking at, and this works well.  
-	Info & Review Icon – The Info & Review icon works as intended, sliding up the book review information over the book image.
-	Buttons – The correct buttons are displayed depending on whether the user is logged in, logged out or is the Admin of the site. 

### Buttons

-	Links - All buttons on the site have been tested to make sure that the direct the users to the relevant page. 
-	Hover – Most buttons have an alternative colour when hovered over, and they were all checked to make sure the correct colours were displayed when hovered over.

### Delete Book Function

-	The Delete function was tested with a number of book reviews from the Home page. 

### Edit Book Review

-	Pre-fill – When a user edits a book review, the form is correctly filled in with the information they have previously entered (bar the 'genre' input which is mentioned in the Bugs and Fixes section). 
-	Buttons – Both the cancel and edit review buttons work as intended, with the edit review button correctly updating the database. 

### Flash Messages

-	All flash messages were tested across the site to make sure they popped up when they should, and that the text in the flash message is correct and not misspelt or gramatically incorrect. 

### Footer

-	Links - All footer social links were tested, and correctly navigated the user to the relevant site. 
-	The footer remained at the bottom of the site regardless of amount of content, and this was tested by removing all content from the page, and re-entering it. 

### Logout

-	The logout feature works as intended and correctly logs the user out of the site. 

### Navbar

-	Links - All navbar links were thoroughly tested on both laptop and mobile views, and they all worked as intended, and directed the user to the correct page.

### Register/Log In Forms

-	Requirements – Email/Password requirements are listed below the Password input on the 'Register' page so users know when signing up what the requirements are for a new Email/Password. I have tested these features to make sure they work.
- Email – Both forms were extensively tested to make sure that the same Email could not be used more than once, and that the incorrect password could not be used to access an account that did not belong to them. 

[Back to contents](#table-of-contents)

# User Stories

## User Story Testing

- As a user, I want the structure of the site to be simplistic and minimalistic

The main content of the site is very simplistic. The site contains three main webpages:

1. Home page which holds site logo and the book reviews 
2. Login Page which allows users to login and post a book review once they've registered 
3. Registration page which gives the users to register to the site using their email and 
4. Account page which displays the books the user has posted 

The UI/UX on all three webpages are also easy on the eye, simplistic and minimalistic. 

- As a user, I want to be able to securely log out of Books and not have other users edit/delete the books I've posted

This criteria has been tested and has successfully been implemented 

- As a user, I want to be able to access the site on all devices

The site is fully responsive on all devices, mobile, tablet and PC.

- As a user, I want to be able to access Books's social media accounts

For the purpose of this project, social media links will not be added however links font awesome icons will be added for demonstration purposes. This critera has been met. 

- As a user, I want to be able to register to Books using an email and password, log in and review a book I have read

This critera has been met successfully. The CRUD functionality has been implemented to make sure this criteria has been met. Users are able to register using an email and password, login, and post a book review which is then displayed on the home page.

- As a user, I want an easy to navigate around site

I believe this criteria has been met as the site is very simple to navigate around. There is a Registration page, a Login page, an Account page and a Home Page. 
The UI/UX is very simplistic and clean in all pages to make sure this criteria is met.

- As a user, I want the structure of the site to be simplistic

This criteria has been met as there are only only 4 webpages to the site.

- As a user, I want to be able securely log out of Books and not have other users edit/delete the books I've posted

This criteria has been met. Mongo has successfully been implemented for the overall CRUD funtionality to work. 

### Developer goals

- To create a database with MongoDB

This criteria has been met

- To implement CRUD funtionality

This criteria has been met. Users are able to register, login, add, edit and delete. 

- To create a responsive, clean and consistent UX

This criteria has been met. The site works on all devices and has a simple UI/UX. 

- To not allow users to edit/delete other users book reviews.

This criteria has been met. I overcame some errors in my code which meant that anyone can edit/delete any of the users books. After some testing, I successfully resolved this.  

[Back to contents](#table-of-contents)

# Bugs and Fixes

In doing this project, I encountered many bugs and errors in creating this site. I have tried to make sure I keep track of each error to showcase them and explain the error as clearly as possible.

#### ***Error #1***
First initial deployment to heroku failed due to the UTF encoding.

#### ***Solution***
After changing to 'Save with encoding', I managed to successfully deploy to Heroku
![Heroku deployment fai](static/images/Heroku-deploy-fail.png)

#### ***Error #2***
Upon first testing to see if my registration page was working and users were able to register, I encontered a Typo error which stated, **rn dumps rv = \_json.dumps(obj, kwargs)**
This error prevented me from adding the user to my Mongo collection
![Typo Error](static/images/Typo-error.png)

#### ***Solution***
After speaking with tutor support, I successfully mananged to add my users to my Mongo collections everytime a user registered.
![Collections](static/images/Collections.png)

#### ***Error #3***
Upon successfully deployment, I encountered an 'Application error' for my deployment link. I found that upon looking into my heroku log, **_error code=h10_** would come up.
![Heroku application error](static/images/Application-error.png)

#### ***Solution***
The solution was that there was a bug in my Procfile. After speaking my mentor, he pointed out that I hadn't correctly typed:
`web:gunicorn run:app`

Once I correctly changed it to `web: gunicorn run:app --preload`, the error was solved.

[Back to contents](#table-of-contents)