 # About 

This is a platform where everyone can share, post, comment and like restaurants, cafes and bars in Lund/Sweden. Its purpose is to help users share their experiences, discuss their ideas, and choose a venue if they wish based on the comments they see.

    
    
The Live Site can be found [here.](https://merve-project-4-dfec2093a369.herokuapp.com/)  

# Table of Contents
- [About](#about)
- [Table of Contents](#table-of-contents)
  - [User Experience](#user-experience)
  - [Admin](#admin)
  - [Member User](#member-user)
  - [General User](#general-user)
    - [Design Choices](#design-choices)
    - [Typography](#typography)
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
    - [Manuel Testing](#manuel-testing)
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
      - [On Amazon web service](#on-amazon-web-service)
      - [In env.py](#in-envpy-1)
      - [In Heroku](#in-heroku)
      - [In settings.py](#in-settingspy-1)
    - [In Visual Studio Code](#in-visual-studio-code)
    - [In Procfile](#in-procfile)
    - [In Terminal](#in-terminal)
    - [In Heroku](#in-heroku-1)
    - [How To Fork The Repository On GitHub](#how-to-fork-the-repository-on-github)
    - [Cloning And Setting Up This Project](#cloning-and-setting-up-this-project)
  - [Credits](#credits)
  - [Acknowledgements](#acknowledgements)

## User Experience 

I designed this platform with desgin thinking approach. With only the necessary content/information. User can surf the site easily and get the information they are looking for. Please find all my defined user stories [here](https://github.com/users/mervecoskunn/projects/7)

## Admin

  * As a Site Admin I can approve or disapprove posts so that I can filter out objectionable posts.
  * As a Site Admin I can create, read, update and delete posts so that I can manage my blog content.
  * As a Site Admin I can approve posts before it is published so that the site content will be consistent.
  * As the site admin, I can create or delete categories.
  * As the site admin, I can define users as super users.
  * As the site admin I can see the users and can delete or add new users if desired.
  * As the site admin I can see the all comments from all users and if it is need I can delete it.
  
  ![admin page](documentation/admin-page-screenshot.png)

## Member User
  
  * As a Member User I can register an account so that I can manage my posts, comment and like.
  * As a Member User I can post/add/edit/delete posts so that I can share and manage my posts.
  * As a Member User I can like or unlike a post so that I can interact with the content.
  * As a Member User I can leave comments on a post so that I can be involved in the conversation.
  * As a Member User I can edit or delete my comment. 
  * As a Member User I can view my posts status of approval so that I can manage my posts.

## General User 
  
  * As a Site User I can view a list of posts so that I can select one to read.
  * As a Site User I can click on a post so that I can read the full text.
  * As a Site User I can view comments on an individual post so that I can read the conversation.
  * As a Site User  I can view the number of likes on each post so that I can see which is the most popular or viral.
  * As a Site User I can register an account and login web site.

### Design Choices

 -  Color Schema
   The following colors were used for the color scheme. In general, simple and eye-friendly colors were preferred, so that the user could focus more on the content and posts.

   [Coolors](https://coolors.co/)color palette.

   ![Coolors](documentation/colors.png)

### Typography
 [Google Fonts](https://fonts.google.com/) 
 These three fonts, Bitter, Lato and Roboto, were used on the site. Since the site is generally aimed to be simple, legible and simple font families were chosen.

 ![bitter](documentation/bitter.png)
 ![lato](documentation/lato.png)
 ![roboto](documentation/roboto.png)

## Features

### Existing Features 

- Navigation

 The navigation bar is very clean and clear. Different menus appear for the site user depending on whether you are logged in or not.

  - Logout Menu Big Size
  
    ![logout menu big size](documentation/logout-menu.png)

  - Logout Menu Small Size 
  
     ![logout menu small size](documentation/logout-menu-small-size.png)

  - Login Menu Small Size
  
     ![login menu small size](documentation/login-small-size-menu.png)

  - Login Menu Big Size
  
     ![logoin menu big size](documentation/login-big-size-menu.png)      

- Home Page

  - Three posts representing categories were shared on the home page, so that users could access short and clear information about the site, and were supported with visuals. If the user wishes, they can easily list the posts belonging to the relevant category by clicking the button below. A short and clear guidance has been added on the screen so that they can Login/Register and like comments.
  
  ![Home Page](documentation/homepage-features.png)

  - When the visitor clicks on any category selected, it goes to the relevant category. 

  - Anyone who visits the page, whether they are a user or not, can go directly to the category if they click on the "Read More" button on the category posts on the main page.
  
    ![read more button](documentation/read-more-screenshots.png)

  - Visitor can create an account by clicking on login/register from the menu or from the button below.

  ![login-register-section](documentation/menu-login-register.png)

  - After logging in, the user is notified with a message.
  
   ![login-alert-message](documentation/login-alert-message.png)
  
  - After logging out, you will be greeted with the same message for logout.
  
   ![logout-alert-message](documentation/logout-alert.png)

  - Edit comment alert 
  
   ![edit comment alert](documentation/comment-alert-message.png)

  - Delete comment alert
    
    ![edit comment delete alert](documentation/delete-%20comment-success-alert.png)

 - Delete comment confirm message

  ![delete comment confirm message](documentation/delete-%20comment-confirm-message.png)

 - Comment create alert message

  ![comment create alert message](documentation/comment-create-success.png)

 - Register Success 
 - Post create success
 - Post delete success
 - Post edit success 
  
  In such cases, the user is also informed with alert messages.The user sees these warning messages for 5 seconds and then the messages disappear or the user can close them earlier by pressing the x sign.

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

  - If you visit the post detail page without logging in, there is a button that directs you to the login page to log in or register to comment.
   ![join to discussion](documentation/join-discussion.png)

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
  
  ![My page](documentation/my-page-last.png)

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
  - The user will be informed by message after the edit and delete operations.
   
   ![Manage my posts](documentation/manage-my-post.png)

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
  - Users can comment to all posts.
  
  ![comment button](documentation/comment-section.png)

  - User can edit or delete own comments and then user can see a message is done.
   
   ![alert-message-comment](documentation/comment-alert-message.png)

- Logout
 
  - The user can logout from Menu and from their accounts page.

  - When the user wants to logout a pop-up modal is triggered for confirmation.

  - The logout modal asks the user if they confirm to logout. 
  ![logout section](documentation/logout-screenshot.png)
  
  - When users loggout they will see a message logout is successful like other message login create post, create comment, edit post, edit comment, delete post, delete comment and register. 

- Footer
  
  Footer section was designed very simply and understandably. He was directed with icons to follow blog-related pages on social media.
  ![footer](documentation/footer.png)

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
Color confusion and unnecessary information were avoided.

The Best Places of Lund site is divided into two parts: When the user is logged in and When the user is logged in. Depending on the login status, the user is presented with different pages. When the user logs out, user can access the home page, all posts, categories, the detail page where user can read the post details, and the login/register pages. When the user logs in, the home page, all posts, categories, my page, and logout options can be accessed.

Read more about the different choices in the [Features](#features) section.

## Databases

[pgadmin4](https://www.pgadmin.org/docs/pgadmin4/latest/erd_tool.html)- I created database schema with pgadmin4.

![Database Diagram](documentation/database-schema.png)

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
  * [asgiref](https://pypi.org/project/asgiref/)- ASGI is a standard for Python asynchronous web apps and servers to communicate with each other, and positioned as an asynchronous successor to WSGI.
  * [Bootstrap 5](https://getbootstrap.com/docs/5.3/getting-started/introduction/) - grid, layout, columns, cards and forms structure.
  * [Django](https://pypi.org/project/Django/) - django frameworks to manage apps.
  * [gunicorn](https://pypi.org/project/gunicorn/) -- Gunicorn ‘Green Unicorn’ is a Python WSGI HTTP Server for UNIX. It’s a pre-fork worker model ported from Ruby’s Unicorn project. The Gunicorn server is broadly compatible with various web frameworks, simply implemented, light on server resource usage, and fairly speedy.
  * [GitHub](https://github.com/) - to store the overall project repository.
  * [Visual Studio Code](https://code.visualstudio.com/) - used as workspace to do the coding.
  * [Balsamiq Wireframes](https://balsamiq.com/) - To design the wireframe of the complete project.
  * [Google Fonts](https://fonts.google.com/) - Used for logo and all the written content.
  * [Fontawesome](https://fontawesome.com/) - fontawesome icons for social media links and as additional design.
  * [Heroku](https://www.heroku.com/github-students) - for the deployement of the project.
  * [Coolors](https://coolors.co/) - to choose the color palette and color shades.
  * [ElephantSQL](https://www.elephantsql.com/)PostgreSQL - database storage of the models.
  * [Amazon Web Service](https://aws.amazon.com/) - image and static files storage.
  * Lighthouse - used for testing site functionality.
  * [W3C Markup Validation Service](https://validator.w3.org/) - used for HTML testing.
  * [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) - used for CSS testing
  * [PEP8](https://pep8ci.herokuapp.com/) - used for Python files testing.

## Testing

### Manuel Testing

| Status | Main Website - User Logged Out                                |
| ------ | --------------------------------------------------------------| 
|   ✓    | Typing in a incorrect URL on the page loads the 404 error page|
|   ✓    | Pasting page that needs authentication loads a forbidden page |
|   ✓    | Clicking the nav logo loads the home page                     |
|   ✓    | Click the Home button and all categories are listed home page |
|   ✓    | Click on the category you want to see and list the posts      |
|   ✓    | Click one post and read more detail about this post           |
|   ✓    | See likes and comments on the post detail page                |
|   ✓    | If you want to comment, click the join discussion button.     |
|   ✓    | Clicking the other categories and list their posts            |
|   ✓    | Clicking the nav bar all posts and lists all posts            |
|   ✓    | Clicking the login section on nav bar and login page          |
|   ✓    | Clicking the register section on nav bar create an account    |
|   ✓    | Clicking the youtube icon on footer and visit youtube         |
|   ✓    | Clicking the facebook icon on footer and visit facebook       |
|   ✓    | Clicking the instagram icon on footer and visit instagram     |



| Status | Main Website - User Logged In                                |
| ------ | --------------------------------------------------------------| 
|   ✓    | Typing in a incorrect URL on the page loads the 404 error page|
|   ✓    | Pasting page that needs authentication loads a forbidden page |
|   ✓    | Clicking the nav logo loads the home page                     |
|   ✓    | Click the Home button and all categories are listed home page |
|   ✓    | Click on the category you want to see and list the posts      |
|   ✓    | Click one post and read more detail about this post           |
|   ✓    | See likes and comments on the post detail page                |
|   ✓    | Clicking the like icon and like post                          |
|   ✓    | Write one comment on comment section and save your own comment|
|   ✓    | Clicking comment edit icon and edit or delete your comment    |
|   ✓    | Clicking the other categories and list their posts            |
|   ✓    | Clicking the nav bar all posts and lists all posts            |
|   ✓    | Clicking the my page on navbar and go your page see two option|
|   ✓    | Click the publish post button and see create post page        |
|   ✓    | Click the manage my post button and list your posts           |
|   ✓    | Click the edit button on post edit your own post              |
|   ✓    | Click the delete button and delete your own post              |
|   ✓    | Click the publish post button and see create post page        |
|   ✓    | Clicking the youtube icon on footer and visit youtube         |
|   ✓    | Clicking the facebook icon on footer and visit facebook       |
|   ✓    | Clicking the instagram icon on footer and visit instagram     |
|   ✓    | Click the logout on navbar and see logout confirmation message|
|   ✓    | Click the logout button and see logout successful message     |



| Status | Main Website - Admin Logged In                                |
| ------ | --------------------------------------------------------------| 
|   ✓    | Clicking the login section on navbar and login as admin       |
|   ✓    | Clicking the nav logo loads the home page                     |
|   ✓    | Click the Home button and all categories are listed home page |
|   ✓    | Click on the category you want to see and list the posts      |
|   ✓    | Click one post and read more detail about this post           |
|   ✓    | See likes and comments on the post detail page                |
|   ✓    | Clicking the like icon and like post                          |
|   ✓    | Write one comment on comment section and save your own comment|
|   ✓    | Clicking comment edit icon and edit or delete your comment    |
|   ✓    | Clicking the other categories and list their posts            |
|   ✓    | Clicking the nav bar all posts and lists all posts            |
|   ✓    | Clicking the my page on navbar and go your page see two option|
|   ✓    | Click the publish post button and see create post page        |
|   ✓    | Click the manage my post button and list your posts           |
|   ✓    | Click the edit button on post edit your own post              |
|   ✓    | Click the delete button and delete your own post              |
|   ✓    | Click the publish post button and see create post page        |
|   ✓    | Clicking the youtube icon on footer and visit youtube         |
|   ✓    | Clicking the facebook icon on footer and visit facebook       |
|   ✓    | Clicking the instagram icon on footer and visit instagram     |
|   ✓    | Click the logout on navbar and see logout confirmation message|
|   ✓    | Click the logout button and see logout successful message     |
|   ✓    | Add the end of the url "/admin" and see django admin panel    |
|   ✓    | Clicking the categories and delete one category /add category |
|   ✓    | Clicking the comments and delete or add comments              |
|   ✓    | Click the posts on admin panel and create new posts or delete |
|   ✓    | Click the posts on admin panel and approve posts, delete, edit|
|   ✓    | Click the users on admin panel and create new users           |
|   ✓    | Click the users on admin panel and change their features      |
|   ✓    | Clicking the categories and delete one category /add category |


| Status | Create a Post - User Logged In                                |
| ------ | --------------------------------------------------------------| 
|   ✓    | Title field is required                                       |
|   ✓    | Title field does not accept empty field                       |
|   ✓    | Title field does not accept just spaces                       |
|   ✓    | Content field is required                                     |
|   ✓    | Content field does not accept empty field                     |
|   ✓    | Content field does not accept just spaces                     |
|   ✓    | Category field is required                                    |
|   ✓    | Category field does not accept empty field                    |
|   ✓    | Images field is required                                      |
|   ✓    | Clicking the create post button                               |
|   ✓    | Sending  to admin appove                                      |
|   ✓    | Clicking the my manage post on my page checking approval posts|



| Status | Create a New User - User Logged Out                           |
| ------ | --------------------------------------------------------------|
|   ✓    | Username field is required                                    |
|   ✓    | Username field does not accept empty field                    |
|   ✓    | Email field does not accept just spaces                       |
|   ✓    | Email field is request                                        |
|   ✓    | Password field does not accept empty field                    |
|   ✓    | Success flash message is displayed when the user submits the create a new user form|


| Status | Create a Profile Page  - User Logged In                       |
| ------ | --------------------------------------------------------------| 
|   ✓    | Username field is required                                    |
|   ✓    | Username field does not accept empty field                    |
|   ✓    | Email field does not accept just spaces                       |
|   ✓    | Email field is request                                        |
|   ✓    | Password field does not accept empty field                    |
|   ✓    | Success flash message is displayed when the user submits the create a register form|

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
    ![test cases result screenshot](documentation/test-result.jpeg)

## Validator Testing:

- Lighthouse
  - Testing results:
    ![lighthouse-screenshot](documentation/lighthouse-last.png)

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
  - As the site admin, I can access the Django-admin panel and log in as admin by adding "/admin" to the end of the url link and pressing the enter button again.
  - As a Site Admin I can approve or disapprove posts so that I can filter out objectionable posts.

  - As a Site Admin I can create, read, update and delete posts so that I can manage my blog content.

  - As a Site Admin I can aproove Posts before it is published so that the site content will be consistent. 
   
    ![admin-page-django-screenshot](documentation/admin-page-screenshot.png)

  - Member User
    - As a Member User I can login my account so that I can manage my posts, comment and like.  
    ![sign-up-screenshot](documentation/login-screenshot.png)
    
    - As a Member User I can post/add/edit/delete posts so that I can share and manage my posts.
    ![my page](documentation/my-page-last.png) 
  
    - As a Member User I can like or unlike a post so that I can interact with the content.
    - As a Member User I can leave comments on a post so that I can be involved in the conversation.
    - As a Member User I can edit my comment or delete.
    
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

    - As a Site User I can register an account and login if I want to share post or comment.
    ![register page](documentation/register-screnshot.png)

  - Browser Compatability
    - Checked and verified that the site works on different browsers.
  
    - Safari:
    ![safari-screenshot](documentation/safari-browser-capability.png) 

  - Chrome:
    ![chrome-screenshot](documentation/chrome-browser-capability.png)
  

- Responsiveness Testing

  - Desktop-Large Screen sizes:
  
  ![large screen check](documentation/largescreen.png)

  - Ipad - Medium Screen sizes
  
  ![ipad mini screen check](documentation/ipad-mini.png)

  - Mobile - Small Screen Sizes:
  
  ![chrome-screenshot](documentation/smallscreen.png)

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
  #### On Amazon web service
  
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
  
  ### In Visual Studio Code

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

### How To Fork The Repository On GitHub 

It is possible to do a independent copy of a GitHub Repository by forking the GitHub account. The copy can then be viewed and it is also possible to do changes in the copy without affecting the original repository. To fork the repository, take these steps:

After logging in to GitHub, locate the repository. On the top right side of the page there is a 'Fork' button. Click on the button to create a copy of the original repository.
 
- Github Fork 
   ![github fork](documentation/github_fork.png)

### Cloning And Setting Up This Project
To clone and set up this project you need to follow the steps below.

  - When you are in the repository, find the code tab and click it.
  - To the left of the green GitPod button, press the 'code' menu. There you will find a link to the repository. Click on the clipboard icon to copy the URL.
  - Use an IDE and open Git Bash. Change directory to the location where you want the cloned directory to be made.
  - Type 'git clone', and then paste the URL that you copied from GitHub. Press enter and a local clone will be created.

- Github Create Local Clone

 ![github colone](documentation/copy-github.png)
  
  - To be able to get the project to work you need to install the requirements. This can be done by using the command below:
   * pip3 install -r requirements.txt - This command downloads and install all required dependencies that is stated in the requirements file.

  - The next step is to set up the environment file so that the project knows what variables that needs to be used for it to work. Environment variables are usually hidden due to sensitive information. It's very important that you don't push the env.py file to Github (this can be secured by adding env.py to the .gitignore-file). The variables that are declared in the env.py file needs to be added to the Heroku config vars. Don't forget to do necessary migrations before trying to run the server.
   * python3 manage.py migrate - This will do the necessary migrations.
   * python3 manage.py runserver - If everything i setup correctly the project is now live locally.

- Setup env.py
  ![env.py set up](documentation/env-py.png)

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
- [Coolors](https://coolors.co/) color palette.

     ![colors](documentation/colors.png)

- [Amazon web service](https://aws.amazon.com/console/) I used AWS and I followed this page to implement it. [How to implementAWS to project](https://simpleisbetterthancomplex.com/tutorial/2017/08/01/how-to-setup-amazon-s3-in-a-django-project.html)

- The links I added below belong to their own websites related to the posts shared on the blog page. The content and free photographs from these pages were used.

- [Espresso House](https://espressohouse.com/)
- [Waynes Cafe](https://www.waynescoffee.se/)
- [Broder Jacobs](https://www.broderjakobs.se/)
- [Stortorget Bar](https://stortorget.bar/)
- [Ericssons Bar](https://ericssons.bar/)
- [Jhon Scott Lund](https://johnscotts.se/lund/)
- [la cucina](https://lacucina-lund.se/)
- [aiko sushi](https://www.aikosushi.se/)
- [rosegarden lund](https://rosegarden.se/locations/lundgrand)


- Template for read.me provided by Code Institute (with some additional changes that my mentor [Precious Ijege](https://www.linkedin.com/in/precious-ijege-908a00168/)) suggested.


## Acknowledgements

This project was created for Portfolio Project #4 (Full-Stack Tolkit) - Diploma in Full Stack Software Development Diploma at the Code Institute. I would like to thank my mentor Precious Ijege for relevant feedback during the project.

[Merve COSKUN](https://www.linkedin.com/in/merve-coskun-fullstack/), 2024







