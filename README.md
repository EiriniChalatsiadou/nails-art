## **Nails Art** ##

![responsive](/static/media/responsive.png)
## **FEATURES**
- ### **DESCRIPTION**
  
  This project designed and developed to create a useful experience for the clients of Nails Art. The users are given the possibility to explore and book a treatment and choose the staff member that they like to have the treatment too. <br>
  All these functionalities can be accessed by any user with an account, considering that the staff members have permissions for controlling the data.
  Nails Art was developed using Python (Django), HTML, CSS and JavaScript by storing the data in a PostgreSQL database.
  
  The fully deployed project can be accessed at [here](https://nails-art-06fcba4b6e97.herokuapp.com/)

## The header

  At the header, you can find the logo with the name of the site and also the Navigation bar through that you can have an easy navigation to the site.
  Also with the active menu item the page that selects the user is getting BOLD.
  The nav bar consists:
   - Home
   - Treatments
   - Book a treatment
   - Contact 
   - About us
   - Login/Register
![header](/static/media/header.png)


## Homepage

At homepage, the users can find a welcome content with a nice comment and as a background an image from the Studio.
![homepage](/static/media/homepage-README.png)

## Treatment page

At this page the users can find the treatments to make pretty their nails!
 The treatments consists: 
  - Shellac
  - Gel nails
  - Manicure
  - Pedicure
  
![treatment page](/static/media/treatments_screenshot.png)

## Book a treatment page

At this sectionauthe, the user can book a treatment.
The user can choose the treatment that pleasure, the date and the time and also the staff member that prefers.
Finally the user has the opportunity to update or cancel the booking.
![create](/static/media/create-appointment.png)

![upcoming](/static/media/upcoming-appointments.png)
![upcoming-first-time](/static/media/create-booking-first-time.png)
![edit-booking](/static/media/edit-booking.png)

## Contact page

At this section the user can find the contact details, the opening hours and also a map that pin to the address.
![contact](/static/media/contact-us.png)

## About us
At this page, the user can find a few words for Nails Art about the team.
Also has an image from the studio and see how comfortable is.
![about us](/static/media/aboutus.png)

## Login page

At this page, if the user already has an account, can put username and password and log in if authentication is successful.If the user doesnt have an account there is a link to register. User should't be logged in order this page to appear.
 ![login](/static/media/sign-in.png)

## Register page

User can create an account, by inserting username, password and optionally an email. User should't be logged in order this page to appear.
![register](/static/media/register.png)

## Logout page

User can log out. User should be logged in order this page to appear.
![logout](/static/media/sign-out.png)

## Footer

 At the footer, you can find the social media links for Facebook, Instagram and Twitter also the copyright for 2023.
![footer](/static/media/footer.png)


- ### **Tools used**

  - [Git](https://git-scm.com/) - for version control.
  - [Gitpod](https://www.gitpod.io/) - online IDE.
  - [GitHub](https://github.com/) - for host repository.
  - [Heroku](https://www.heroku.com/) - for deploying the project
  - [favicon](https://favicon.io/) - for favicon
  - [fontawsome](https://fontawesome.com/) - for creating icons
  - [Boostrap5](https://getbootstrap.com/) - creating responsiveness
  - [LucidChart](https://lucidchart.com/) - used for creating the Flowchart
  - [Google maps](https://www.google.com/) - used for creating the google map fr the contact details
  - [Cloudinary](https://cloudinary.com/) -  for storing static data
  


### **Languages Used**

  This tool is created using [Python](https://en.wikipedia.org/wiki/Python_programming_language)
 language. <br>
This tool is created using[SQL](https://en.wikipedia.org/wiki/SQL) language.<br>
 This tool is created using [HTML](https://en.wikipedia.org/wiki/HTML)language.<br>
 This tool is created using [CSS](<https://en.wikipedia.org/wiki/CSS>)
 language. <br>
 This tool is created using [javascript](https://en.wikipedia.org/wiki/JavaScript)
 language.<br>
 This tool is created using[JQuery](https://en.wikipedia.org/wiki/JQuery) language.

### **Libraries Used**

```
asgiref==3.7.2
dj-database-url==0.5.0
Django==3.2.20
django-allauth==0.54.0
gunicorn==21.2.0
oauthlib==3.2.2
psycopg2-binary==2.9.7
PyJWT==2.8.0
python3-openid==3.2.0
pytz==2023.3
requests-oauthlib==1.3.1
sqlparse==0.4.4
```

- [Git](https://git-scm.com/) For version control These commands were used for version control during project:
- git add . or git add -A: To add files before committing
- git commit -m: "type your message mentioning changes" - To commit changes to the local repository
- git push : To push all committed changes to the GitHub repository

- ### **VALIDATORS TESTING**

As advised by tutors, I validated Code Institute Python linter, html validator, css validator and Js validator

- [HTML](https://validator.w3.org) No errors were returned when passing through the official W3C validator
- [CSS](https://jigsaw.w3.org/css-validator/#validate_by_uri)
No errors were found when passing through the official validator
- [Js](https://jshint.com/)
  No errors were found when passing through the official validator
- [PEP8 validator](http://ww1.pep8online.com/) used for validating the python code

![css-validator](/static/media/css_validator.png)
![html-validator](/static/media/html-checker.png)
![js-validator](/static/media/jshint-checker.png)
![pep8-validator](/static/media/pep8.png)


## Running some tests:
 `python3 manage.py test`
 ![tests](/static/media/tests.png)


- ### **UNFIXIDED BUGS**
  - No bugs

- ### **DEPLOYMENT**
  - On [Heroku](https://www.heroku.com/) dashboard, select "New" and click "Create new app"
  - Create a unique app name
  - Select your region
  - Click "Create app"
  - Go to the settings tab:
  - Scroll down to the config vars section and select "Reveal Config Vars"
  - Add necessary config vars
  - In this case, in the key field enter "PORT" and the value field enter "8000"
  - Click "Add"
  - Scroll down to Buildpacks and click "Add buildpack"
  - Add the necessary buildpacks.
  - In this case, select "python" and click "Save changes"
  - Then, select "node.js" and click "Save changes"
  - Go to the Deploy tab:
  - Select GitHub and confirm connection to GitHub account
  - Search for the repository and click "Connect"
  - Scroll down to the deploy options
  - Select automatic deploys if you would like automatic deployment with each new push to the GitHub    repository
  - In manual deploy, select which branch to deploy and click "Deploy Branch"
  - Heroku will start building the app
  - The link to the app can be found at the top of the page by clicking "Open app"
  - The link can be found

- ### **FLOWCHART**
 - The Flowchart for my program was created using LucidChart and represents how the project works.
   ![flowchart](/static/media/flowchart.png)

- ### **SURFACE**

- Color Scheme

  - rgb(207, 186, 202)
  
  ![color-1](/static/media/color-1.png)
  
  -  #220622 
  
  ![color-2](/static/media/color-2.png)
  
  - rgb(227, 214, 220)
  
  ![color-3](/static/media/color-3.png)

  - #773c85
  - 
  ![color-4](/static/media/color-4.png)

  
  - Visual effect
  for the box-shadow:
    - rgba(17, 16, 16, 0.19) 0px 10px 20px
    - rgba(19, 15, 15, 0.23) 0px 6px 6px
  
  - Fonts 
  The fonts I used for the site are:
   - Gabriola, sans
   - Copperplate, fantasy


- ### **AGILE METHODOLOGY**
   The project was developed by Agile methodology.
   The implementation progress was registered by [Jira](https://www.atlassian.com/software/jira)
   The tasks were accomplished, there moved to Jira from to do, to in Progress, Tests and Done lists.
    - - examples of Jira:
  ![Jira](/static/media/jira-1.png) - ![Jira](/static/media/jira-2.png) - 

- ### **CREDITS**

- Content
  
  The content of the site is fictive. it's only for the project.
  
- Media
  - [freepngimg.com](https://freepngimg.com/png/61049-watercolor-what-color-nail-cosmetics-polish-painting/icon) - favicon and Logo
  - [pinterest.ie](https://www.pinterest.ie/pin/633740978953200202/) - Homepage background image
  - [pinterest.ie](https://www.pinterest.ie/pin/733664595561243125/) - About us page
  - [beepmix.com](https://spa.beepmix.com/API/v1.0/uploads/1629309542_755897661_60_a.jpeg) Treatment page
  - [google.com](https://www.google.com/search?q=background+images&tbm=isch&ved=2ahUKEwjgjYzK9dGAAxWfTkEAHeZlD18Q2-cCegQIABAA&oq=background+&gs_lcp=CgNpbWcQARgCMgQIIxAnMgQIIxAnMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgARQ8RhY7Shg7ztoAHAAeACAATeIAboEkgECMTKYAQCgAQGqAQtnd3Mtd2l6LWltZ8ABAQ&sclient=img&ei=scDUZKDxGJ-dhbIP5su9-AU&bih=743&biw=1440#imgrc=5P7GDAt5_8PXSM>) - Brick background image for details, about us and Login/register
  - [fontawesome.com](https://fontawesome.com/icons/twitter?f=brands&s=solid) - for the social media in footer
  - [fontawesome.com](https://fontawesome.com/icons/instagram?f=brands&s=solid) - for the social media in footer
  - [fontawesome.com](https://fontawesome.com/icons/facebook?f=brands&s=solid) - for the social media in footer
  - [fontawesome.com](https://fontawesome.com/v5/icons/edit?f=classic&s=solid) - for the edit button on booking page
  - [fontawesome.com](https://fontawesome.com/icons/trash?f=classic&s=solid) - for the delete button on booking page
  - [stackoverflow](https://stackoverflow.com/)
  - [w3schools](https://www.w3schools.com/)
  - [geeksforgeeks](https://www.geeksforgeeks.org/)
 

- ### **ACKNOWLEDGEMENTS**

     I'd like to thank my mentor, Akshat Garg, for providing advices and feedback for this project. Also the tutors and the students for the comments to Slack.
   
 
