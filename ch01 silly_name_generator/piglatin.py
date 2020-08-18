import sys
import random

def main():

    print("I'll convert your word to Pig Latin\n")

    vowels = ["a", "e", "i", "o", "u"]
    retry = True
    while retry:
        ans = input("Tell me your word, peasant: ")

        if len(ans) == 0:
            print("You fool, state your word or be gone at once")
        elif ans[0] in vowels:
            ans = ans + "way"
            print(f"{ans} is your worday")
        else:
            ans = ans + "ay"
            print(f"{ans} is your worday")

        retry_section = input("Will you bother me with another word? (y): ")
        if retry_section.lower() != "y":
            retry = False

if __name__ == "__main__":
    main()
