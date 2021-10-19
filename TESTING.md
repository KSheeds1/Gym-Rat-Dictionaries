 # Testing documentation for Gym Rat Dictionaries
 ## Contents: 
 * [Testing User Stories](#testing-user-stories)
  * [Bugs: discovered & resolved during development](#bugs:-dicovered-&-resolved-during-development)
  * [Manual functionality testing](#manual-functionality-testing)
	* [User Authentication](#user-authentication)
	* [CRUD Operations](#crud-operations)
	* [Cancel functionality](#cancel-functionality)
	* [Features](#features) 
  * [Responsive Testing](#repsonsive-testing)
  * [Validation Testing](#validation-testing)
  * [Lighthouse performance](#lighthouse-performance) 

# Testing User Stories:
***As a regular user, I want to be able to:***
* **UST1: *Login and out of my account:***
A registered user can login to their account my clicking on 'Log In' located in the Navigation Bar on the right hand side. To log out of their account they must be logged into the account, navigate to the navigation bar and click on 'Log Out'.

* **UST2: *Upload an exercise definition:*** 
Registered users can click create or add a definition from three places, once logged in, they can either click on the '+' icon in the navigation bar or the '+' icon FAB located on the bottom right hand corner of the screen. Otherwise, they can navigate to their 'Profile' page from the navigation and click on the button to 'Add a Definition'. 

* **UST3: *View all my uploaded exercises in one place:***
Once logged in users can navigate to their 'Profile' page from the Navigation bar and view their uploaded definitions from there. 
 
* **UST4: *Save or add all my favourite definitions to 'My Favourites':***
Once logged in, users can simply click on the 'Add to Favourites' icon featured on each individual definition card panel to add a definition to their favourites. They can then view their favourites on their profile page. 

* **UST5: *'Like' or 'upvote' a definition:***
Logged in users can 'upvote' a definition by simply clicking on the 'upvote' button featured on each individual definition card panel, also the amount of upvotes seen on the button will increase by one.
 
* **UST6: *Edit or delete any definition I have added:***
A logged in user can choose to edit or delete any of their own added definitions. To do so, they can simply navigate to their profile from the navigation bar and view their 'My Definitions'. Each card panel has two buttons, 'Edit' & 'Delete'. 
	* To edit a definition, a user can click the 'Edit' button, which will redirect them to the 'Edit Definition' form and will be able to make the edit to the definition, they can either choose to save the changes or cancel. 
	* To delete a definition, a user can click on the 'Delete' button attached to each definition card panel. They will be prompted to confirm the action once, to delete they can click the 'Delete' button offered in the user-confirmation modal or they can choose to 'Cancel' and the profile page will reload. 

***As a first-time user, I want to be able to:***
* **UST7: *Identify the different categories of definitions available on the app:***
First-time users can browse the different categories of exercise definitions by clicking on the 'Categories' nav-item and selecting a category they wish to browse from the dropdown.

* **UST8: *Search for a particular definition quickly:***
Casual users of the site can search for a particular definition quickly by using the search bar, which can be accessed in two places, the Navigation bar or the magnify glass icon FAB located on the bottom right hand side of the app.
   
* **UST8: *Create an account if I like the content of the site:***
First-time users can create an account or register with the app by navigating to the nav-bar and clicking on the nav-item for 'Register'. From there they will be prompted to create a unique username and to provide a validated password. The user will know that they have succeeded in creating an account as they will be redirected to their new profile page and will see a successful registration flash message. 

* **UST9: *To share a definition on my Facebook or Instagram account:***
Even casual, first-time users can choose to share a definition from GRD to their social media account, this can be achieved by clicking on the share icon featured on each individual definition card panel and choosing from the options made available. 

* **UST10: *To quickly find a definition while I'm at the gym:*** 
Anyone can quickly find a definition on the go by accessing the site and searching for the definition using the search bar located in either the nav-bar of the FAB. If the definition has been added, it will return in the search request, if it has not been added, the app will inform the user thusly. 

***As the site owner/Admin, I want to be able to:***
* **UST11: *Add a new workout type category to the site:***
Adding a new category to the app is restricted to both the site owner and admin. Once logged in as either, they can navigate to the 'Categories' from the navigation bar and click on the card panel that reads 'Add New Category', from their they can fill out the form to create a new category and select to 'Create' or 'Cancel'.

* **UST12: *Edit an existing workout type category:***
This functionality is restricted to both the site owner and admin. To edit a category, navigate to the categories section, click on the nav-item 'Categories'. Once redirected to the categories page, the admin or site owner will have the option to click on the 'Edit' button offered on each category. Once selected, fill out the 'Edit' form and make the necessary changes. If they want to save the changes select the 'Save' button or to cancel the changes, select 'Cancel'. 

* **UST13: *Delete an existing workout type category:*** 
This functionality is restricted to both the site owner and admin. To delete an existing category, navigate to the categories section, click on the nav-item 'Categories'. Once redirected to the categories page, the admin or site owner will have the option to click the 'Delete' button attached to each category. Once clicked the user will be prompted to confirm the action prior to deletion, they can choose to either delete or cancel the deletion. 

* **UST14: *Provide the functionality to users to allow them to 'save' their favourite definitions to 'My Favourites':***
Logged in users can simply click on the 'Add to Favourites' icon featured on each individual definition panel to add a definition to their favourites. They can then view their favourites on their profile page. 


# Bugs: discovered & resolved during development:
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

# Manual functionality testing:

## User Authentication: 
### Registration functionality:
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

### Log In functionality:
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


# CRUD OPERATIONS
## Create/Add :
### Add Definition:
Following the completion of add_definition functionality, manual testing was carried out against the functionality. It was tested in the following manner:
 
 * Click on 'Add Definition' in the Navbar.
 * Once redirected to add definition form, fill out field inputs and click 'Add Definition' button.
 * User is informed of a successful creation by the Flash message and is redirected to the home page.
INSERT IMG OF FORM AND FLASH MESSAGE

### Add Category: [Admin only]
Following the completion of the add_category functionality, manual testing was carried out against the functionality. It was tested in the following manner:
* Navigate to 'Category Management' via the navbar.
* Click on the 'Add Category' panel.
* Admin is redirected to the add category form.
* Fill out the necessary input fields.
* Click 'Add Category' button.
* Following a successful category creation, the category management page is reloaded and the admin is provided with user confirmation via a Flash message. 
INSERT IMG OF FORM AND FLASH MESSAGE 

## Read:
Users of the app have the ability to read data in the following areas of the site:

**Home page:**
* Recently added definitions.

**Categories:**
* Different categories available across the site, access and read definitions refined by category.

**User profile:**
* User created definitions.
* User favourites. 

ADD IMG OF ALL OF THE ABOVE

## Update/Edit: 
### Edit Definition:
Following the completion of the edit_definition functionality, manual testing was carried out against the functionality. It was tested in the following manner:
**Note:** Edit functionality is restricted to the users own definitions. 

* Select the definition you wish to edit.
* Click on the 'Edit' button available on the definition card panel.
* Once redirected to the edit definition form, make the necessary edits to the definition. 
* Click the 'Edit Definition' button to update the definition. 
INSERT IMG OF FORM AND FLASH MESSAGE

### Edit Category: [Admin only]
Following the completion of the edit_categories functionality, manual testing was carried out against the functionality. It was tested in the following manner:
* Navigate to 'Category Management' via the navbar.
* Select the category to edit.
* Edit the existing data in the edit category form.
* Click on 'Edit Category' button.
* Following a successful edit, the category management page is reloaded and the admin is provided with user confirmation via a Flash message.
INSERT IMG OF FORM AND FLASH MESSAGE 

## Delete:
Delete functionality/operations are available across the following areas of the app: 

**Delete definition:**
Each individual definition card panel has a 'Delete' button. Prior to the deletion of a definition, a user will be prompted to provide user confirmation via a modal. Users can delete their own definitions in the following manner:
	
* Navigate to the definition you wish to delete. 
* Click the 'Delete' button.  
* Confirm action via the modal.
* The user will be redirected back to their profile and will receive user feedback via a Flash message. 

**Note:** The ability to delete a user added definition has also been extended to Admins. To delete a user added definition, admins also follow the steps outlined above. 

**Delete category:  [Admin only]**

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
 

## Responsive Testing:

## Validation Testing:

## Lighthouse Performance: 