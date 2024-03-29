# Hawksbill Heroes

![Hawksbill Heroes Logo](/static/assets/images/hawksbill-heroes-nav-logo.jpg)

Hawksbill Heroes is a organisation raising funds to aid in the mission of keeping Hawksbill Sea Turtles from going extinct. The site currently features a merchandise shop where users can purchase items and a personalised dashboard where they can see their orders.

The site is targeted towards envirnomentally concious people some of whom will already know about the Hawksbill Turtles but for others it will teach them about the animal, explain the dangers they are facing and what they can do to help.

This website does take payments using Stripe; Please note that the website is for project purposes only, do not enter any personal credit/debit cards when placing orders. You can find a list of dummy cards to use under Stripes documentation [here](https://stripe.com/docs/testing#cards).

View the deployed app [Live website for Hawksbill Heroes](https://hawksbill-heroes-6080a7a722cc.herokuapp.com/)

![Image to show the website on different media screens](/static/assets/images/am-i-responsive.jpg)

- [Hawksbill Heroes](#hawksbill-heroes)
  * [UX](#ux)
    + [User stories](#user-stories)
      - [First time users](#first-time-users)
      - [Returning users](#returning-users)
    + [Design](#design)
    + [Wireframes](#wireframes)
    + [Agile Methodology](#agile-methodology)
      - [User stories not yet implemented](#user-stories-not-yet-implemented)
  * [Database](#database)
    + [Features](#features)
      - [Current features](#current-features)
      - [CRUD](#crud)
      - [Create](#create)
        * [Users](#users)
        * [Owners](#owners)
      - [Read](#read)
        * [Users](#users-1)
        * [Owners](#owners-1)
      - [Update](#update)
        * [Users](#users-2)
        * [Owners](#owners-2)
      - [Delete](#delete)
        * [Users](#users-3)
        * [Owners](#owners-3)
  * [Marketing strategies](#marketing-strategies)
    + [SEO](#seo)
      - [Keywords](#keywords)
      - [External links](#external-links)
      - [Sitemap and robots.txt](#sitemap-and-robotstxt)
      - [Email Marketing](#email-marketing)
  * [Technologies Used](#technologies-used)
    + [Languages](#languages)
    + [Frameworks, Libraries & Programs Used](#frameworks--libraries---programs-used)
  * [Testing](#testing)
      - [HTML Validator](#html-validator)
      - [CSS Validator](#css-validator)
      - [JavaScript](#javascript)
      - [Pylint](#pylint)
    + [Bugs](#bugs)
  * [Installing](#installing)
    + [Create the Heroku App](#create-the-heroku-app)
    + [Attach the Postgres database](#attach-the-postgres-database)
    + [Update Heroku Config Vars](#update-heroku-config-vars)
    + [Deploy](#deploy)
  * [Forking this repository](#forking-this-repository)
  * [Cloning this repository](#cloning-this-repository)
  * [Acknowledgments](#acknowledgments)
    + [Content](#content)
    + [Code](#code)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

## UX

### User stories

#### First time users
For first time users the goal of the site is to:
- Spread awareness of Hawksbill turtles, who they are and why they are going extinct.
- Provide knowledge on what users can do to help.
- Learn what the charity is doing to help.
- Be able to contribute to the cause.
- Purchase merchandise to help.
- Donate to the cause.

#### Returning users
Returning users are able to log in and:
- See previous orders.
- Make new orders with ease.
- View total donations on their dashboard.
- Review the products.

### Design
The design is minimilistic with many photos of the turtles to showcase their beauty. The colour scheme is colour picked from the images, with the header and footer being a green/blue tone to match the water and the soft beige background body matching the turtles body. It represents the clear shallow waters of Hawaii and envokes a calming reaction from the user.

![Colour palette chosen for website](/static/assets/images/color-palette.jpg)

### Wireframes

![Homepage Wireframe](/static/assets/images/hawksbill-heroes-wireframe-homepage.jpg)
![Login Wireframe](/static/assets/images/hawksbill-heroes-wireframe-login.jpg)
![Turtles Wireframe](/static/assets/images/hawksbill-heroes-wireframe-turtles.jpg)
![Merchandise Wireframe](/static/assets/images/hawksbill-heroes-wireframe-merchandise.jpg)
![Checkout Wireframe](/static/assets/images/hawksbill-heroes-wireframe-checkout.jpg)

### Agile Methodology

Using Github projects user stories where created using an issues template, then these where mapped onto a Project board to keep track of the the development in an agile approach. View the [Project board](https://github.com/users/debbie-herridge/projects/9/views/1). An additional coloumn called 'Current Iteration' was added to ensure the current iteration of Epics was being worked on before moving onto the next.

#### User stories not yet implemented

- Adopt a turtle

As the website grows, users will be able to adopt a turtle for a set amount of time. These are labelled as "Won't Have" as a user story issue, but they are intented to be added at a later date.

## Database 

The diagram below shows the database schema and the relationship between models. Data is stored on ElephantSQL which is linked to the site using an API key.

![Database schema](/static/assets/images/hawksbill-heroes-dataschema.jpg)

### Features

#### Current features

The site boasts clean consistant styling throughout the site. The same template is used throughout to improve user experience, the only difference between pages is the image background where it changes for displaying products, user account pages and dashboard.

#### CRUD

#### Create

##### Users

- Users can register to create new accounts.
- Create reviews for the products they have purchased.
- Create new orders.
- Can make new donation payments.

##### Owners

When owners are logged in they can add new turtles on the main page using a form only visable to those logged in with Staff status. The form allows them to enter all the details needed to add a new turtle and automatically displays them on the main page when refreshed.

#### Read 

##### Users

 - Users can view their previous orders in their dashboard and leave reviews.
 - View their current personal details their dashboard including their total donation payments.
 - Users can view all the turtles on the database in the turtles homepage.

##### Owners

Owners can view all previous orders in their dashboard.

#### Update

##### Users

Users can update their personal details either by their dashboard or the drop down navigation bar.

##### Owners 

On each individual turtle page owners can update each turtles details.

#### Delete

##### Users

Users can delete their accounts, which requires them to tick a box to confirm they are happy to proceed so no accounts are deleted by mistake.

##### Owners

Owners can delete a turtle by following the link on each individual turtle page. The page requires them to confirm they are happy to proceed before deleting the turtle from the database. Once a turtle is deleted it is automatically reflected and removed from the turtles homepage.


## Marketing strategies

Hawksbill Heroes is a B2C site, where it's goal is to educate and raise user funding for sealife conservation. Currently this is collected using the purchasing of merchandise, however this will expand in future to take donations and allow users to adopt the turtles. 

The target market are animal lovers who are environment cautious. As this organisation is not driven by profit there is a limited marketing budget. Consumers would want their donations to be used on the turtles and not marketing, therefore the charity adopts creative and cost-effective strategies, such as using images of the turtles on social media, email marketing and word of mouth. 

### SEO

As the Hawksbill Turtles are not well researched, the website has limited competion to reach the first page of google and therefore using SEO strategies such as Meta Data and Keywords will help boost the website.

#### Keywords

Keywords include:
- Hawksbill Turtles
- Sealife welfare
- Animal welfare
- Sealife conservation
- Ocean
- Exctinction
- How to save the Hawksbill turtles
- Why are Hawksbill turtles going exctint 

#### External links

The website has been linked to:

-[WWF](https://www.wwf.org.uk/) 
-[NOAA](https://www.noaa.gov/)
-[Hawaiian Hawksbill Conservation](https://www.hihawksbills.org/)

The above are all reputable websites which helps build trust in our organisation and shows search engines that this website is good quality, therefore improving the websites ranking.

#### Sitemap and robots.txt

Using [XML Sitemap generator](https://www.xml-sitemaps.com/) a sitemap file was created with a list of important page URLs to ensure that search engines are able to understand the site's structure and easily navigate through the site.

A robots.txt file was created to tell search engines where they are not allowed to go on the website. This improves SEO by increasing the quality of the site

#### Email Marketing

Using [MailChimp](https://mailchimp.com/landers/email-marketing-platform/?ds_c=DEPT_AOC_Google_Search_UK_EN_Brand_Acquire_Exact_MKAG_UK&ds_kids=p77184324956&ds_a_lid=kwd-2285511033&ds_cid=71700000112280664&ds_agid=58700008474313140&gad_source=1&gclid=CjwKCAiA-vOsBhAAEiwAIWR0TUfY3feNzMQwqGg5DbYJWv79iRw8EukSsRr8wBOA3l4-OGa16TrqfBoC0_cQAvD_BwE&gclsrc=aw.ds) users can sign up for email marketing. Once users input their email they are added to the list of audience on Mail Chimp where emails can regularly be sent to them containing updates from the organisation and marketing techniques.

## Technologies Used

### Languages 
- [HTML](https://en.wikipedia.org/wiki/HTML5)
- [CSS](https://en.wikipedia.org/wiki/CSS)
- [Python](https://www.python.org/)
- [Javascript](https://www.javascript.com/)

### Frameworks, Libraries & Programs Used
- [Bootstrap 5](https://getbootstrap.com/)
Bootstrap is used throughout the site for styling and responsiveness accross different devices.
- [Fontawesome](https://fontawesome.com/docs/web/style/animate)
Icon used to display the shopping basket on the Navagation bar.
- [Google Fonts](https://fonts.google.com/)
I choose font Sofia Sans for the whole site with a back up font of Sans Serif.
- [JQuery](https://jquery.com/)
JQuery is used with Bootstrap for the Navagation bar to make it responsive.
- [Git](https://git-scm.com/)
Git is used to commit and Push code to GitHub.
- [GitHub](https://github.com/)
Used to store code for this project after being pushed from Git.
- [GitPod](https://gitpod.io/workspaces)
Used as coding environment for the development.
- [Canva](https://www.canva.com/posters/0)
Used to make the website logo for the navigation bar and merchandise logo.
- [Django](https://www.djangoproject.com/) 
Used to build the project and apps.
- [ElephantSQL](https://www.elephantsql.com/)
Used to store information to the database.
- [Cloudinary](https://cloudinary.com/ip/gr-sea-gg-brand-home-base?utm_source=google&utm_medium=search&utm_campaign=goog_selfserve_brand_wk22_replicate_core_branded_keyword&utm_term=1329&campaignid=17601148700&adgroupid=141182782954&keyword=cloudinary&device=c&matchtype=e&adposition=&gad_source=1&gclid=CjwKCAiA-P-rBhBEEiwAQEXhH2ndeczu952BxiEy0n2brT63DR2X09OuugdQMRhehy0gXScT3VM9VxoCldEQAvD_BwE)
Used to store media. 
- [Heroku](https://www.heroku.com/)
Used to deploy from Github to create the live website.
- [LucidChart](https://lucid.app/)
Used to create the wireframes.
- [Chrome Dev Tools](https://developer.chrome.com/docs/devtools)
Used to help debug and style website throughout development.
- [Favicon](https://favicon.io/)
Used to create favicon icons.
- [Grammerly](https://www.grammarly.com/service/download)
Used to check and correct grammer.
- [MailChimp](https://mailchimp.com/landers/email-marketing-platform/?ds_c=DEPT_AOC_Google_Search_UK_EN_Brand_Acquire_Exact_MKAG_UK&ds_kids=p77184324956&ds_a_lid=kwd-2285511033&ds_cid=71700000112280664&ds_agid=58700008474313140&gad_source=1&gclid=CjwKCAiA-vOsBhAAEiwAIWR0TUfY3feNzMQwqGg5DbYJWv79iRw8EukSsRr8wBOA3l4-OGa16TrqfBoC0_cQAvD_BwE&gclsrc=aw.ds)
Used to set up email marketing.

## Testing

User stories where crucial to testing to make sure each aspect of the website was fit for purpose.

#### HTML Validator
All HTML pages were run through the [W3C HTML Validator](https://validator.w3.org/). It passed with warnings.

![HTML Validator](/static/assets/images/hawksbill-heroes-html-validator.jpg)

#### CSS Validator

CSS was tested using [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input). The only issue was a warning as it could not validate part of the MailChimp form. However the rest of the code passed with no errors.

![CSS Validator](/static/assets/images/hawksbill-heroes-css-validator.jpg)

#### JavaScript

Javascript was passed through [JS Hint](https://jshint.com/) with two warnings.

![JSHint](/static/assets/images/hawksbill-heroes-jshint.jpg)

#### Pylint

[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/pylint-dev/pylint)

Python code was tested using Pylint, installed in the terminal using **pip install pylint** and ran using the command **pylint $(git ls-files '*.py')**. 

The overall score was 4.58/10.

#### Media Queries

Google Dev Tools was used to test the sites responsiveness on different media screens. The website was testing for all log in functions and purchasing on phones, tablets and laptops to ensure it kept consistant. On small screens some columns in the checkout pages had to be removed, this was done using CSS to remove the column if the screen was a set size.

### Bugs 

Several bugs appeared when trying to impliment stripe. This was solved by closely following the CodeInstitute video guides on Boutique Ado and with help from the tutor support team. 

As user login was done using custom forms, there was issues to relay back to the user if their details where incorrect for log in. This was solved using form errors rather than Django messages.

## Installing

### Create the Heroku App
- Log in to Heroku or create an account.
- On the main page click the button labelled New in the top right corner and from the drop-down menu select "Create New App".
- Enter a unique and meaningful app name.
- Next, select your region.
- Click on the Create App button.

### Attach the Postgres database
- In the Resources tab, under add-ons, type in Postgres and select the Heroku Postgres option.
- Copy the DATABASE_URL located in Config Vars in the Settings Tab.
- Go back to your IDE and install 2 more requirements:
    - `pip3 install dj_databse_url`
    - `pip3 install psycopg2-binary` 
- Create requirements.txt file by typing `pip3 freeze --local > requirements.txt`
- Add the DATABASE_URL value and your chosen SECRET_KEY value to the env.py file. 
- In settings.py file import dj_database_url, comment out the default configurations within database settings and add the following: 

```
DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
}
```
- Run migrations and create a superuser for the new database. 
- Create an if statement in settings.py to run the postgres database when using the app on heroku or sqlite if not

```
    if 'DATABASE_URL' in os.environ:
        DATABASES = {
            'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
        }
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
    }
```

- Create requirements.txt file by typing `pip3 freeze --local > requirements.txt`
- Create a file named "Procfile" in the main directory and add the following: `web: gunicorn project-name.wsgi:application`
- Add Heroku to the ALLOWED_HOSTS list in settings.py in the format ['app_name.heroku.com', 'localhost']

- Push these changes to Github.

### Update Heroku Config Vars
Add the following Config Vars in Heroku:

|     Variable name     |                           Value/where to find value                           |
|:---------------------:|:-----------------------------------------------------------------------------:|                     
| DATABASE_URL          | Postgres generated (as per step above)                                        |
| EMAIL_HOST_PASS       | Password from email client                                                    |
| EMAIL_HOST_USER       | Site's email address                                                          |
| SECRET_KEY            | Random key generated as above                                                 |
| STRIPE_PUBLIC_KEY     | Stripe Dashboard > Developers tab > API Keys > Publishable key                |
| STRIPE_SECRET_KEY     | Stripe Dashboard > Developers tab > API Keys > Secret key                     |
| STRIPE_WH_SECRET      | Stripe Dashboard > Developers tab > Webhooks > site endpoint > Signing secret |                         |

### Deploy
- NB: Ensure in Django settings, DEBUG is False
- Go to the deploy tab on Heroku and connect to GitHub, then to the required repository. 
- Scroll to the bottom of the deploy page and either click Enable Automatic Deploys for automatic deploys or Deploy Branch to deploy manually. Manually deployed branches will need re-deploying each time the repo is updated.
- Click View to view the deployed site.

The site is now live and operational.

## Forking this repository

- Locate the repository at this [link](https://github.com/debbie-herridge/bee-inkspired)
- At the top of the repository, on the right side of the page, select "Fork" from the buttons available.

A copy of the repository is now created.

## Cloning this repository

- Locate the repository at this [link](https://github.com/debbie-herridge/bee-inkspired)
- Under 'Code', see the different cloning options, HTTPS, SSH, and GitHub CLI. Click the preferred cloning option, and then copy the link provided.
Open Terminal.
- In Terminal, change the current working directory to the desired location of the cloned directory.
- Type 'git clone', and then paste the URL copied from GitHub earlier.
- Type 'Enter' to create the local clone.

## Acknowledgments

### Content
Images where sourced from [USplash](https://unsplash.com/).
Branding was created by the developer and turned into merchandise for the charity using [RedBubble](https://www.redbubble.com/explore/for-you/)

### Code 
Documents from [Django](https://www.djangoproject.com/) where a key componant to help write the code for this site.
Also the Boutique Ado project from [CodeInstitute](https://codeinstitute.net/full-stack-software-development-diploma/?utm_term=code%20institute&utm_campaign=CI+-+UK+-+Search+-+Brand&utm_source=adwords&utm_medium=ppc&hsa_acc=8983321581&hsa_cam=1578649861&hsa_grp=62188641240&hsa_ad=635720257674&hsa_src=g&hsa_tgt=kwd-319867646331&hsa_kw=code%20institute&hsa_mt=e&hsa_net=adwords&hsa_ver=3&gad_source=1&gclid=Cj0KCQjwtJKqBhCaARIsAN_yS_mInTq8p659q7gN0o4bX5Q1Zat1nQRvSXbjSrkPh2er3w1rYdFLlhQaAsDvEALw_wcB) helped with the shop on this website.
