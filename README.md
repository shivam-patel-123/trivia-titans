# Trivia Titans Game
![Trivia-Titans-Architecture](https://github.com/user-attachments/assets/62ad7d6d-e9f5-473b-b299-cb70207534b8)


# How to use

1. Create .env file in the root of `frontend` directory and replace the following with your firebase credentials:

```
API_KEY = your-api-key
AUTH_DOMAIN = your-auth-domain
PROJECT_ID = your-project-id
STORAGE_BUCKET = your-storage-bucket
MESSAGING_SENDER_ID = your-messaging-sender-id
APP_ID = your-app-id
MEASUREMENT_ID = your-measurement-id
```
2. Install project dependencies:

```
cd frontend
npm i
```

3. Run the project:

```
cd frontend
npm start
```


# Features

## 1. User Authentication
For any web application, user authentication is the first and most crucial part. I decided to implement this feature. I have implemented the Authentication feature for Trivia Titans online gaming application. Users wishing to play games on the website need to register themselves first. For registration they have three options, email, Google, Facebook. Once the user is registered, they can login and start having fun. Users registering using social media will be automatically logged in after registration. If a user forgot the password they can reset from the link on the login page. After signing in, users can play games or update the profile.

## 2. User Profile Management 
The User Profile Management feature allows users to edit their personal information, including their profile picture, and name. It provides users with the flexibility to keep their profiles up-to-date. Additionally, users can access and review their gaming statistics, such as the number of games played. Additionally, user can manage their team affiliations and leave the team and check statistics compared to the other users.

## 3. Team Management 
It allows users to create a team and invite otherplayers to the team. The user who initiates the team becomes the admin. The players can accept or reject the team invitations. The admin can remove the team members, the users can leave the team. In case the admin chooses to leave, the next member in the list becomes the new admin and assumes the same privileges, including adding or removing team members. The admin/user can see the participants in the team and team statistics.

## 4. Trivia Game Lobby
It allows users to browse and join available trivia games created by administrators. Users can filter games based on category, difficulty level, or time frame and view game details, including the number of participants, time remaining, and a short description.

## 5. In-Game Experience 
The "In-Game Experience" feature provides users with an interactive trivia gaming experience. Users can answer multiple-choice trivia questions within a specified time frame, view real-time team scores, communicate with team members through a chat feature, view the correct answers and explanations after each question, and track individual and team performance.

## 6. Leaderboards 
The Leaderboard Module is a comprehensive platform within the application that empowers users to track their performance and rankings in various contexts. It offers global and category-specific leaderboards, time frame filtering, top-performing entity showcases, and detailed performance statistics. This module fosters healthy competition and provides valuable insights for users or teams to gauge their progress, strategize better, and achieve higher rankings, contributing to an engaging and fulfilling user experience.

## 7. Trivia Content Management 
This module provides administrators with the capability to manage trivia questions, oversee games, and analyze relevant game data. The functionalities offer a level of control and versatility for the administrators, enabling them to manage trivia questions. Administrators have a wide array of options to effectively manage the trivia questions content in this module. This includes the ability to add, modify, or delete trivia questions. Each question, defined by its unique difficulty level and category, can be flexibly altered or deleted as per requirements, providing an agile system for question management.

## 8. Notifications and Alerts 

The Notifications and Alerts Module is a key component of gaming experience. This system's primary goal is to keep users engaged, informed, and up-to-date with in-game events, achievements, and social interactions. It also ensures users remain connected with the gaming platform, game updates and their teammates.

## 9. Automated Question Tagging 
This module organizes trivia questions into different categories. It sorts and labels all untagged questions by assigning suitable tags. This way, users or teams can easily choose questions from their preferred categories.

## 10. Virtual Assistance 
The Virtual Assistance module seamlessly integrates Amazon Lex for natural language processing, AWS Lambda for powerful backend logic, and Firestore for retrieving score data. This chatbot aims to engage users in interactive conversations, providing assistance with quiz-related queries, guiding them through the website, and offering real-time score updates for teams and players.

# Sprint Plan

- ### _Sprint 1 (26 May - 5 June):_
  Explored various AWS and GCP services such as Firestore, Cloud functions, SNS, Web socket, and also discussed the tables.

- ### _Sprint 2 (6 June - 13 June):_
  Development of User Authentication, T eam Management, In-Game Experience, Trivia Content Management, Automated Question Tagging

- ### _Sprint 3 (14 June - 20 June):_
  Testing of different functionalities of the first set of modules

- ### _Sprint 4 (21 June - 27 June):_
  Development of User Profile Management, Trivia Game Lobby, Leaderboards, Notifications and Alerts, Virtual Assistance

- ### _Sprint 5 (28 June - 4 July):_
  Testing 2nd set of modules and Integration of modules

- ### _Sprint 6 (5 July - 11 July):_
  User Acceptance Testing and fixing integration bugs; Performance Testing and optimizing the application

- ### _Sprint 7 (12 July - 18 July):_
  Deployment preparation; creation of documentation and setting up deployment environment

- ### _Sprint 8 (19 July - 25 July):_
  Fixing bugs in the previous deployment and address whatever issues that may have occurred

- ### _Sprint 9 (26 July - 1 August):_
  Final Deployment and testing it thoroughly; Closing of project


# Flowchart / Roadmap

![Flowchart drawio](https://github.com/user-attachments/assets/c46055d6-c4e3-4054-af4b-93cb1a9705bf)


#

