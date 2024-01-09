# Hawksbill Heroes

![Hawksbill Heroes Logo](/static/assets/images/hawksbill-heroes-nav-logo.jpg)

Hawksbill Heroes is a organisation raising funds to aid in the mission of keeping Hawksbill Sea Turtles from going extinct. The site currently features a merchandise shop where users can purchase items and a personalised dashboard where they can see their orders.

The site is targeted towards envirnomentally concious people some of whom will already know about the Hawksbill Turtles but for others it will teach them about the animal, explain the dangers they are facing and what they can do to help.

This website does take payments using Stripe; Please note that the website is for project purposes only, do not enter any personal credit/debit cards when placing orders. You can find a list of dummy cards to use under Stripes documentation [here](https://stripe.com/docs/testing#cards).

View the deployed app here.

![Image to show the website on different media screens](/static/assets/images/am-i-responsive.jpg)

## UX

### User stories

#### First time users
For first time users the goal of the site is to:
- Spread awareness of Hawksbill turtles, who they are and why they are going extinct.
- Provide knowledge on what I can do to help.
- Learn what the charity is doing to help.
- Be able to contribute to the cause.

#### Returning users
Returning users are able to log in and:
- See previous orders.
- Make new orders with ease.

### Design
The design is minimilistic with many photos of the turtles to showcase their beauty. The colour scheme is colour picked from the images, with the header and footer being a green/blue tone to match the water and the soft beige background body matching the turtles body.

![Colour palette chosen for website](/static/assets/images/color-palette.jpg)

### Wireframes

![Homepage Wireframe](/static/assets/images/hawksbill-heroes-wireframe-homepage.jpg)
![Login Wireframe](/static/assets/images/hawksbill-heroes-wireframe-login.jpg)
![Turtles Wireframe](/static/assets/images/hawksbill-heroes-wireframe-turtles.jpg)
![Merchandise Wireframe](/static/assets/images/hawksbill-heroes-wireframe-merchandise.jpg)
![Checkout Wireframe](/static/assets/images/hawksbill-heroes-wireframe-checkout.jpg)

### Features

#### Current features
The site boasts clean consistant styling throughout the site. 

#### Future features
- Donation page
- Turtle subscription and adoption

#### CRUD



## Marketing strategies
The target market are animal lovers who are environment cautious. As this is a Charity there is a limited marketing budget, as consumers would want their donations to be used on the turtles and not marketing, therefore the charity adopts creative and cost-effective strategies, such as using images of the turtles on social media and community events.

## Database 

![Database schema](/static/assets/images/hawksbill-heroes-dataschema.jpg)

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
I choose font Bricolage Grotesque for the whole site with a back up font of Sans Serif.
- [JQuery](https://jquery.com/)
JQuery is used with Bootstrap for the Navagation bar to make it responsive.
- [Git](https://git-scm.com/)
Git is used to commit and Push code to GitHub.
- [GitHub](https://github.com/)
Used to store code for this project after being pushed from Git.
- [Canva](https://www.canva.com/posters/0)
Used to make the website logo for the navigation bar and merchandise logo.



- [Django](https://www.djangoproject.com/) 
- [ElephantSQL](https://www.elephantsql.com/)
- [Cloudinary](https://cloudinary.com/ip/gr-sea-gg-brand-home-base?utm_source=google&utm_medium=search&utm_campaign=goog_selfserve_brand_wk22_replicate_core_branded_keyword&utm_term=1329&campaignid=17601148700&adgroupid=141182782954&keyword=cloudinary&device=c&matchtype=e&adposition=&gad_source=1&gclid=CjwKCAiA-P-rBhBEEiwAQEXhH2ndeczu952BxiEy0n2brT63DR2X09OuugdQMRhehy0gXScT3VM9VxoCldEQAvD_BwE) 
- [Heroku](https://www.heroku.com/)
- [LucidChart](https://lucid.app/)
- [Chrome Dev Tools](https://developer.chrome.com/docs/devtools)
- [Font awesome](https://fontawesome.com/)
- [Google fonts](https://fonts.google.com/)
- [GitPod](https://gitpod.io/workspaces)
- [Favicon](https://favicon.io/)
- [Pylint](https://pypi.org/project/pylint/)
- [Grammerly](https://www.grammarly.com/service/download)

## Testing

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

### Prepare the environment and settings.py file
- In your GitPod workspace, create an env.py file in the main directory.
- Add the DATABASE_URL value and your chosen SECRET_KEY value to the env.py file.
- Update the settings.py file to import the env.py file and add the SECRETKEY and DATABASE_URL file paths.
- Comment out the default database configuration.
- Save files and make migrations.
- Add Cloudinary URL to env.py
- Add the Cloudinary libraries to the list of installed apps.
- Add the STATIC files settings - the URL, storage path, directory path, root path, media URL and default file storage path.
- Link the file to the templates directory in Heroku.
- Change the templates directory to TEMPLATES_DIR
- Add Heroku to the ALLOWED_HOSTS list in the format ['app_name.heroku.com', 'localhost']

### Create files/directories
- Create requirements.txt file
- Create three directories in the main directory; media, storage and templates.
- Create a file named "Procfile" in the main directory and add the following: web: gunicorn beeinkspired.wsgi

### Update Heroku Config Vars
Add the following Config Vars in Heroku:

- SECRET_KEY value
- CLOUDINARY_URL
- PORT = 8000
- DISABLE_COLLECTSTATIC = 1

### Deploy

Ensure in Django settings, DEBUG is False

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
