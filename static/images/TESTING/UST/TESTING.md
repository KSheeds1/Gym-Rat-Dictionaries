 # Testing documentation for Gym Rat Dictionaries
 ## Contents: 
* [Testing User Stories](#testing-user-stories)
* [Bugs: discovered & resolved during development](#bugs:-discovered-&-resolved-during-development:)
* [Manual functionality testing](#manual-functionality-testing)
	* [User Authentication](#user-authentication)
	* [CRUD Operations](#crud-operations)
	* [Cancel functionality](#cancel-functionality)
	* [Features](#features) 
* [Responsive Testing](#repsonsive-testing)
* [Validation Testing](#validation-testing)
* [Lighthouse performance](#lighthouse-performance) 

# Testing User Stories:
## ***As a regular user, I want to be able to:***
> ### **UST1: *Login and out of my account:***

A registered user can login to their account by clicking on 'Log In' in the Navigation Bar on the right hand side. To log out of their account, they must be logged into their account, navigate to the navigation bar and click on 'Log Out'.

![Login navbar](static/images/TESTING/UST-login.png)
![Login page](static/images/TESTING/UST-login-2.png)

> ### **UST2: *Upload an exercise definition:*** 

Once logged in, registered users can add a definition from three places:
* 'Add Definition' nav-link
* The '+' icon in the floating action button
* 'Add Definition' button on their profile page

![Add definition - navbar](static/images/TESTING/UST-add-def.png)
![Add definition - FAB](static/images/TESTING/UST-add-def-2.png)
![Add definition - form](static/images/TESTING/UST-add-def-form.png)

> ### **UST3: *View all my uploaded exercises in one place:***

Once logged in, users can navigate to their 'Profile' page from the Navigation bar and view their uploaded definitions from there.

![My definitions](static/images/TESTING/UST-view-my-defs.png)

 
> ### **UST4: *Save or add all my favourite definitions to 'My Favourites':***

Once logged in, users can simply click on the 'Add to Favourites' icon featured on each individual definition card panel to add a definition to their favourites. They can then view their favourites on their profile page. 

![My Favourites](static/images/TESTING/UST-view-my-faves.png)

> ### **UST5: *'Upvote' or 'Downvote' a definition:***

Logged in users can 'upvote' or 'Downvote' a definition by simply clicking on the thumbs up or down icon featured on each individual definition card panel, the amount of votes for both are displayed on the icon and incremented by one when clicked.

![Up/Down vote](static/images/TESTING/UST-up-down-vote.png)
 
> ### **UST6: *Edit or delete any definition I have added:***

A logged in user can choose to edit or delete any of their own added definitions. This can be achieved across the site:
* On the users profile
* On the home page
* On any of the category pages
* By searching for a specific definition in the search bar and deleting the definition in the search results. 

 Each card panel has two buttons, 'Edit' & 'Delete'. 
	* To edit a definition, a user can click the 'Edit' button, which will redirect them to the 'Edit Definition' form. From there, they will be able to edit the pre-existing data, and choose to save the changes or cancel. 
	* To delete a definition, a user can click on the 'Delete' button attached to each definition card panel. They will be prompted to confirm the action once, to delete they can click the 'Delete' button offered in the user-confirmation modal or they can choose to 'Cancel' and the profile page will reload.

![Edit/Delete - Profile](static/images/TESTING/UST-edit-delete-2.png)
![Edit/Delete - Home pg](static/images/TESTING/UST-edit-delete.png)
![Edit definition form](static/images/TESTING/UST-edit-def-form.png)
![Delete definition](static/images/TESTING/UST-delete-confirm.png)

## ***As a first-time user, I want to be able to:***
> ### **UST7: *Identify the different categories of definitions available on the app:***

First-time users can browse the different categories of exercise definitions by clicking on the 'Categories' nav-item and selecting a category they wish to browse from the dropdown. This will direct them to the specific category collection.

![Category menu](static/images/TESTING/UST-see-categories.png)
![Category pg](static/images/TESTING/UST-view-category.png)

> ### **UST8: *Search for a particular definition quickly:***

Casual users of the site can search for a particular definition quickly by using the search bar, which can be accessed in two places: 
* From the magnify glass icon in the Navigation bar, which triggers the search bar 
* The magnify glass icon FAB located on the bottom right hand side of the app, which scrolls the user to the top and triggers the search bar. 

![Search - Nav](static/images/TESTING/UST-search-bar.png)
![Search - Fab](static/images/TESTING/UST-search-fab.png)

> ### **UST8: *Create an account if I like the content of the site:***

First-time users can create an account or register with the app by navigating to the nav-bar and clicking on the nav-item for 'Register'. From there they will be prompted to create a unique username and to provide a validated password. The user will know that they have succeeded in creating an account as they will be redirected to their new profile page and will see a successful registration flash message. 

![Register - Nav](static/images/TESTING/UST-register.png)
![Register - Form](static/images/TESTING/UST-register-2.png)

> ### **UST9: *To share a definition on my Facebook or Instagram account:***

Even casual, first-time users can choose to share a definition from GRD to their social media account, this can be achieved by clicking on the share icon featured on each individual definition card panel and choosing from the options made available in the share modal. 

![Share icon](static/images/TESTING/UST-share-2.png)
![Share modal](static/images/TESTING/UST-share.png)

> ### **UST10: *To quickly find a definition while I'm at the gym:***

Anyone can quickly find a definition on the go by accessing the site and searching for the definition using the search bar. This can be accessed from the magnify icon in the nav-bar or in the floating action buttons. If the definition has been added, it will be returned in the search request, if it has not been added, the app will inform the user thusly. 

![Search Nav](static/images/TESTING/UST-quick-find-2.png)
![Search FAB](static/images/TESTING/UST-quick-find.png)

## ***As the site owner/Admin, I want to be able to:***
> ### **UST11: *Add a new category to the site:***

Adding a new category to the app is restricted to both the site owner and admin. Once logged in as either, they can navigate to the 'Category Management' page from the navigation bar and click on the card panel that reads 'Add New Category'. From there they can fill out the form to create a new category and select to 'Create' or 'Cancel' if they decide not to add a new category.

![Add new category btn](static/images/TESTING/UST-add-new-cat.png)
![Add new category form](static/images/TESTING/UST-add-new-cat-form.png)


> ### **UST12: *Edit an existing workout type category:***

This functionality is restricted to both the site owner and admin. To edit a category, navigate to Category Management, by clicking on the nav-item 'Category Management'. Once redirected to the page, the admin or site owner will have the option to click on the 'Edit' button offered on each category panel. Once selected, an admin can edit the pre-existing data in the 'Edit Category form'. If they wish to save the changes select the 'Edit Category' button or to cancel the changes, select 'Cancel'. 

![Edit category btn](static/images/TESTING/UST-edit-cat-btn.png)
![Edit category form](static/images/TESTING/UST-edit-cat-form.png)

> ### **UST13: *Delete an existing workout type category:*** 

This functionality is restricted to both the site owner and admin. To delete an existing category, navigate to the Category Management page from the nav-bar. Once redirected to the page, the admin or site owner will have the option to click the 'Delete' button attached to each category. Once clicked, the user will be prompted to confirm the action prior to deletion, they can choose to either delete or cancel to be redirected to the category management page. 

![Delete category btn](static/images/TESTING/UST-edit-cat-btn.png)
![Delete category modal](static/images/TESTING/UST-delete-cat-confirm.png)



# Bugs discovered and resolved during development:

## **Loss of functionality to 'add' and 'edit' buttons:**
A loss of functionality for the buttons featured on the add_definition and edit_definition forms was discovered following the completion of the POST method for the edit_definition form. When manually testing the edit_definition function, by updating a definition the 'edit' button would not send the updated definition to the database.
Nor would the 'add' button on the add_definition form add a definition to the database. 

With no errors being thrown, I check over both the add_definition and edit_definition functions in app.py but everything seemed in order, both form templates were rendering so I turned to the HTML for both templates. After running both forms through the [W3C Markup Validation Service](https://validator.w3.org/#validate_by_input) an error was thrown for the form tags surrounding the image_url input field on both forms that 'nested forms are not allowed'. 
INSERT IMGS TO DO WITH THIS BUG

Upon removal of the nested form, the functionality of both the 'add' and 'edit' buttons on their respective forms was restored. 


## **Multiple 'delete' buttons added to definitions created by admin:**
A bug was discovered when an admin user added a definition to the site. Once redirected back to the home page, the new definition card had two delete buttons. The conditional formatting put in place at the time to restrict access to the 'edit' and 'delete' buttons was as follows:
INSERT IMG OF ORIGINAL CF HERE

* If the session user created the definition, they had access to edit or delete the definition. 
* Admins were also granted permission to delete user added definitions as a means of removing malicious or unrelated content from the site. 

However, the template logic put in place was flawed, as the likely occurrence of an admin adding a definition to the site was overlooked. The conditional formatting that had been implemented was ill-defined, and so, was refactored.
INSERT IMG OF REFACTORED CODE HERE

Access to both the edit and delete functionality was granted under the following specifications: 
* If the session user created the definition. 
OR  
* If the session user is an admin AND created the definition.
 ELSE IF
 * If the session user is an admin (they will have access to the delete function on all user added definitions.)

The refactoring of the conditional formatting resolved the bug. 

## **Loss of functionality to add and edit form's category select input:**

Following the implementation of the @app.context_processor and the category_pg function there was a loss of functionality for both category select inputs on the add and edit forms. 
The categories to choose from in the add definition form were no longer available and the pre-existing category in the edit from was also gone. 

INSERT IMG OF THE TWO SELECTS

Initially it was believed that the issue was due to the fact that the select inputs were actually `<ul><li>` structures and shared the same 'dropdown-content' class as the navbar and sidenav dropdown menus.
INSERT IMG OF DEV TOOLS PIC WITH CSS

 However, after reviewing both functions in app.py, it became clear that the bug arose from attempting to reuse lists in Jinja, the for-loop of 'categories' was now listed three times. To rectify the bug, the .find() functions in both add_definition and edit_definition were wrapped inside a python list to convert the Mongo cursor objects 'categories' into proper lists. Following this, functionality returned to both forms. The pre-existing category selection for edit was readily available, as were the category selection options in the add definition form. 
 IMG OF REFACTORED CODE FOR BOTH ADD EDIT FUNCTIONS.

## **Displaying user favourites on profile page:**
An issue arose when attempting to display user favourites on the profile page. A user's favourites are saved to an array 'user_favourites' in the users collection. While the definitions were being updated into the array, and filtered for-loops were employed in profile.html to display only session user created definitions and user favourite definitions all attempts to display the user favourite definitions were unsuccessful. 

The bug was discovered while reviewing the profile function. Initially "username" was being passed through, which only pointed to a string. In order to resolve the bug the profile view was altered to gain access to all user document fields by passing through the Mongo Object "user" and the projection parameter was removed from the find method. This allowed for all definitions to be accessible from the profile page and then filtered by the for-loops. The changes made to the profile view, resolved the bug and both session user created definitions and their favourite definitions were now displaying on the profile page.   
INSERT IMGS FOR THIS

### **Pagination bugs:**
Three routes for the project were refactored to include pagination: 
* get_definitions
* categories_pg
* search

When first implemented, the pagination seemed functional, definition panels per page were limited and the pagination links were in working order on definitions.html and category_pg.html. However when attempting to search an error was thrown pointing at the if statement in definitions.html
INSERT IMG TYPE ERROR CURSOR NO LEN
Following some research of this issue, a suitable fix was found in this [Stack Overflow question.](https://stackoverflow.com/questions/65477524/flask-and-jinja-template-throwing-error-object-of-type-cursor-has-no-len)
To resolve the TypeError  the 'definitions' lists were changed to return a cursor object and the if statements were updated also. 
INSERT IMG OF DEFINITIONS.HTML .COUNT() 
These changes to the code seemed to rectify the issue and all aspects of the Flask pagination seemed to be functional. These changes were then pushed to Git. 

However, when later returning to development again, and attempting to save a definition to 'favourites', an error was thrown and new bug had appeared. While the definition was being added to the user_favourites array in the User collection, the profile page was no longer accessible.
INSERT IMG OF DEFINITIONS NOT DEFINED. 

Upon reviewing the app.py file and definitions.html it was decided that this bug was due to the change from lists to cursor objects, 'definitions' was no longer iterable more than once. The decision was made to return the cursor objects to lists and attempt to deal with the search functionality differently. Once this change had been made, functionality was returned. Even access to the search functionality also seemed possible, however when attempting to view the second page of search results an error was thrown:
INSERT IMG OF SEARCH RESULTS ERROR THROWN

Some research and guidance was necessary to resolve this bug. Initially, the plan to resolve this issue was to build a second route to split the search functionality. Maintain the original route as a post request, the initial search query and build a second route to deal with the pagination and subsequent requests. However this was abandoned for a much more straightforward approach. 

It was decided to keep the current pagination and just change the form from `POST` to `GET`. Following this approach, the `GET` method passes the query term into the URL args, using `request.args.get()` to get it from the args, to search the database and paginate. So the query cannot be lost from the args upon pagination. The following alterations were made to the code to implement this: 
INSERT IMG OF ARGS IN SEARCH() AND GET IN DEF SEARCH FORM. 

Following this all aspects of pagination were manually tested and all bugs and issues surrounding pagination had been resolved. 

# Manual functionality testing:

# User Authentication: 

## **Registration functionality:**
Following completion of the function register(), the function and form were tested manually. The functionality was tested in the following manner: 

1. Attempt registration by providing **neither** a username or password and clicking on the 'Register' button.:
	INSERT PIC HERE
	**Result:** User is prompted to fill in the fields. 
	
2. Attempt registration with an **invalid** username and **valid** password:
INSERT PIC HERE
**Result:** User is prompted to 'Please match the format requested', the form validation or pattern recognition required has not been met for the username. 

3. Attempt registration by submitting the form filling out both inputs with nothing but spaces:
INSERT PIC HERE
**Result:** User is again prompted to 'Please match the format requested' and the form validation and pattern recognition are throwing errors. 

4. Attempt registration with a **valid** username and an **invalid** password:
INSERT PIC HERE
**Result:** User is prompted to 'Please match the format requested'. The form validation and pattern recognition are throwing errors for the password. 

5. Attempt registration with a **valid** username and **valid** password: 
INSERT PIC HERE
**Result:**  The form validation and pattern recognition are accepting both the username and password, the user is redirected to their profile and receive a flash message of 'Registration Successful'. 

## **Log In functionality:**
Following completion of the function login(), the function and form were tested manually. The functionality was tested in the following manner: 

1. Attempt login by providing **neither** a username or password and clicking on the 'Register' button.:
	INSERT PIC HERE
	**Result:** Neither form validation or pattern recognition requirements have been met. The user is prompted to fill in the fields.
	 
2. Attempt login with an **invalid** username and **valid** password:
INSERT PIC HERE
**Result:** The form redirects back to the login page and the user is informed by the flash message that either an incorrect username or password have been entered. 

3. Attempt login by submitting the form filling out both inputs with nothing but spaces:
INSERT PIC HERE
**Result:** User is again prompted to 'Please match the format requested' and the form validation and pattern recognition are throwing errors. 

4. Attempt login with a **valid** username and an **invalid** password:
INSERT PIC HERE
**Result:** The form redirects back to the login page and the user is informed by the flash message that either an incorrect username or password have been entered. 

5. Attempt login with a **valid** username and **valid** password: 
INSERT PIC HERE
**Result:**  The form validation and pattern recognition are accepting both the username and password, the user is redirected to their profile and receive a flash message of 'Welcome {username}'.

## **Log Out functionality:** 
Following completion of the function logout(), manual testing was carried out against the functionality. The functionality was tested in the following manner:

**1. Log in as user and logout:**
INSERT PIC HERE

**Results:** Once logged in as a user, the changes in the nav-items is apparent, a regular user has access to the following nav-items: 
* Home
* Profile
* Add Definition
* Categories
* Log Out

The users login status can be confirmed in 'Cookies' found in the 'Application' section of Dev Tools, as the 'session cookie' is present. To logout the user clicks on the 'Log Out' nav-item and receives a flash message to inform them that they have been logged out and are redirected to login page. Checking against Dev Tools 'Cookies', it's noted that the session cookie has been deleted. 



**2. Log in as admin and logout:** 
INSERT PIC HERE

**Results:** Once logged in as an admin, the changes in the nav-items is apparent, an admin has access to the following nav-items:
* Home
* Profile
* Add definition
* Category Management
* Log Out

The admin's login status can be confirmed in 'Cookies' found in the 'Application' section of Dev Tools, as the 'session cookie' is present. To logout the admin clicks on the 'Log Out' nav-item and receives a flash message to inform them that they have been logged out and are redirected to login page. Checking against Dev Tools 'Cookies', it's noted that the session cookie has been deleted.



# CRUD OPERATIONS
## **Create/Add:**
### Add Definition:
Following the completion of add_definition functionality, manual testing was carried out against the functionality. It was tested in the following manner:
 
 * Click on 'Add Definition' in the Navbar.
 * Once redirected to add definition form, fill out field inputs and click 'Add Definition' button.
 * User is informed of a successful creation by the Flash message and is redirected to the home page.
INSERT IMG OF FORM AND FLASH MESSAGE

### Add Category: **Admin only**
Following the completion of the add_category functionality, manual testing was carried out against the functionality. It was tested in the following manner:
* Navigate to 'Category Management' via the navbar.
* Click on the 'Add Category' panel.
* Admin is redirected to the add category form.
* Fill out the necessary input fields.
* Click 'Add Category' button.
* Following a successful category creation, the category management page is reloaded and the admin is provided with user confirmation via a Flash message. 
INSERT IMG OF FORM AND FLASH MESSAGE 

## **Read:**
Users of the app have the ability to read data in the following areas of the site:

**Home page:**
* Recently added definitions.

**Categories:**
* Different categories available across the site, access and read definitions refined by category.

**User profile:**
* User created definitions.
* User favourites. 

ADD IMG OF ALL OF THE ABOVE

## **Update/Edit:** 
### Edit Definition:
Following the completion of the edit_definition functionality, manual testing was carried out against the functionality. It was tested in the following manner:
**Note:** Edit functionality is restricted to the users own definitions. 

* Select the definition you wish to edit.
* Click on the 'Edit' button available on the definition card panel.
* Once redirected to the edit definition form, make the necessary edits to the definition. 
* Click the 'Edit Definition' button to update the definition. 
INSERT IMG OF FORM AND FLASH MESSAGE

### Edit Category: **Admin only**
Following the completion of the edit_categories functionality, manual testing was carried out against the functionality. It was tested in the following manner:
* Navigate to 'Category Management' via the navbar.
* Select the category to edit.
* Edit the existing data in the edit category form.
* Click on 'Edit Category' button.
* Following a successful edit, the category management page is reloaded and the admin is provided with user confirmation via a Flash message.
INSERT IMG OF FORM AND FLASH MESSAGE 

## **Delete:**
Delete functionality/operations are available across the following areas of the app: 

### Delete definition:

Each individual definition card panel has a 'Delete' button. Prior to the deletion of a definition, a user will be prompted to provide user confirmation via a modal. Users can delete their own definitions in the following manner:
	
* Navigate to the definition you wish to delete. 
* Click the 'Delete' button.  
* Confirm action via the modal.
* The user will be redirected back to their profile and will receive user feedback via a Flash message. 

**Note:** The ability to delete a user added definition has also been extended to Admins. To delete a user added definition, admins also follow the steps outlined above. 

### Delete category:  **Admin only**

Admins have the ability to delete categories as they see fit, each category panel has a 'Delete' button. Prior to the deletion of a category, the admin will be prompted to provide user confirmation via a modal. Admins can delete a category in the following manner: 
* Navigate to the 'Category Management' using the navbar.
* Select the category you wish to delete. 
* Click the 'Delete' button on the selected panel.
* Upon deletion of the category, the category management page will reload and the admin will be informed of a successful deletion through a Flash message. 
* The deleted category will have been removed from the page. 
INSERT PIC OF CATEGORY DELETION

## Cancel functionality: 
The ability to 'cancel' is available across the following areas of the app:

**Add definition form:**
If a user chooses not to add a new definition they can click on the 'Cancel' button on the add definition form and will be redirected back to the home page.
INSERT IMG OF CANCEL BUTTON

**Edit definition form:**
If a user chooses not to edit an existing definition, they can click on the 'Cancel' button on the edit definition form and will be redirected back to the home page.
INSERT IMG OF CANCEL BUTTON

**Delete definition confirmation modal:**
Prior to the deletion of a definition, a user will be prompted to provide user confirmation via a modal. If the user chooses not to delete a definition, they can click the 'Cancel' button and be redirected back to the home/profile page.
INSERT IMG OF DELETION MODAL  

**Add category form: [Admin only]**
If an admin chooses not to add a new category, they can click on the 'Cancel' button on the add category form and will be redirected back to the category management page.
INSERT IMG OF CANCEL BUTTON

**Edit category form: [Admin only]**
If an admin chooses not to edit an existing category, they can click the 'Cancel' button on the edit category form and will be redirected back to the category management page.
INSERT IMG OF CANCEL BUTTON

**Delete category confirmation modal: [Admin only]**
Prior to the deletion of a category, the admin will be prompted to provide user confirmation via a modal. If an admin chooses not to delete a category, they can click on the 'Cancel' button and will be redirected back to the category management page. 
INSERT IMG OF DELETION MODAL 
 

 ## **Base.html**

| **Element**                 | **Action** | **Expected Outcome**                                        | **Pass/Fail** | **Notes**                                                             |
|-------------------------|--------|---------------------------------------------------------|-----------|-------------------------------------------------------------------|
| **Navbar**                  |        |                                                         |           |                                                                   |
| Navbar Brand            | Click  | Redirect to home                                        | Pass      |                                                                   |
| Home                    | Click  | Redirect to home                                        | Pass      |                                                                   |
| Profile                 | Click  | Redirect to Profile                                     | Pass      |                                                                   |
| Categories              | Click  | Opens dropdown menu for category selection              | Pass      | Only available to users not Admin                                 |
| Add Definition          | Click  | Redirects to Add definition form                        | Pass      | Only available if user is logged in                               |
| Category Management     | Click  | Redirect to Category Management                         | Pass      | Only available to Admin users                                     |
| Log In                  | Click  | Redirect to Log In page                                 | Pass      | Not visible if user is logged in                                  |
| Log Out                 | Click  | Logs user out of account, redirecting to Log In page    | Pass      | Only visible if user is logged in                                 |
| Register                | Click  | Redirects to register page                              | Pass      | Not visible if user is logged in                                  |
| **SideNav**                 |        |                                                         |           |                                                                   |
| Hamburger Icon          | Click  | Opens sidenav menu                                      | Pass      | Available on smaller viewports.                                   |
| Navbar Brand            | Click  | Redirects to home page                                  | Pass      |                                                                   |
| Home                    | Click  | Redirects to home page                                  | Pass      |                                                                   |
| Profile                 | Click  | Redirects to profile page                               | Pass      | Only available to logged in users                                 |
| Categories              | Click  | Opens dropdown categories menu                          | Pass      | Only available to users not admin                                 |
| Add Definition          | Click  | Redirects to Add definition form                        | Pass      | Only available if user is logged in                               |
| Category Management     | Click  | Redirects to category management                        | Pass      | Only available to Admin users                                     |
| Log In                  | Click  | Redirects to log in page                                | Pass      | Not available to logged in users                                  |
| Log Out                 | Click  | Logs user out and redirects to login page               | Pass      | Only available if user is logged in                               |
| Register                | Click  | Redirects to register page                              | Pass      | Not visible to logged in users                                    |
| **Section**                 |        |                                                         |           |                                                                   |
| Message Flashing        | Click  | Displays user feedback across site                      | Pass      |                                                                   |
| Floating Action Buttons | Click  | Displays icons for search, add definition and scroll up | Pass      | Add definition functionality is only available to logged in users |
| Search                  | Click  | Renders search bar to screen                            | Pass      |                                                                   |
| Add definition          | Click  | Redirects to add definition form                        | Pass      | Only available to logged in users                                 |
| Scroll to the top       | Click  | Automatically scrolls user back to the top of the page  | Pass      |                                                                   |
| **Footer**                  |        |                                                         |           |                                                                   |
| Facebook Link           | Click  | Opens Facebook in a new tab                             | Pass      |                                                                   |
| TikTok Link             | Click  | Opens Tiktok in a new tab                               | Pass      |                                                                   |
| Instagram Link          | Click  | Opens Instagram in a new tab                            | Pass      |                                                                   |
| Youtube                 | Click  | Opens Youtube in a new tab                              | Pass      |                                                                   |

## **Definitions.html:**
| **Element**                | **Action** | **Expected Output**                                                          | **Pass/Fail** | **Notes**                                                                        |
|------------------------|--------|--------------------------------------------------------------------------|-----------|------------------------------------------------------------------------------|
| **Search**             |   |                                                              |     || Search Bar             | Search | Input search query                                                       | Pass      |                                                                              |
| Search Btn             | Search | Triggers search of database using query                                  | Pass      |                                                                              |
| Reset Btn              | Reset  | Redirects to the home page definition.html                               | Pass      |                                                                              |
| **Definition Card Panel**  |        |                                                                          |           |                                                                              |
| Add to favourites icon | Click  | Triggers add_to_favourites and saves definition to user_favourites array | Pass      | Only available to logged in users, will trigger redirect to login            |
| Share icon             | Click  | Triggers share modal and presents platforms to share to                  | Pass      |                                                                              |
| Upvote icon            | Click  | Increments the upvote count for a specific definition                    | Pass      | Only available to logged in users                                            |
| Downvote icon          | Click  | Increments the downvote count for a specific definition                  | Pass      | Only available to logged in users                                            |
| Tooltips               | Hover  | Provide further information on icons when icon is hovered over           | Pass      |                                                                              |
| Edit Btn               | Click  | Redirects to edit definition form                                        | Pass      | Only available to logged in users                                            |
| Delete Btn             | Click  | Triggers delete confirmation modal                                       | Pass      | Must click 'Delete' on confirmation modal to delete, available to admin also |
| **Modals**                 |        |                                                                          |           |                                                                              |
| Share Modal            | Click  | Click social media platform you wish to share on                         | Pass      | Triggered by share icon                                                      |
| Facebook link          | Click  | Opens Facebook in new tab                                                | Pass      |                                                                              |
| TikTok link            | Click  | Opens TikTok in new tab                                                  | Pass      |                                                                              |
| Instagram link         | Click  | Opens Instagram in new tab                                               | Pass      |                                                                              |
| Youtube link           | Click  | Opens Youtube in new tab                                                 | Pass      |                                                                              |
| Cancel Btn             | Click  | Closes modal                                                             | Pass      |                                                                              |
| Delete Modal           | Click  | Confirm to delete specific definition                                    | Pass      | Triggered by Delete btn                                                      |
| Delete Btn             | Click  | Triggers delete_definition function and deletes specific definition      | Pass      |                                                                              |
| Cancel Btn             | Click  | Closes modal                                                             | Pass      |
| **Pagination**             |   |                                                              |     |                                                                              |
| << Btn                 | Click  | Redirects back to previous definitions page                              | Pass      |                                                                              |
| Pagination Links       | Click  | Numbered buttons to redirect to specific page                            | Pass      |                                                                              |
| >> Btn                 | Click  | Redirects forward to next definitions page                               | Pass      |                                                                              |


## **Add_definition.html:**
| **Element**            | **Action** | **Expected Output**                                        | **Pass/Fail** | **Notes**                                                                              |
|--------------------|--------|--------------------------------------------------------|-----------|------------------------------------------------------------------------------------|
| **Form**              | POST   | Fill out and submit definition to database             |           |                                                                                    |
| Category Dropdown  | Click  | Reveals category options to choose from                | Pass      | Required                                                                           |
| Input text fields  | Type   | Text appears, green line if validated, red line if not | Pass      | Required                                                                           |
| Textarea           | Type   | Text appears, green line if validated, red line if not | Pass      | Required                                                                           |
| URL upload         | Click  | Paste in URL for image to upload with definition       | Pass      | Not required                                                                       |
| Tooltips           | Hover  | Provide further instruction for form fields            | Pass      |                                                                                    |
| Add definition Btn | Click  | Submits definition to the database                     | Pass      | Form will not submit if not correctly validated and all required fields filled out |
| Cancel Btn         | Click  | Cancel action and redirects back to home page          | Pass      |                                                                                    | 

## **Edit_definition.html:**
| **Elements**                 | **Action** | **Expected Output**                                                 | **Pass/Fail** | **Notes**                                                 |
|--------------------------|--------|-----------------------------------------------------------------|-----------|-------------------------------------------------------|
| **Form**                     | POST   | Edit specific definition form and update in database                       | Pass      | Filled with pre-existing data to be edited as chosen |
| Category select dropdown | Click  | Reveals category selection options                              | Pass      | Required                                              |
| Input text fields        | Type   | Text appears, green line if validated, red line if not          | Pass      | Required                                              |
| Textarea                 | Type   | Text appears, green line if validated, red line if not          | Pass      | Required                                              |
| Tooltip                  | Hover  | Provides further instruction for form fields                    | Pass      |                                                       |
| URL image upload         | Click  | Include URL of image to upload with definition                  | Pass      | Not required                                          |
| Edit Btn                 | Click  | Triggers edit_definition function and uploads edited definition | Pass      |                                                       |
| Cancel Btn               | Click  | Cancels edit of definition, redirects back to home page         | Pass      |                                                       |


## **Categories.html:**
| **Elements**                 | **Action** | **Expected Output**                                                 | **Pass/Fail** | **Notes**                                                 |
|--------------------------|--------|-----------------------------------------------------------------|-----------|-------------------------------------------------------|
| **Category Card**    |        | Holds the edit/delete btns for category management                    |           |       |
| Edit Btn         | Click  | Triggers edit_category function and redirects to edit category form   | Pass      |       |
| Delete Btn       | Click  | Triggers deletion confirmation modal                                  | Pass      |       |
| Delete Modal     | Click  | Triggered by delete btn, confirmation is required prior to deletion   | Pass      |       |
| Delete Btn       | Click  | Triggers delete_definition function and deletes a specific definition | Pass      |       |
| Add Category Btn | Click  | Triggers add_category function and redirects to add category form     | Pass      |       |

## Category_pg.html:
| **Elements**         | **Action** | **Expected Output**                                                       | **Pass/Fail** | **Notes**                                             |
|------------------|--------|-----------------------------------------------------------------------|-----------|---------------------------------------------------|
| **Category_pg**      |        | Dynamically generates category page upon selection from dropdown menu | Pass      |                                                   |
| Card Panel       |        | Definition panels refined by category                                 |           |                                                   |
| Upvote icon      | Click  | Increments upvote count                                               | Pass      | Users must be logged in to use this functionality |
| Downvote icon    | Click  | Increments downvote count                                             | Pass      | Users must be logged in to use this functionality |
| **Pagination**             |   |                                                              |     |
| << Btn           | Click  | Redirect to previous page                                             | Pass      |                                                   |
| Pagination Links | Click  | Numbered buttons to redirect to specific page                         | Pass      |                                                   |
| >> Btn           | Click  | Redirect to next page                                                 | Pass      |                                                   |


## **Edit_category.html:**
| **Element**           | **Action** | **Expected Output**                                           | **Pass/Fail** | **Notes**                                           |
|-------------------|--------|-----------------------------------------------------------|-----------|-------------------------------------------------|
| **Form**              | POST   | Edit specific category form and submit to database        | Pass      | Filled with pre-existing data to edit as chosen |
| Input text fields | Type   | Text appears, green line if validated, red line if not    | Pass      | Required                                        |
| Tooltip          | Hover  | Provides further instruction for form fields            | Pass      |          |
| Edit Btn          | Click  | Triggers submission of edited category                    | Pass      |                                                 |
| Cancel Btn        | Click  | Cancels edit of category and redirects to get_categories  | Pass      |                                                 |

## **Login.html:**
| **Element**          | **Action** | **Expected Output**                           | **Pass/Fail** | **Notes**    |
|------------------|--------|--------------------------------------------------------|-----------|----------|
| Form             | POST   | Log In form, logs in user to site                      | Pass      |          |
| Input text field | Type   | Text appears, green line if validated, red line if not | Pass      | Required |
| Tooltip          | Hover  | Provides further instruction for form fields            | Pass      |          |
| Log In Btn       | Click  | Submit btn logs user into the app                      | Pass      |          |
| Register Link    | Click  | Redirects unregistered user to register.html           | Pass      |          |
 
## **Registration.html:**
| **Element**          | **Action** | **Expected Output**                           | **Pass/Fail** | **Notes**    |
|------------------|--------|---------------------------------------------------------|-----------|----------|
| Form             | POST   | Registration form to sign up site visitor               | Pass      |          |
| Input text field | Type   | Text appears, green line if validated, red line if not  | Pass      | Required |
| Tooltip          | Hover  | Provides further instruction for form fields            | Pass      |          |
| Register Btn     | Click  | Submits registry information to the database            | Pass      |          |
| Log In Link      | Click  | Redirect to Log In page for previously registered users | Pass      |          |


## **Profile.html:**
| **Element**          | **Action** | **Expected Output**                           | **Pass/Fail** | **Notes**    |
|-----------------------|--------|-------------------------------------------------------------------------|-----------|-------|
| Collapsible Accordian |        | Displays user created definitions                                       | Pass      |       |
| Edit Btn              | Click  | Triggers edit_definition function and redirects to edit form            | Pass      |       |
| Delete Btn            | Click  | Triggers delete modal for specific definition                           | Pass      |       |
| Modal                 |        | User confirmation for definition deletion                               |           |       |
| Delete Btn            | Click  | Triggers delete_definition function and deletes specific definition     | Pass      |       |
| Cancel Btn            | Click  | Modal close                                                             | Pass      |       |
| Collapsible Accordian |        | Displays user favourite definitions                                     | Pass      |       |
| Delete Btn            | Click  | Triggers delete modal for specific user favourite                       | Pass      |       |
| Edit Btn              | Click  | Triggers edit_definition function and redirects to edit definition form | Pass      |       |
| Modal                 |        | User confirmation for definition deletion                               | Pass      |       |
| Delete Btn            | Click  | Triggers delete_definition function and deletes specific definition     | Pass      |       |
| Cancel                | Click  | Modal close                                                             | Pass      |       |
| Add definition Btn    | Click  | Redirects to add_definition form                                        | Pass      |       |

## Responsive Testing:

## Validation Testing:

## Lighthouse Performance: 