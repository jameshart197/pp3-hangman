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

## Features

### Current Features 

1. Prints words in blanked format
    a. Updates when a letter is guessed correctly
2. Prints incorrect guesses		
    a. When an incorrect guess is made, inform user
3. Prints remaining ‘lives’ (incorrect guesses)
4. Validates user guesses and informs them if they have entered an incorrect input
5. Offers user to play again after each round
6. Informs the user if they have won (Victory!) or lost (Game Over!)
7. Informs the user of the correct word, whether they guessed it or not
8. Pulls from a random list of 850 words
    a. Sorts this list, so that there are no repeats when pressing “Play Again”


### Current Features 

- Implement a “difficulty setting”
- Implement graphic for Hangman ASCII
- Potentially have the difficulty scale depending on the length of word
- Implement color to the text

## Validation

### PEP-8 Validation

<details><summary>Pep-8 Validation</summary>
<img src="docs/pep9-validation.png">
</details>

## Testing

### Testing user stories

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

## Bugs

| Bug                                                                                                               | Fix                                                                                                                                       |
| ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| Code ran endlessly even if user ran out of guesses | Implemented a Maximum Incorrect Guesses variable to work from that is a global |
| There was no “user victory” | Eventually worked out a code counting letters not guessed down to 0 |
| Play again function would not work | Put function inside main function |                                                               |
| Words containing capitals did not work properly | Used the .lower() functionality |
| Users whitespace was counted in guessing | Used the .strip() functionality in python |
| Could not shuffle words.txt properly | Imported random library in python |

## Deployment

### Deployment through Heroku
The website was deployed using Heroku by following these steps:
1. Create a new app from heroku dashboard
2. Enter PORT and 8000 in Config Vars
3. Add python and nodeJS buildpacks
4. Link GitHub repository
5. Deploy Automatically so that any changes pushed to the main branch go live.

### Forking the GitHub Repository
1. Go to the GitHub repository
2. Click on Fork button in top right corner

### Making a Local Clone
1. Go to the GitHub repository 
2. Locate the Code button above the list of files and click it
3. Highlight the "HTTPS" button to clone with HTTPS and copy the link
4. Open Git Bash
5. Change the current working directory to the one where you want the cloned directory
6. Type git clone and paste the URL from the clipboard ($ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY)
7. Press Enter to create your local clone

## Credits

### Code

-  Words.txt was supplied by GitHub user Xehtron, found through a google search
-  Mentor Brian helped with coding the Play Again function
-  Assistance from a friend outside the course helped with the logic of the letter_not_guessed function

## Acknowledgements

This application was assisted in its production by;

- My mentor for professional guidance and feedback
- Code Institute Slack members who helped with small bugs and testing along the way
- Friends who tested the website and user stories for me on various devices
