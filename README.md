# LAB - Class 03
## Project: File IO and Exceptions
## Author: Mandela Steele-Dadzie

### Setup:

VENV Creation: python3 -m venv .venv
VENV Activation: source .venv/bin/activate

Initialize App: python3 -m madlib

### Tests:

Testing was difficult here as my code was not written with these tests in mind, a mistake on my part.
Because I used regex to simply pull out and then replace the words within curly braces, I am not returning a "stripped string" where the template is returned after the words in curly braces have been pulled out. 
I am not pulling these words out from the template, but rather logging them in a new list through regex.
I may attempt to rework this code so that it passes these tests at a later date.

### Notes/Credits:
I used ChatGPT to develop a regex solution to parse the template for all words located in curly braces, and to also replace all words in curly braces for the output template.