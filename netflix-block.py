# import modules
import random
import webbrowser
import os
import socket

# Determine the IP address of www.netflix.com
website = "www.netflix.com"
ip_address = socket.gethostbyname(website)

# Add a firewall rule to block access to the website's IP address
os.system(f"netsh advfirewall firewall add rule name=Block_{website} dir=out remoteip={ip_address} action=block")

# Define function that generates a 6-letter word and with operators between each letter.
def get_random_configurators():

    # Generate a random 6-letter word from the English alphabet
    letters = "abcdefghijklmnopqrstuvwxyz"
    word = "".join(random.choices(letters, k=6))

    # Split the word into a list of letters
    letters = list(word)

    # Generate 5 random arithmetic configurators
    configurators = []
    for i in range(5):
        # Select a random letter
        letter1 = random.choice(letters)

        # Generate a random arithmetic operator
        operators = ["+", "-", "*", "/"]
        operator = random.choice(operators)

        # Combine the letter and operator into a string representing the configurator
        configurator = f"{letter1.upper()} {operator}"
        configurators.append(configurator)

    # Select a random letter
    letter2 = random.choice(letters)

    # Append the letter to the configurators
    configurators.append(letter2.upper())

    # Join the configurators into a single string
    configurators_str = " ".join(configurators)

    # Generate a list of algebraic problems for each letter in the configurators string
    problems = []
    for letter in configurators_str:
        if letter.isalpha():
            # Generate random numbers between 1 and 1000 for the problem
            num1 = random.randint(1, 1000)
            num2 = random.randint(1, 1000)
            num3 = random.randint(1, 1000)

            # Generate the algebraic problem and solution
            problem = f"{num1}*{letter} - {num2} = {num3}"
            solution = round((num3 + num2) / num1, 1)
            print(solution)

            # Append the problem and solution to the list
            problems.append((problem, solution))

    return configurators_str, problems


configurators_str, problems = get_random_configurators()
print(configurators_str)  # Outputs the configurators as a single string, such as "A + B / C - D - E * F"

# Prompt the user to solve the problems one by one
for i, (problem, solution) in enumerate(problems):
    while True:
        # Print the problem and ask the user to solve it
        print(f"\nProblem {i+1}: Solve equation. Round to the nearest tenth.:")
        user_input = input(f"{problem} = ")

        # Check if the user's answer is correct, rounds to nearest tenth
        if float(user_input) == solution:
            # If the answer is correct, go to the next problem
            break
        else:
            # If the answer is incorrect, start again from the first problem // DOES NOT START OVER. TO BE FIXED
            print("Incorrect answer. Please try again.")
            i = 0

print("\nAll problems solved successfully!")

# Prompt user to give final answer. If they are correct, they can open Netflix.
final_answer = input(f"Enter password. {configurators_str} = ")
# Unblocks firewall setting on netflix.com. Must have administrator access and running on Windows OS.
if final_answer == solution:
    os.system(f"netsh advfirewall firewall add rule name=Unblock_{website} dir=out remoteip={ip_address} action=allow")
else:
    print("Incorrect password. Please try again.")

    

def solve_configurator(configurator_str, answers):
# Split the configurator string into a list of terms
    terms = configurator_str.split()


# Initialize the result to the first term
    result = answers[terms[0]]

# Iterate through the remaining terms, applying the operator and the answer to the result
    for i in range(1, len(terms), 2):
        operator = terms[i]
        letter = terms[i+1]
        answer = answers[letter]

        if operator == "+":
            result += answer
        elif operator == "-":
            result -= answer
        elif operator == "*":
            result *= answer
        elif operator == "/":
            result /= answer

# Return the result
        return result






