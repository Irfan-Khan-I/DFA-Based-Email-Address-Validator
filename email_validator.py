import re

def validate_email(email):
    # DFA states
    states = [
        {"[a-zA-Z0-9._%+-]": 1},
        {"[a-zA-Z0-9._%+-]": 1, "@": 2},
        {"[a-zA-Z0-9.-]": 3},
        {"[a-zA-Z]": 4},
        {"[a-zA-Z0-9.-]": 4}
    ]
    
    current_state = 0
    
    for char in email:
        found_transition = False
        for transition, next_state in states[current_state].items():
            if re.match(transition, char):
                current_state = next_state
                found_transition = True
                break
        
        if not found_transition:
            return False
    
    return current_state in {3, 4}

# Prompt the user to input an email address
user_email = input("Enter an email address to validate: ")

# Validate the user-provided email address
if validate_email(user_email):
    print("Valid email address!")
else:
    print("Invalid email address!")
