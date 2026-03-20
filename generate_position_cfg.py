import sys
import argparse

def create_cfg(coords, file_name):
    """
    Creates a .cfg file with cyclic position aliases and mouse binds.

    Parameters:
    coords (list): List of setpos/setang command strings, one per spawn position.
    file_name (str): File name of output config
               
    """

    n = len(coords)

    header = f'// Aliases\nalias "prevPos" "Position{n}"\nalias "nextPos" "Position1"\n\n'
    footer = '\n// Binds\nbind "mouse4" "prevPos"\nbind "mouse5" "nextPos"'

    try:
        with open(file_name, 'w') as file:
            file.write(header)

            for i in range(1, n + 1):
                prev_i = n if i == 1 else i - 1
                next_i = 1 if i == n else i + 1
                file.write(f'alias "Position{i}" "{coords[i - 1]}; alias prevPos Position{prev_i}; alias nextPos Position{next_i}; say {i};"\n')

            file.write(footer)

        print(f"File '{file_name}' has been created and populated successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

def read_positions():
    """
    Reads positions.txt file in same directory and returns array where each element is a given position
    """

    try:
        with open("positions.txt", 'r') as file:
            return file.read().splitlines()

    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    parser = argparse.ArgumentParser(
        description='Creates a .cfg file with cyclic position aliases and mouse binds.'
    )

    parser.add_argument(
        '--output', default='positions.cfg',
        help='Output .cfg file path (default: positions.cfg)'
    )

    args = parser.parse_args()

    SPAWN_COORDS = read_positions()
    create_cfg(SPAWN_COORDS, args.output)

if __name__ == "__main__":
    main()
