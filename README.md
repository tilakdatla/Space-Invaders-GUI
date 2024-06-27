# Space-Invaders-GUI

This is a simple Space Invaders game implemented in Python using the Turtle graphics library. The player controls a paddle at the bottom of the screen and can fire bullets to destroy alien ships that descend from the top of the screen. The game ends when all alien ships are destroyed, an alien ship collides with the paddle, or an alien ship crosses a certain limit.

##  Getting Started
### Prerequisites
To run this game, you need to have Python installed on your machine. You can download Python from python.org.

### Installation
Clone the repository to your local machine using:


### Copy code
git clone https://github.com/tilakdatla/Space-Invaders-GUI/
Navigate to the project directory:
cd space-invaders

### Running the Game
To start the game, run the day95.py file using Python. You can use an IDE like PyCharm or VS Code, or you can run it from the command line.


### How to Play
- Use the Left arrow key to move the paddle to the left.
- Use the Right arrow key to move the paddle to the right.
- Use the Up arrow key to fire bullets.
- The objective is to destroy all the alien ships before they collide with your paddle or cross the limit.

### Libraries Used
- Turtle: The Turtle graphics library is used to create the game's graphics. It is a standard Python library used for creating basic graphics and shapes. For more information, visit the Turtle documentation.

### Project Structure
- day95.py: This is the main file that initializes the game, handles user inputs, and runs the game loop.
- day95extra.py: This file contains the classes used in the game:
- Paddle: Represents the player's paddle.
- Aliens: Manages the alien ships.
- Score: Keeps track of the score and displays game messages.
- Bullet: Represents the bullets fired by the paddle.

### Game Logic

- The paddle moves left and right based on user input.
- Bullets are fired from the paddle's current position when the Up arrow key is pressed.
- Alien ships move downward continuously.
- The game checks for collisions between bullets and alien ships, and between the paddle and alien ships.
- The score increases when an alien ship is destroyed.
- The game ends when all alien ships are destroyed, an alien ship collides with the paddle, or an alien ship crosses the limit.

### Screenshots
Include some screenshots of the game here to give users a visual idea of the gameplay.

### Contributing
If you would like to contribute to the project, please fork the repository and create a pull request with your changes.

### License
This project is licensed under the MIT License. See the LICENSE file for more information.
