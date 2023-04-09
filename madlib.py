from textwrap import dedent
import re, json

greeting = dedent(
    """
    **************************************
    **    Welcome to MadLib!            **
          To play this game, you will   
          receive a series of prompts
          asking you to provide
          different types of words
          (nouns, adjectives, etc.) in
          order to build a story! Once 
          each question has been 
          answered, we will display the
          story YOU helped create!
           
    ** To quit at any time, type "quit" **
    **************************************
    """
)

game_prompt = dedent(
    """
    ***********************************
    ** Would you like to play?       **
       Type 'yes' to get started!
    ***********************************
    """
)

game_end = dedent(
    """
    ***********************************
    **         STORY TIME!!!!        **
    ***********************************
    """
)

farewell = dedent(
    """
    ***********************************
    ** We hope you enjoyed playing!  **
       See you next time!
    ***********************************
    """
)


def read_template(file):
    with open(file) as f:
        return f.read().strip()


def parse_template(string):
    return re.findall(r'{([^}]+)}', string)


def merge(template, word_list, output_file):
    merged_text = re.sub(r'{([^}]+)}', lambda match: word_list.pop(0), template)
    with open(output_file, 'w') as f:
        f.write(merged_text)
    return merged_text


if __name__ == "__main__":
    word_input_list = []

    print(greeting)
    print(game_prompt)

    path = "assets/example.txt"
    path2 = "assets/completed_game_file.txt"
    template = read_template(path)
    parsed_template = parse_template(template)
    # print(parsed_template)

    user_input = input("> ")

    while user_input != 'quit':
        if user_input == 'yes':
            for word in parsed_template:
                word_input = input(f'Please provide a {word} > ')
                word_input_list.append(word_input)

            if len(word_input_list) == len(parsed_template):
                merged_text = merge(template, word_input_list, path2)
                print(game_end)
                print("Great job! Here is the story you created:")
                print(merged_text)
                print(farewell)
                break

        user_input = input("> ")
