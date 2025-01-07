# Tasker Hub

Tasker Hub is platform designed for creativity, collaboration, and productivity.

Tasker Hub simplifies the process of exploring, creating, and sharing tasks within a vibrant community. With a clear purpose, mobile-friendly design, and intuitive navigation, it provides a seamless and user-friendly experience.

It facilitates connections by enabling the discovery of tasks, showing support through likes, and building on ideas by creating templates. Task management is streamlined with features to add, edit, or remove tasks, ensuring flexibility and control. A quick and secure sign-up process ensures smooth onboarding.

Tasker Hub transforms ideas into action, fostering collaboration and innovation.


## Table of Contents

- [Tasker Hub](#tasker-hub)
  * [User Experience (UX)](#user-experience-ux)
    + [User Stories](#user-stories)
    + [Design](#design)
      - [Colour Scheme](#colour-scheme)
      - [Imagery](#imagery)
      - [Fonts](#fonts)
      - [Wireframes](#wireframes)
  * [Data Model](#data-model)
  * [Testing](#testing)
  * [Features](#features)
  * [Deployment](#deployment)
  * [Technologies Used](#technologies-used)
  * [Frameworks - Libraries - Programs Used](#frameworks---libraries---programs-used)
  * [Credits](#credits)
  * [Acknowledgments](#acknowledgments)

## User Experience (UX)

Site user is an individual who values productivity, creativity, and collaboration, such as but not limited to task planners, project managers, and idea enthusiasts. 


### User Stories

#### Planned User Stories
- User Navigation
    - As a Site User I can:
        - see what the site is about so I can gain understanding of where I landed.
        - view the site on any screen size so that I can browse the site on all devices.
        - intuitively navigate around the site so that I can easily browse content.
        - locate social media links so that I can integrate into site's community.

- Task Lists Managment
    - As a Site User I can:
        - view paginated list of tasks so that I can select the preferred task. 
        - sort list of tasks so I can have easier time finding the preferred task.
        - click on a task so I can view the task.
        - add a new task so that I can create my own tasks as well.
        - highlight a task so that I can easily navigate to my current to do task.

- View Task Managment
    - As a Site User I can:
        - like other users tasks so that I can support their Tasker journey.
        - create templates from other user tasks so that I can expand on their idea.
        - edit my own task so that I can complete, correct or expand a main idea.
        - delete a task so that I can no longer see that task live on site.
        - save a task so that I can add a task to my tasks.

- Account Management
    - As a Site User I can:
        - sign up to the site so I can create my account.
        - sign in to the site so I can start using its features.
        - log out of my account so that I can keep my account secure.

- Site Administration
    - As a Superuser I can create, read, update and delete both tasks and users so that I can manage the site.


### Design


#### Colour Scheme

#### Imagery

#### Fonts

#### Wireframes
<details>

 <summary>Landing Page</summary>

![Landing Page](docs/wireframes/landing_page.png)
</details>
<details>

 <summary>Browse Tasks</summary>

![Browse Tasks](docs/wireframes//browse_tasks.png)
</details>
<details>

 <summary>View Task</summary>

![View Task](docs/wireframes/view_task.png)
</details>
<details>

 <summary>Your Tasks</summary>

![Your Tasks](docs/wireframes/your_tasks.png)
</details>
<details>

 <summary>Add a New Task</summary>

![Add a New Task](docs/wireframes/add_new_task.png)
</details>
<details>

 <summary>Register</summary>

![Register](docs/wireframes/register.png)
</details>
<details>

 <summary>Log In</summary>

![Log In](docs/wireframes/log_in.png)
</details>

## Data Model

Entity Relationship Diagram (ERD) is created using [Database Diagram Tool](https://databasediagram.com/) to represent data models visually.

<details>

 <summary>Code used to create a model</summary>

```
User
-
user_id Int PK
username Char(20)
email Char(50)
password Char(50)


Task
-
task_id Int PK
author Int FK > User.user_id
name Char(200)
is_completed Boolean
image Cloudinary
date_updated DateTime
likes Int

Subtask
-
subtask_id Int PK
task Int FK > Task.task_id
title Char(200)
note Text
is_completed Boolean
```
</details><br>

![Entity Relationship Diagram ](docs/img/erd.png)

The database design for this project consists of the following models:

- **User** <br>
Represents the individual user. Sensitive information needed to succesfully access the account is stored here.
- **Task** <br>
Represents the individual task. Single Task is constructed from one or multiple subtasks and contains Foreign Key "author" effectively connecting User to Task. 
- **Subtask** <br>
Represents the individual subtask and contains all information needed to log a single subtask into a Task through "task" Foreign Key.


## Testing


## Features


## Deployment


## Technologies Used


## Credits


## Acknowledgments

