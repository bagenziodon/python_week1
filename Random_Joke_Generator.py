import random

def get_random_joke():
    # List of jokes (including programming and Python-related ones)
    jokes = [
        "Why do programmers prefer dark mode?\nBecause light attracts bugs! 🦠",
        "Why did the Python developer break up with their partner?\nThey couldn’t find any common variables. 💔",
        "Why do Java developers wear glasses?\nBecause they don’t see sharp. 👓",
        "Why don’t programmers like nature?\nIt has too many bugs. 🐛",
        "How many programmers does it take to change a light bulb?\nNone, that’s a hardware issue! 💡",
        "Why was the JavaScript developer sad?\nBecause they didn’t know how to 'null' their feelings. 😢",
        "What’s a programmer’s favorite hangout place?\nThe Foo Bar. 🍻",
        "Why did the developer go broke?\nBecause they used up all their cache. 💸",
        "What did the Python say to the JavaScript?\n'You have a lot of promises, but no closure.' 😂",
        "Why was the computer cold?\nBecause it left its Windows open. 🖥️"
    ]
    
    # Select a random joke from the list
    joke = random.choice(jokes)
    
    # Display the joke
    print(joke)

def main():
    print("Welcome to the Random Joke Generator! 🤣")
    get_random_joke()

if __name__ == "__main__":
    main()
