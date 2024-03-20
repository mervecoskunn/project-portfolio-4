 # About 

This is a platform where everyone can share, post, comment and like restaurants, cafes and bars in Lund/Sweden. Its purpose is to help users share their experiences, discuss their ideas, and choose a venue if they wish based on the comments they see.

    ADD AM I RESPONSIVE SCREENSHOT !!!!
    
The Live Site can be found [here.](https://merve-project-4-dfec2093a369.herokuapp.com/)  

# Table of Contents
- [About](#about)
- [Table of Contents](#table-of-contents)
  - [User Experience](#user-experience)
  - [Admin](#admin)
  - [Member User](#member-user)
  - [General User](#general-user)
  - [Features](#features)
    - [Existing Features](#existing-features)
  - [Future Features](#future-features)
  - [Wireframes](#wireframes)
  - [Structure](#structure)
  - [Databases](#databases)
    - [Post Model](#post-model)
    - [Comment Model](#comment-model)
  - [Technologies Used](#technologies-used)
    - [Frameworks, Libraries \& Tools Used](#frameworks-libraries--tools-used)
  - [Testing](#testing)
- [Unit Testing](#unit-testing)
  - [Testing :](#testing-)
  - [Validator Testing:](#validator-testing)
  - [W3C Markup Validation Service](#w3c-markup-validation-service)
  - [CSS Validation Results](#css-validation-results)
  - [PEP8 Python Validator](#pep8-python-validator)
  - [BUGS](#bugs)
  - [User Story Testing](#user-story-testing)
  - [Deployment](#deployment)
    - [Steps to Deployment:](#steps-to-deployment)
    - [In the terminal](#in-the-terminal)
    - [In the setting.py](#in-the-settingpy)
    - [In the terminal](#in-the-terminal-1)
    - [Step 2: Deploying an app to Heroku](#step-2-deploying-an-app-to-heroku)
      - [Create the Heroku app](#create-the-heroku-app)
      - [Attach the Database:](#attach-the-database)
      - [In env.py](#in-envpy)
    - [In settings.py](#in-settingspy)
    - [In the terminal](#in-the-terminal-2)
    - [Get our static and media files stored on Amazon:](#get-our-static-and-media-files-stored-on-amazon)
      - [On Amazon](#on-amazon)
      - [In env.py](#in-envpy-1)
      - [In Heroku](#in-heroku)
      - [In settings.py](#in-settingspy-1)
    - [In Gitpod](#in-gitpod)
    - [In Procfile](#in-procfile)
    - [In Terminal](#in-terminal)
    - [In Heroku](#in-heroku-1)
  - [Credits](#credits)
  - [Acknowledgements](#acknowledgements)

## User Experience 

I designed this platform with desgin thinking approach. With only the necessary content/information. User can surf the site easily and get the information they are looking for. Please find all my defined user stories [here](https://github.com/mervecoskunn/project-portfolio-4/issues)

## Admin

  * As a Site Admin I can approve or disapprove posts so that I can filter out objectionable posts.
  * As a Site Admin I can create, read, update and delete posts so that I can manage my blog content.
  * As a Site Admin I can approve posts before it is published so that the site content will be consistent.

## Member User
  
  * As a Member User I can register an account so that I can manage my posts, comment and like.
  * As a Member User I can post/add/edit/delete posts so that I can share and manage my posts.
  * As a Member User I can like or unlike a post so that I can interact with the content.
  * As a Member User I can leave comments on a post so that I can be involved in the conversation.
  * As a Member User I can view my posts status of approval so that I can manage my posts.

## General User 
  
  * As a Site User I can view a list of posts so that I can select one to read.
  * As a Site User I can click on a post so that I can read the full text.
  * As a Site User / Admin user I can view comments on an individual post so that I can read the conversation.
  * As a Site User / Admin I can view the number of likes on each post so that I can see which is the most popular or viral.


## Features

### Existing Features 

- Home Page
  - Three posts representing categories were shared on the home page, so that users could access short and clear information about the site, and were supported with visuals. If the user wishes, they can easily list the posts belonging to the relevant category by clicking the button below. A short and clear guidance has been added on the screen so that they can Login/Register and like comments.
  
  ![Home Page](documentation/homepage-features.png)

  - When the visitor clicks on any category selected, it goes to the relevant category. 

  - Anyone who visits the page, whether they are a user or not, can go directly to the category if they click on the "Read More" button on the category posts on the main page.
    ![read more button](documentation/read-more-screenshots.png)

  - Visitor can create an account by clicking on login/register from the menu or from the button below.

  ![login-register-section](documentation/menu-login-register.png)

- Categories
  
  - When visitors click on the categories option in the menu, we encounter a dropdown menu and from there the visitors can select the option visitor wants and list the relevant posts.
  
  ![category select](documentation/category-select.png)

- Restaurant/Cafe/Bar Page
  
  - When the relevant category is selected, relevant posts are sorted.
   - Restaurant Page
   ![restaurant-page](documentation/restaurant-screenshot.png)
   - Cafe Page
    ![cafe-page](documentation/cafe-page-screenshot.png)
   - Bar Page
    ![bar-page](documentation/bar-page-screenshot.png)

- Post Detail Page
  
  - When visitor click on one of the listed posts, it will be seen in detail. If the visitor wants to comment or like, visitor must log in or register.
   
   ![post detail page ](documentation/post-detail-page-screenshot.png)

- Login Page
  
  - Visitor can login from the Login tab in the menu and comment, like or post can be shared.
  
   ![login page](documentation/login-screenshot.png)

- Register Page
  
  - A new account can be created from the register tab in the menu and thus can log in and use user features.
  
   ![register page](documentation/register-screnshot.png)

- My Page
 
  - On the My page, the user sees 3 buttons to navigate easily.
  - User can share new posts, view own posts, and edit or delete them if user wishes when user click the manage my posts button. If user clicks on the title of own post, user can view own post in detail.
  - User can log out using the logout button.
  
  ![My page](documentation/my-page-screenshot.png)

- Publish a Post 

  - Creating and adding a post by a registered user is possible.

  - The user can publish a post after signing in and from their profile page.

  - The user must enter a title, catogory, content and image.
  
  ![Publish post page](documentation/publish-post-screenshot.png)

  - Once the post is published, the post is submitted for approval to the admin. The submitted post can be viewed/edited/deleted by the owner from 'Manage my posts Page'.

- Manage My Posts Page
  
  - The user can see the list of their own posts from 'Manage My Posts' page
  - Each post listed has information about that particular post.
  - Post title, quote, and submission date/time are available separately for each submission.
  - Finally, buttons for editing and deleting options are provided for user management.
  - After the post is published, it is submitted to the administrator for approval. The submitted post can be viewed/edited/deleted by its owner from the 'Manage My Post'.
   
   ![Manage my posts ekran goruntusu ](ekran_goruntusu_dosya_adi.png)

- Edit Page
   
  - The user can select the post user wants to edit and edit it.
  - The authenticated and owner of the post can only edit the post.
  - The posts that are selected for editing are prepopulated form that is ready for editing.

   ![Edit page](documentation/edit-page-screenshot.png)
 
- Delete a Post

   - The authenticated and owner of the post can only delete the post.
   - The posts that are chosen to be deleted asks the user for confirmation by pop-up alert on the window.  
   ![Delete button](documentation/delete-button-post.png)

- Like and Comment on a Post 

  - All the site visiters can view the comments and the number of likes.

  - The unregistered site visiters cannot view the comment box to write a comment. Once they register, then it is visible for them and they can post a comment on any post they want.
  ![comment button](documentation/comment-section.png)

- Logout
 
  - The user can logout from Menu and from their accounts page.

  - When the user wants to logout a pop-up modal is triggered for confirmation.

  - The logout modal asks the user if they confirm to logout. 
  ![logout section](documentation/logout-screenshot.png)

## Future Features

 - Connect with Google translate API, so users can submit posts from different languages and also translate to language they want.
  - Members can save posts that they like (in save category) and go back to read it later.
  - Users can set up their own profile page, add information about themselves, upload a profile picture and connect with other members.
  - Create a community group and vote for their own admin/admins to review their posts.
  
## Wireframes

  - Each pages wireframes includes mobile(small screen), tablet(medium screen), desktop(large screens).
    - Home Page:  
   ![Home page](documentation/homepagebalsamiq.png)

    - Login Page:
    ![Login page](documentation/login-page-balsamiq.png)

    - Register Page:
      ![Register page wireframes](documentation/register-page-balsamiq.png)

    - Category Page:
      ![Category pages](documentation/restaurant-cafe-bar-page-balsamiq.png)

    - Post Page:
      ![Post detail page](documentation/post-detail-balsamiq.png)

    - My Page:
      ![My Page](documentation/my-account-page-balsamiq.png)

    - Publish Post Page:
      ![Publish post](documentation/publish-post.png)
    
    - My Publish Page:
     ![My publish page](documentation/my-publish-page-balsamiq.png)

## Structure
 
The idea behind the structure of Best Places Of Lund was to simply guide users visiting the site in a clear and understandable way.
Color confusion and unnecessary information were avoided

Throughout the project development, GitHub projects is used. Click[here](https://github.com/users/mervecoskunn/projects/7) to view the process.

## Databases
![Database Diagram](documentation/database_schema.png)

### Post Model

Post model handles posts details: title, content, date created/updated, featured image and likes. This post model handles the base for confirming user/author authentication to manage their own posts.

### Comment Model

Comment model handles the content of the comment, the username of the person commenting, date/time of commenting.

## Technologies Used
  * HTML
  * CSS
  * JavaScript
  * Python

### Frameworks, Libraries & Tools Used

  * Bootstrap 5 - grid, layout, columns, cards and forms structure.
  * Django - django frameworks to manage apps.
  * GitHub - to store the overall project repository.
  * GitPod - used as workspace to do the coding.
  * Balsamiq Wireframes - To design the wireframe of the complete project.
  * Google Fonts - Used for logo and all the written content.
  * Fontawesome - fontawesome icons for social media links and as additional design.
  * Heroku - for the deployement of the project.
  * Coolors - to choose the color palette and color shades.
  * PostgreSQL - database storage of the models.
  * Amazon - image and static files storage.
  * AmIResponsinve - responsiveness of the site.
  * Lighthouse - used for testing site functionality.
  * W3C Markup Validation Service - used for HTML testing.
  * W3C CSS Validation Service - used for CSS testing
  * PEP8 - used for Python files testing.

## Testing

# Unit Testing

I have used django TestCase for automated testing views, forms and models files.

## Testing : 

  - Testing Index/Home page view:
    ![Test home](documentation/homepage-test-code.png)
   - Category Model Test:
    ![Category model test](documentation/category-model-test.png)
    
   - Post Model Test:
    ![Post model test](documentation/post-model-test.png)

   - Comment Model Test:
    ![Comment model test](documentation/comment-model-test.png)

   - PostList View Test:
    ![Postlist view test](documentation/post-view-test.png) 

   - User Page View Test:
    ![User page view test](documentation/user-page-test.png)  

  - Result:
    ![result-terminal-screenshot](ekran_goruntusu_dosya_adi.png)

## Validator Testing:

- Lighthouse
  - Testing results:
    ![lighthouse-screenshot](ekran_goruntusu_dosya_adi.png)

## W3C Markup Validation Service
- Home Page:
  - index.html:
  ![home page screenshot](documentation/index.png)

  - pages/account/index.html:
    ![pages account screenshot](documentation/account.png)

  - pages/actions/post-create.html:
    ![result-terminal-screenshot](documentation/post-create.png)

  - pages/actions/post-edit.html:
     ![result-terminal-screenshot](documentation/post-edit.png)

  - pages/actions/posts.html:
    ![result-terminal-screenshot](documentation/posts.png)

  - pages/categories/bar/index.html:
    ![bar html validation](documentation/bar-html-validation.png)

  - pages/categories/cafe/index.html:
    ![cafe html validation](documentation/cafe-html-validation.png)
  
  - pages/categories/restaurant/index.html:
    ![restaurant html validation](documentation/restaurant-html-validation.png)
  
  ## CSS Validation Results

  The CSS validation results for the files used in the project are as follows:
    - Styles.css:
     ![css validation](documentation/css.png)

  ## PEP8 Python Validator
  - No errors or warnings found.
   
  - models.py:
    ![post model.py pep8 ](documentation/posts-model-py-screenshot.png)
  
  - admin.py:
    ![posts admin.py pep8](documentation/posts-admin-pep8.png)

  - posts urls.py:
    ![posts urls.py-screenshot](documentation/posts-urls-pt-screenshot.png)  

  - views.py:
    ![posts views.py pep8](documentation/posts-view-py-screenshot.png)
  
  - forms.py:
    ![posts forms.py pep8](documentation/posts-forms-py-screenshot.png)
   
  - home_tests.py:
    ![home test.py](documentation/home-test-py-screenshot.png)
  
  - model-tests.py:
    ![model-test.py-screenshot](documentation/model-py-screenshot.png)
  
  - pages.py-test:
    ![pages-test](documentation/pages-test-py-screenshot.png)

  - apps.py:
    ![apps.py-screenshot](documentation/apps-py-screenshot.png)  
  
  - asgi.py:
    ![asgi.py-screenshot](documentation/asgi-py-screenshot.png)

  - project-urls.py:
    ![project urls.py pep8](documentation/project-urls-py-screecshot.png)

## BUGS
 - I encountered a few errors on restaurant /cafe/bar html files during HTML validator testing and they were resolved.
  
  ![html validator bugs](documentation/bugs/restaurants-1.png)  

  ![html validator bugs](documentation/bugs/restaurants-2.png) 

  ![html validator bugs](documentation/bugs/restaurants-3.png)

## User Story Testing

- Admin
  - As a Site Admin I can approve or disapprove posts so that I can filter out objectionable posts.

  - As a Site Admin I can create, read, update and delete posts so that I can manage my blog content.

  - As a Site Admin I can aproove Posts before it is published so that the site content will be consistent. 
   
    ![admin-page-django-screenshot](documentation/admin-page-screenshot.png)

  - Member User
    - As a Member User I can register an account so that I can manage my posts, comment and like.  
    ![sign-up-screenshot](documentation/login-screenshot.png)

    - As a Member User I can post/add/edit/delete posts so that I can share and manage my posts.
    ![my-account-page-screenshot](documentation/my-page-screenshot.png)  
  
    - As a Member User I can like or unlike a post so that I can interact with the content.

    - As a Member User I can leave comments on a post so that I can be involved in the conversation.
  
   ![comment-section-screenshot](documentation/comment-section.png)

    - As a Member User I can view my posts status of approval so that I can manage my posts.
     ![manage-my-post-screenshot](documentation/edit-page-screenshot.png)
    

  - General User
    - As a Site User I can view a list of posts so that I can select one to read.
      
    ![home-page-screenshot](documentation/restaurant-screenshot.png)    
  
    - As a Site User I can click on a post so that I can read the full text.
     ![one-post-screenshot](documentation/post-detail-page-screenshot.png)

    - As a Site User / Admin user I can view comments on an individual post so that I can read the conversation.
    - As a Site User / Admin I can view the number of likes on each post so that I can see which is the most popular or viral. 
    ![one-post-commentscreenshot](documentation/comment-section.png)

  - Browser Compatability
    - Checked and verified that the site works on different browsers.
    - Safari:
    ![safari-screenshot](ekran_goruntusu_dosya_adi.png) 

  - Chrome:
    ![chrome-screenshot](ekran_goruntusu_dosya_adi.png)

- Responsiveness Testing

  - Desktop-Large Screen sizes:
  
  ![chrome-screenshot](ekran_goruntusu_dosya_adi.png)

  - Ipad - Medium Screen sizes:
  ![chrome-screenshot](ekran_goruntusu_dosya_adi.png)

  - Mobile - Small Screen Sizes:
  ![chrome-screenshot](ekran_goruntusu_dosya_adi.png)

## Deployment

This project was deployed to Heroku. "Heroku is a cloud platform that lets companies build, deliver, monitor and scale apps."[here](https://id.heroku.com/login)

- Steps to open account in Heroku:
  - [Signup here](https://signup.heroku.com/) if you do not have an account already.
  - ![signup-heroku.png](documentation/signup-heroku.png)
  - After you fill in all the information for account and sign in, you will be on [Dashbord](https://id.heroku.com/login). Here is where you will create an application. 
  - Click on New => Create new app.
    ![new-app.png](documentation/new-app.png)
  - Choose a name to your application and select location that you are based.
  
### Steps to Deployment: 

I have followed Code Institute's [Django Blog Cheat Sheet](https://codeinstitute.s3.amazonaws.com/fst/Django%20Blog%20Cheat%20Sheet%20v1.pdf) steps to follow, create and deploy the project on Herokuapps.
- Step 1: Installing Django and supporting libraries 

 ### In the terminal
     
  * Install Django and gunicorn: pip3 install django gunicorn
  * Install supporting libraries:	pip3 install dj_database_url psycopg2
  * Install Cloudinary Libraries	pip3 install dj3-cloudinary-storage
  * Create requirements file	pip3 freeze --local > requirements.txt
  * Create Project	django-admin startproject PROJ_NAME . (Don’t forget the . )
  * Create App	python3 manage.py startapp APP_NAME
  
  ### In the setting.py
  
  * Add to installed: apps	‘APP_NAME’,
   
 ### In the terminal
  
  * Migrate Changes: python3 manage.py migrate
  * Run Server to Test: python3 manage.py runserver

 ### Step 2: Deploying an app to Heroku

  - Create the Heroku app
  - Attach the database
  - Prepare our environment and settings.py file
  - Get our static and media files stored on
 
 

  #### Create the Heroku app
  1. Create new Heroku App
   ![create-heroku-app.png](documentation/create-new-app.png)

  2.  Copy DATABASE_URL - Located in the Settings Tab, in Config Vars, Copy Text
   
   ![config var](documentation/config-var.png)

  3. Add Database url link as confiq vars on Heroku from ElephantSQL
   ![add database heroku](documentation/database-link.png)
  
  #### Attach the Database: 

  - Create new env.py file on top level directory
 
   #### In env.py

  - Import os library : import os
  - Set environment variables: os.environ["DATABASE_URL"] = "Paste in Heroku DATABASE_URL Link"
  - Add in secret key: os.environ["SECRET_KEY"] = "Make up a randomSecretKey"
  
  - In Heroku.com
  
    - Add Secret Key to Config Vars: SECRET_KEY, “randomSecretKey”
  
  ### In settings.py
  
    - Reference env.py
    - Remove the insecure secret key and replace - links to the secret key variable on Heroku
    - Replace DATABASES Section (Comment out the old DataBases Section) - links to the DATATBASE_URL variable on Heroku 
  
  ### In the terminal
   - Make Migration: 
    - python3 manage.py migrate
  
  ### Get our static and media files stored on Amazon:
  #### On Amazon
  
  - Copy your Amazon_URL from Amazon Dashboard
  
  #### In env.py
  - Add Amazon URL to env.py - be sure to paste in the correct section of the link

  #### In Heroku

 - Add Amazon URL to Heroku Config Vars - be sure to paste in the correct section of the link
 - Add DISABLE_COLLECTSTATIC to Heroku Config Vars (temporary step for the moment, must be removed before deployment)
  ![disable_collecstatic](documentation/DISABLE_COLLECTSTATIC.png)

  #### In settings.py

  - Add Amazon Libraries to installed apps (note: order is important)
  - Tell Django to use Amazon to store media and static files. Place under the Static files Note
  - Link file to the templates directory in Heroku. Place under the BASE_DIR line
  - Change the templates directory to TEMPLATES_DIR. Place within the TEMPLATES array
  - Add Heroku Hostname to ALLOWED_HOSTS
  
  ### In Gitpod

  - Create 3 new folders on top level directory
   - media, static, templates 
  - Create procfile on the top level directory
   - Procfile
  
  ### In Procfile

  - Add code
   - web: gunicorn PROJ_NAME.wsgi
  
  ### In Terminal

  - Add, Commit and Push
   - git add .
   - git commit -m “Deployment Commit”
   - git push
  
  ### In Heroku
  - Deploy Content manually through heroku/
  - E.g Github as deployment method, on main branch
  ![heroku deploy manuel](documentation/heroku-deploy-manuel.png)

  Before the final Deployement: Remove the "DISABLE_COLLECTSTATIC" from Heroku Config vars, and Change Debug to "False" in settings.py

## Credits

- The contents in the posts were taken from the relevant websites.
- These site links are attached to the post detail page.
- Some content was written only by me.
- Photos used were taken from [www.pexels.com](https://www.pexels.com/)
- and some photos were taken from websites, they are free
- [Stack Overflow](https://stackoverflow.com/)
- [Django project documentation](https://www.djangoproject.com/)
- [Code Institute](https://codeinstitute.net/se/)
- [Bootstrap](https://getbootstrap.com/)
- [Django Allauth](https://docs.allauth.org/en/latest/)
- [Coolors](https://coolors.co/) color palette.
  ![colors](documentation/colors.png)
- [Am I Responsive](https://ui.dev/amiresponsive) 

 
## Acknowledgements

This project was created for Portfolio Project #4 (Full-Stack Tolkit) - Diploma in Full Stack Software Development Diploma at the Code Institute. I would like to thank my mentor Precious Ijege for relevant feedback during the project.

Merve COSKUN, 2024







