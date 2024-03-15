import random
from tkinter import *
from tkinter import messagebox

class HangmanGame:
    def __init__(self):
        self.score = 0
        self.run = True

        # Read hints from the hints file
        with open('hints.txt', 'r') as hints_file:
            self.hints = hints_file.readlines()

        # Main loop
        while self.run:
            self.root = Tk()
            self.root.title('Hangman')
            self.root.config(bg='#E7FFFF')
            self.root.bind("<Configure>", self.on_resize)  # Bind resize event

            self.count = 0
            self.win_count = 0

            # Choose word and hint
            self.index = random.randint(0, 49)
            with open('word.txt', 'r') as word_file:
                self.selected_word = word_file.readlines()[self.index].strip('\n')
            self.hint = self.hints[self.index].strip('{}\n')

            # Display hint
            self.hint_label = Label(self.root, text=self.hint, bg="#E7FFFF", font=("arial", 14))
            self.hint_label.grid(row=0, column=0, columnspan=2, pady=10)  # Use grid layout

            # Calculate word dashes variables
            self.dashes_width = len(self.selected_word) * 60
            self.x_start = (self.root.winfo_width() - self.dashes_width) // 2  # Center horizontally

            # Create word dashes labels
            self.dash_labels = []
            for i in range(len(self.selected_word)):
                x = self.x_start + i * 60
                dash_label = Label(self.root, text="_", bg="#E7FFFF", font=("arial", 40))
                dash_label.grid(row=1, column=i, padx=5)  # Use grid layout with padding
                self.dash_labels.append(dash_label)

            # Load letter and hangman images
            self.letter_images = {letter: PhotoImage(file=f"{letter}.png") for letter in 'abcdefghijklmnopqrstuvwxyz'}
            self.hangman_images = {f"h{i}": PhotoImage(file=f"h{i}.png") for i in range(1, 8)}

            # Create letter buttons
            self.letter_buttons = []
            button_row = 2
            button_col = 0
            for letter in 'abcdefghijklmnopqrstuvwxyz':
                button = Button(self.root, text=letter, command=lambda letter=letter: self.check_letter(letter),
                                font=10, image=self.letter_images[letter])
                button.grid(row=button_row, column=button_col, padx=5, pady=5)  # Use grid layout with padding
                self.letter_buttons.append(button)
                button_col += 1
                if button_col == 13:
                    button_col = 0
                    button_row += 1

            # Hangman image placeholder
            self.hangman_image_label = Label(self.root)
            self.hangman_image_label.grid(row=4, column=0, columnspan=2)  # Use grid layout

            # Exit button
            self.exit_button = Button(self.root, text="Exit", command=self.close, font=10)
            self.exit_button.grid(row=0, column=2, padx=5, pady=5)  # Use grid layout

            # Score label
            self.score_label = Label(self.root, text=f"Score: {self.score}", font=("arial", 25))
            self.score_label.grid(row=0, column=1, padx=5, pady=5)  # Use grid layout

            self.root.mainloop()

    def on_resize(self, event):
        # Adjust widget sizes and positions based on new window size
        self.hint_label.config(width=int(0.5 * event.width))  # Scale hint label to half window width
        self.x_start = (event.width - self.dashes_width) // 2  # Recalculate x_start for word dashes
        for i, dash_label in enumerate(self.dash_labels):
            x = self.x_start + i * 60
            dash_label.grid_configure(column=i, padx=(x, 5))  # Update grid position of dash labels

    def check_letter(self, letter):
        # Your check logic here
        pass

    def close(self):
        self.run = False
        self.root.destroy()

HangmanGame()
