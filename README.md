[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/JTXl4WMa)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=21325173&assignment_repo_type=AssignmentRepo)
# COMP 163 - Project 1: Character Creator & Chronicles

# Game Concept
My RPG is a quest where you have to find treasure and along the way you defeat enemies and make friends with NPC's to enrichen your experience. 
 
# Design Choices
I chose my stat formulas because the highest level you can get is level 100. From there I broke down what type of status you would have have you level up such as once you get to level 20 your a noivce instead of your starting status of a noob. Then I just created stats based off on what your usually starting stats would be and how easy it would be to level up one stat over the other based on your character class. 
 
# AI Usage
I used AI to help me understand where my code went wrong and why it wasn't passing the test cases. 
 
# How to Run
You can run my code by calling the functions and entering the parameters. For example you call create_character(character, character_class) function then you enter your charcter name and character class. Now that you've done that there is now a dictionary that holds all your characters information. Then if you want to save your character you call save_character(character, filename) fucntion. You enter your charcater's name and your file which attached to your charcater's name is a dictionary. So it saves all your character's stats into a file in a very specific format. Then after that if you want to load your character you call the load_character(filename) function which will load your charcter and returna dictionary of all your character's stats. If you want to level up your charcter you call the level_up(character) function and input your charcater which will level_up your character's level by 1 and level up your character's stats. Finally if you want to display your character's stats you call the display_character(character) function and enter your character. Then it will display your character's name, level, and their stats. 
 
# 🎯 Project Overview

Build a text-based RPG character creation and story progression system that demonstrates mastery of functions and file I/O operations.

# Required Functions 
Complete these functions in project1_starter.py:

create_character(name, character_class) - Create new character

calculate_stats(character_class, level) - Calculate character stats

save_character(character, filename) - Save character to file

load_character(filename) - Load character from file

display_character(character) - Display character info

level_up(character) - Increase character level

# 🎭 Character Classes
Implement these character classes with unique stat distributions:


Warrior: High strength, low magic, high health

Mage: Low strength, high magic, medium health

Rogue: Medium strength, medium magic, low health

Cleric: Medium strength, high magic, high health

# 📁 Required File Format
Your save_character() function must create files in this exact format:

Character Name: [name]

Class: [class]

Level: [level]

Strength: [strength]

Magic: [magic]

Health: [health]

Gold: [gold]


# Run specific test file
python -m pytest tests/test_character_creation.py -v

# Test your main program
python project1_starter.py

GitHub Testing:

After pushing your code, check the Actions tab to see automated test results:

✅ Green checkmarks = tests passed
❌ Red X's = tests failed (click to see details)

# ⚠️ Important Notes
Protected Files

DO NOT MODIFY files in the tests/ directory

DO NOT MODIFY files in the .github/ directory

Modifying protected files will result in automatic academic integrity violation

# AI Usage Policy

✅ Allowed: AI assistance for implementation, debugging, learning

📝 Required: Document AI usage in code comments

🎯 Must be able to explain: Every line of code during interview

# 📝 Submission Checklist

 All required functions implemented
 
 Code passes all automated tests
 
 README updated with your documentation
 
 Interview scheduled and completed
 
 AI usage documented in code comments

# 🏆 Grading

Implementation (70%): Function correctness, file operations, error handling

Interview (30%): Code explanation and live coding challenge
