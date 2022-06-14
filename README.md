# Awwards

##### By Florence Wambui


![Homepage](/static/images/homepage.png)



#### Description
In this application user/developer is able to post/upload his project and also rates other people projects depending on the design, userbility, and content.



#### API EndPoints    
[Profile API EndPoints]()

[Projects API EndPoints]() 


#### Technology Used

The following languages have been used on this project:

- HTML
- CSS
- Bootstrap
- Python
- Django
- PostgreSQL



- Live link to view the project <a target="_blank" href="">Awwards</a>


#### User Stories
These are the behaviours/features that the application implements for use by a user.

Users would like to:
* View all projects submitted by any user.
* Click on links to visit a live site.
* Search for Project by title.
* Must be signed up to vote.
* See averages of projects as voted by other users.
* Rate Projects.


#### Admin Abilities
These are the behaviours/features that the application implements for use by the admin.

Admin should:
* Sign in to the application
* Add, Edit and Delete projects
* Delete projects
* Manage the application.


#### Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Admin Authentication | **On demand** | Access Admin dashboard |
| Display all projects| **Home page** | Click links to visit site|
| To add an project  | **Through Admin dashboard and Authenticated Users Homeview** | Click on add and upload respectively|
| To edit project  | **Through Admin dashboard** | Redirected to the  project form details and editing happens|
| To delete an project  | **Through Admin dashboard** | click on project object and confirm by delete button|
| To search projects by title | **Enter text in search bar** | Users can search by Project Title|
| Vote on projects | **Vote** | Users can review projects they like and comment|


#### Setup Installation

- Copy the github repository url
- Clone to your computer
- Open terminal and navigate to the directory of the project you just cloned to your computer
- Run the following command to start the server using virtual environment

```
python3 -m venv --without-pip virtual
```

- To activate the virtual environment

```
source virtual/bin/activate
```

```
curl https://bootstrap.pypa.io/get-pip.py | python
```

```
pip install -r requirements.txt
```

- To copy .env.example to .env

```
cp .env.example .env
```

- Edit the .env file and replace the values with your own Cloudinary credentials and database credentials

- To run the server

```
python manage.py runserver

```

- Open the browser and navigate to http://127.0.0.1:8000/ to see the application in action


#### Authors Info
Email Address- gflorencewambui@gmail.com.

Copyright (c) [2022] Florence Wambui.