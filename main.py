# US's 50 States Game

################################
### Created by 4bd3ss4md #######
################################

from turtle import Turtle, Screen
import csv
from state import State
import pandas as pd
from scoreboard import Scoreboard
from prompt_text import PromptText

FONT = ('Courier', 20, 'normal')
NUM_OF_US_STATES = 50


# Get the dictionary that contains the answered's states coordinates
def get_state_dict(answer_state, states_dict):
    for dictio in states_dict:
        if dictio['state'] == answer_state:
            return dictio


def main():
    screen = Screen()
    screen.setup(width=800, height=750)
    screen.title("US's 50 States Game")
    # Turn off the tracer so that nothing happening in the screen gets shown
    screen.tracer(0)

    # Print US 50 States images on screen
    image_dir = 'blank_states_img.gif'
    screen.addshape(image_dir)
    myImage = Turtle(image_dir)
    myImage.speed(0)  # so it will draw the image instantly
    myImage.shape(image_dir)  # give your object the image
    myImage.penup()  # if you dont do this, it will draw a line
    myImage.goto(0, 0)  # give your image a location

    while True:
        screen.update()  # update your window

        # Read 50_states CSV file using CSV module
        with open("50_states.csv", "r") as csv_file:
            csv_file = csv.DictReader(csv_file, delimiter=',')
            states_dict = []
            for line in csv_file:
                new_dict = dict(line)
                states_dict.append(new_dict)
            states_list = []
            for dictio in states_dict:
                states_list.append(dictio['state'])

            # Create the Scoreboard
            scoreboard = Scoreboard()
            scoreboard.update_scoreboard()

            # Create turtle that will be prompted to the screen if the user guesses a wrong state.
            prompt_text = PromptText()

            # Create an empty list that will contain the correct states answered by the user
            answered_states = []

            # Start the game
            is_on = True
            while is_on:
                # Update the screen
                screen.update()
                # Print the Congrats prompt
                if len(answered_states) == NUM_OF_US_STATES:
                    prompt_text.congrats_prompt()
                    is_on = False
                # Get an answer from the user
                answer_state = screen.textinput(title=" Guess the State",
                                                prompt="What's another state's name? ").title()
                if answer_state == "Exit":
                    is_on = False
                # Clear the text prompt
                prompt_text.clear_text_prompt()
                # Check if the input exists in the states
                if answer_state in states_list:
                    # Check if the state is already answered
                    if answer_state in answered_states:
                        # Prompt the user that the state is already answered
                        prompt_text.repeated_prompt()
                    else:
                        # Get the dictionary that contains the state's details
                        state_dict = get_state_dict(answer_state, states_dict)

                        # Append the correct answer to the list of the answered states
                        answered_states.append(answer_state)

                        # Get the name of the state and the x & y coordinates
                        state_name = state_dict['state']
                        x_cor = int(state_dict['x'])
                        y_cor = int(state_dict['y'])

                        # Create an object from State class
                        State(state_name, x_cor, y_cor)

                        # Update the scoreboard
                        scoreboard.increase_score()
                else:
                    if answer_state == 'Exit':
                        break
                    else:
                        # Prompt a wrong answer text
                        prompt_text.wrong_prompt()

            if len(answered_states) < 50:
                # Create a list that contains the states the user did not answer.
                missed_states = []
                for state in states_list:
                    if state in answered_states:
                        continue
                    else:
                        missed_states.append(state)

                # Create a CSV file that contains a list of states missed by the user

                data = pd.DataFrame(missed_states, columns=["Here is a list of all the states that you missed:"])
                data.to_csv('missed_states.csv', index=False)

                #     csv_writer = csv.writer(new_file)
                #     csv_writer.writerows(missed_states)
                print("CSV file successfully created.")

        # Exit screen on click
        screen.exitonclick()


main()
