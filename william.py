from argparse import ArgumentParser
from logging import basicConfig, DEBUG, debug, disable, CRITICAL
from itertools import combinations as itercombinations
from sys import exit as sysexit

# Doing the basic configuration for the debugging feature
basicConfig(level=DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Disabling the debugging feature. Comment out the line to enable debugging.
disable(CRITICAL)

class William:

    def __init__(self, min, max, modification, wordlist, output):
        
        self.version = "William 1.0.1"

        self.min = int(min)

        self.max = int(max)

        self.modification = modification

        self.wordlist = wordlist
        
        self.output = output

    def generate_wordlist(self):
        """A function which generates a word list from an another wordlist""" 

        print("Generating a Word List")

        print("-" * 30)

        # Read words from the source file
        with open(self.wordlist, "r") as source_file:

            words = source_file.read().splitlines()

        # Generate combinations of words
        combinations = []

        for r in range(self.min, self.max + 1):

            for combo in itercombinations(words, r):

                if self.modification == "Capitalize":

                    combo = [word.capitalize() for word in combo]

                elif self.modification == "First-Word":

                    combo = [combo[0].capitalize()] + list(combo[1:])

                combinations.append("".join(combo))

        # Write the generated wordlist to the output file
        with open(self.output, "w") as output_file:

            output_file.write("\n".join(combinations))

        debug(combinations)

        print(f'Generated {len(combinations)} combinations')

        print(f'Output saved to {self.output}')

    def display_version(self):
        """A function which displays the application version"""

        print(self.version)

def main():
    """The main function which runs the entire application"""

    # Create an argument parser
    parser = ArgumentParser(description="A command line tool to create a word list from combination of words.")

    # Add arguments
    parser.add_argument('-v', '--version', action="store_true", help="Display the application's version information",)

    parser.add_argument("-min", "--minimum", help="Minimum length of a word combination",)

    parser.add_argument("-max", "--maximum", help="Maximum length of a word combination",)

    parser.add_argument("-c", "--capitalize", action="store_true", help="Capitalize each sub word's first letter")

    parser.add_argument("-f", "--firstword", action="store_true", help="Capitalize each word's first letter")

    parser.add_argument("source_path", nargs="?", help="Source path of your wordlist")
    
    parser.add_argument("destination_path", nargs="?", help="Destination path of your wordlist")

    # Parse the arguments
    args = parser.parse_args()

    if args.version:
    
        app = William(0, 0, None, None, None)  # Pass None since wordlist is not used here
    
        app.display_version()

    elif args.minimum and args.maximum and args.source_path and args.destination_path:

        if args.capitalize and not args.firstword:

            modification = "Capitalize"    

        elif args.firstword and not args.capitalize:

            modification = "First-Word"

        elif args.capitalize and args.firstword:

            print("You can't use capitalize and firstword arguments at the same time.")

            sysexit()

        else:

            modification = None

        app = William(min=args.minimum, max=args.maximum, modification=modification, wordlist=args.source_path, output=args.destination_path)

        app.generate_wordlist()

    else:

         print("Invalid usage. Use -h or --help to get more information.")


# Evaluate if the source is being run on its own or being imported somewhere else. With this conditional in place, your code can not be imported somewhere else.
if __name__ == '__main__':
    main()
