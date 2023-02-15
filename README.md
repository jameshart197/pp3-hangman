# Hangman Project for Python

**Developer: James Hart**

![Mockup image](docs/responsive-view.png)

[Deployed Project](https://pp3-hangman-jm.herokuapp.com/)
[Github Repository](https://github.com/jameshart197/pp3-hangman)

## Table of Content

  - [Project Goals](#project-goals)
    - [User Goals](#user-goals)
    - [Application Owner Goals](#application-owner-goals)
  - [User Experience](#user-experience)
    - [Target Audience](#target-audience)
    - [User Stories](#user-stories)
  - [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Frameworks, Libraries & Tools](#frameworks-libraries--tools)
  - [Features](#features)
    - [Future Features](#future-features)
  - [Validation](#validation)
  - [Testing](#testing)
    - [Testing user stories](#testing-user-stories)
  - [Bugs](#bugs)
  - [Deployment](#deployment)
  - [Credits](#credits)
  - [Acknowledgements](#acknowledgements)

## Project Goals

### User Goals

- Be able to understand the application intuitively
- Be able to see already guessed letters
- Receive feedback if I make an error
- Keep track of remaining lives
- Find out the word if I fail to guess it

### Application Owner Goals

- Simplistic fun
- Validates user entries to avoid errors
- Returns feedback on why an error occurs
- Offers the user to play again

## User Experience

### Target Audience

- People interested in simple word guessing games
- People interested in the Python coding behind the project

### User Stories

1. As a user, I want to run the game, so that I can play
2. As a user, I want to easily understand how to play the game
3. As a user, I want to understand which type of input is required, and understand my mistakes if I make an error during input
4. As a user, I want to clearly see the number of incorrect guesses or lives I have remaining
5. As a user, I want to see all currently guessed letters
6. As a user I want to see my progress on the guessed word
7. As a user I want to be able to see what the word was, even if I didn’t guess it
8. As a user I want to be able to play again without having to restart the program

## Technologies Used

### Languages

- Python

### Frameworks, Libraries & Tools

- [Am I Responsive](http://ami.responsivedesign.is/) was used to create the multi-device mock-up you can see at the start of this README.md file.
- [Git](https://git-scm.com/) was used for version control, pushing the code to Github.
- [GitHub](https://github.com/) was used for remote storage of the repository for the project code.
- [GitPod](https://gitpod.io/) was used as a coding platform.
- [Greenshot](https://getgreenshot.org/) was used to create the screenshots in this README.md
- [Heroku](https://heroku.com) was used to deploy the project.
- The project also makes use of an HTML, CSS and JS simulated terminal to enable users remote access over the internet.

| **User Story**   | **Feature or Code**                    | **Functionality**          |
| ------------- | ----------------------------- | ---------------------------- | 
| As a user, I want to run the game, so that I can play | The game starts automatically on run | Functioning | 
| As a user, I want to easily understand how to play the game | The game begins by guiding you to guess a single letter | Functioning | 
| As a user, I want to understand which type of input is required, and understand my mistakes if I make an error during input
 | This is covered by feature 4 | Functioning | 
| As a user, I want to clearly see the number of incorrect guesses or lives I have remaining | This is covered by feature 3 | Functioning | 
|As a user, I want to see all currently guessed letters | This is covered by feature 2 | Functioning | 
| As a user I want to see my progress on the guessed word | This is covered by feature 1 | Functioning | 
| As a user I want to be able to see what the word was, even if I didn’t guess it | This is covered by feature 7 | Functioning | 
| As a user I want to be able to play again without having to restart the program | This is covered by feature 5 | Functioning | 