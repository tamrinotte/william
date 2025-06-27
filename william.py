# This Python file uses the following encoding: utf-8

# MODULES AND/OR LIBRARIES
from argparse import ArgumentParser
from logging import (
    basicConfig,
    DEBUG,
    CRITICAL,
    disable,
    debug,
    info,
)
from itertools import permutations as iterpermutations
from sys import exit as sysexit

# Logging configuration
basicConfig(level=DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
disable(CRITICAL)



##############################

# CONSTANTS

##############################

__version__ = "William 1.0.1"



##############################

# William Class

##############################

class William:
    def __init__(self, min_words, max_words, modification, wordlist_path, output_path):
        self.min_words = min_words
        self.max_words = max_words
        self.modification = modification
        self.wordlist_path = wordlist_path
        self.output_path = output_path

    def generate_wordlist(self):
        print("Generating a Word List")
        print("-" * 30)

        try:
            with open(self.wordlist_path, "r", encoding="utf-8") as source_file:
                words = source_file.read().splitlines()
        except (FileNotFoundError, IOError) as e:
            print(f"Error reading wordlist: {e}")
            sysexit(1)

        list_of_permutations = []

        for r in range(self.min_words, self.max_words + 1):
            for permutation in iterpermutations(words, r):
                processed_permutation = list(permutation)

                if self.modification == "Capitalize":
                    processed_permutation = [word.capitalize() for word in processed_permutation]
                elif self.modification == "First-Letter":
                    processed_permutation[0] = processed_permutation[0].capitalize()

                list_of_permutations.append("".join(processed_permutation))

        try:
            with open(self.output_path, "w", encoding="utf-8") as output_file:
                output_file.write("\n".join(list_of_permutations))
        except (FileNotFoundError, IOError) as e:
            print(f"Error writing output file: {e}")
            sysexit(1)

        debug(f"Generated permutations: {list_of_permutations}")
        print(f'Generated {len(list_of_permutations)} permutations')
        print(f'Output saved to {self.output_path}')
        info("Word list has been successfully created.")



##############################

# MAIN

##############################

def main():
    parser = ArgumentParser(description="A command-line tool to create a word list from permutations of words.")

    parser.add_argument('-v', '--version', action="store_true",
                        help="Display the application's version information.")

    parser.add_argument("-min", "--minimum", type=int, help="Minimum number of words in a permutation.")
    parser.add_argument("-max", "--maximum", type=int, help="Maximum number of words in a permutation.")

    group = parser.add_mutually_exclusive_group()
    group.add_argument("-c", "--capitalize", action="store_true",
                       help="Capitalize the first letter of each word in a permutation.")
    group.add_argument("-f", "--firstletter", action="store_true",
                       help="Capitalize the first letter of the first word in each permutation.")

    parser.add_argument("source_path", nargs="?", help="Path to your input wordlist file.")
    parser.add_argument("destination_path", nargs="?", help="Path to save the generated wordlist.")

    args = parser.parse_args()

    if args.version:
        print(__version__)
        return

    if not all([args.minimum, args.maximum, args.source_path, args.destination_path]):
        print("Invalid usage. Use -h or --help to get more information.")
        sysexit(1)

    if args.minimum > args.maximum:
        print("Error: Minimum number of words cannot be greater than maximum.")
        sysexit(1)

    modification = None
    if args.capitalize:
        modification = "Capitalize"
    elif args.firstletter:
        modification = "First-Letter"

    app = William(
        min_words=args.minimum,
        max_words=args.maximum,
        modification=modification,
        wordlist_path=args.source_path,
        output_path=args.destination_path
    )
    app.generate_wordlist()

if __name__ == '__main__':
    main()