## Introduction:
A simple hangman game built using Python. Tkinter library is used for GUI.

## Features:
1. Random selection of words and their corresponding hints from a predefined word list.
2. Visual representation of hangman as incorrect guesses are made.
3. Letters, once selected, disappear from view.
4. Score tracking and display.
5. Option to exit game.
6. User friendly graphical interface.

## Requirements:
1. Python 3.x
2. Tkinter library (usually pre-installed with python)

## Installation: 
1. Clone the repository or download the source code.
2. Ensure you have Python installed on your system.
3. Run the hangman.py file using Python.

## Usage:
1. Launch the game by executing the hangman.py file.
2. Guess letters by clicking on the corresponding buttons.
3. Try to deduce the hidden word before the hangman is fully drawn.
4. If successful, you win the round and can choose to play again.
5. If unsuccessful, the hangman is completed, and you have the option to play again.
6. Close the game by clicking on 'Exit' button on top right corner.
   
## Gameplay:
1. At the start of each round, a word is randomly chosen from a predefined list, and a hint is displayed to assist the player.
2. The player clicks on letter buttons to guess the letters of the word.
3. Correct guesses reveal the corresponding letters in the dashed line.
4. Incorrect guesses result in parts of the hangman being drawn.
5. The game continues until the player successfully guesses the word or the hangman is completed.
6. After each round, the player's score is updated based on their performance.

## Additional Notes:
1. The word list and corresponding hints are stored in separate text files (word.txt and hints.txt).
2. Hangman images are loaded from image files (h1.png to h7.png).
3. Button images for letters are also loaded from image files (a.png to z.png).
4. The game window size is set to 905x700 pixels, but you can adjust this as needed.

## Future Improvements:
1. Implement difficulty levels with varying word lengths or limited attempts.
2. Add sound effects and background music for a more immersive experience.
3. Support game in different, or varying, screen sizes.
4. Enhance the graphical interface with animations and transitions.
   
## Contributing:
Contributions to this project are welcome! If you have ideas for improvements or new features, feel free to fork the repository and submit a pull request.

![Main Screen](https://github.com/Hashibul01/PythonProjects/assets/77710050/f433e021-1ade-46dc-b681-edde3279ca59)
![Correct](https://github.com/Hashibul01/PythonProjects/assets/77710050/96dbc624-2664-43ac-aabd-9c13e654eac4)
![Incorrect](https://github.com/Hashibul01/PythonProjects/assets/77710050/13dcdea8-9e31-4230-97f0-0c793f5ae1e7)
