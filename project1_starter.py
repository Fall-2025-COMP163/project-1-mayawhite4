"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: [Your Name Here]
Date: [Date]

AI Usage: [Document any AI assistance used]
Example: AI helped with file I/O error handling logic in save_character function
"""
def create_character(name, character_class):
    """
    Creates a new character dictionary with calculated stats
    Returns: dictionary with keys: name, class, level, strength, magic, health, gold
    
    Example:
    char = create_character("Aria", "Mage")
    # Should return: {"name": "Aria", "class": "Mage", "level": 1, "strength": 5, "magic": 15, "health": 80, "gold": 100}
    """
    # TODO: Implement this function
    # Remember to use calculate_stats() function for stat calculation
    stats = (character_class, 1)
    character_info = {"name": name, "class": character_class, "level": level, "strength": stats[0], "magic":stats[1], "health": stats[2],"gold": 100}
    return character_info

def calculate_stats(character_class, level):
    """
    Calculates base stats based on class and level
    Returns: tuple of (strength, magic, health)
    
    Design your own formulas! Ideas:
    - Warriors: High strength, low magic, high health
    - Mages: Low strength, high magic, medium health  
    - Rogues: Medium strength, medium magic, low health
    - Clerics: Medium strength, high magic, high health
    """
    # TODO: Implement this function
    # Return a tuple: (strength, magic, health)
    strength = 0
    magic = 0
    health = 0
    # Calculation for Warrior Stats
    if character_class == "Warrior":
        strength = str((20 * level))
        magic = str((2 * level))
        health = str((5 * level))
    # Calculation for Mage Stats
    elif character_class == "Mage":
        strength = str((2 * level))
        magic = str((20 * level))
        health = str((10 * level))
    # Calculation for Rouge Stats
    elif character_class == "Rouge":
        strength = str((10 * level))
        magic = str((10 * level))
        health = str((5 * level))
    #Calculation for Cleric Stats
    elif character_class == "Cleric":
        strength = str((10 * level))
        magic = str((20 * level))
        health = str((20 * level))
    else:
        return "That is not an option"
    return (strength,magic,health)

def save_character(character, filename):
    """
    Saves character to text file in specific format
    Returns: True if successful, False if error occurred
    
    Required file format:
    Character Name: [name]
    Class: [class]
    Level: [level]
    Strength: [strength]
    Magic: [magic]
    Health: [health]
    Gold: [gold]
    """
    # TODO: Implement this function
    # Remember to handle file errors gracefully
    character = create_character(name, character_class)
    with open(filename, "w") as characterfile:
        characterfile.write(f"Character Name: {character}\n")
        characterfile.write(f"Class: {character[1]} \n")
        characterfile.write(f"Level: {character[2]} \n")
        characterfile.write(f"Strength: {character[3]} \n")
        characterfile.write(f"Magic: {character[4]} \n")
        characterfile.write(f"Health: {character[5]} \n")
        characterfile.write(f"Gold: {character[1]} \n")
    return os.path.isfile 

def load_character(filename):
    """
    Loads character from text file
    Returns: character dictionary if successful, None if file not found
    """
    # TODO: Implement this function
    # Remember to handle file not found errors
    if os.path.isfile(filename) == True:
        return create_character(name, character_class)
    else:
        return "None"
        
        

def display_character(character):
    """
    Prints formatted character sheet
    Returns: None (prints to console)
    
    Example output:
    === CHARACTER SHEET ===
    Name: Aria
    Class: Mage
    Level: 1
    Strength: 5
    Magic: 15
    Health: 80
    Gold: 100
    """
    # TODO: Implement this function
    print(f"=== CHARACTER SHEET ===\n")
    print(f"=== CHARACTER SHEET ===\n")
    print(f"Name: {character}")
    print(f"")
    print(f"")
    print(f"")
    print(f"")
    print(f"")
    print(f"")

def level_up(character):
    """
    Increases character level and recalculates stats
    Modifies the character dictionary directly
    Returns: None
    """
    # TODO: Implement this function
    # Remember to recalculate stats for the new level
    pass

# Main program area (optional - for testing your functions)
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    print("Test your functions here!")
    
    # Example usage:
    # char = create_character("TestHero", "Warrior")
    # display_character(char)
    # save_character(char, "my_character.txt")
    # loaded = load_character("my_character.txt")
