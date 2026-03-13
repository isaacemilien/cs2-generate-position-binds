def create_cfg(coords, prefix="positions"):
    """
    Creates a .cfg file with cyclic position aliases and mouse binds.

    Parameters:
    coords (list): List of setpos/setang command strings, one per spawn position.
    prefix (str): Optional prefix for the output filename. Defaults to "positions".
                  e.g. prefix="mirage" -> "mirage_positions.cfg"
    """
    n = len(coords)
    file_name = f"{prefix}_positions.cfg" if prefix != "positions" else "positions.cfg"

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

# Example setpos commands, will assume setpos commands will be argument in future
setpos_commands = [
    'setpos 1296.000000 32.000000 -103.968750;setang -28.974077 -165.835419 0.000000',
    'setpos 1296.000000 -352.000000 -103.968750;setang -42.373402 -173.123993 0.000000',
    'setpos 1216.000000 -16.000000 -102.953156;setang -42.527588 -165.856613 0.000000',
    'setpos 1216.000000 -115.000000 -102.953156;setang -44.594982 -167.799286 0.000000',
    'setpos 1216.000000 -211.000000 -100.616211;setang -45.990883 -170.314789 0.000000',
    'setpos 1216.000000 -307.000000 -100.823303;setang -46.432842 -170.927490 0.000000',
    'setpos 1135.998657 32.001320 -100.788452;setang -45.408260 -164.407379 0.000000',
    'setpos 1136.024658 -63.986389 -100.699768;setang -42.207283 -166.401123 0.000000',
    'setpos 1136.052612 -160.017456 -100.667618;setang -42.878700 -168.192429 0.000000',
    'setpos 1135.997070 -256.000000 -100.836365;setang -27.521547 -171.046158 0.000000',
]

if __name__ == "__main__":
    create_cfg(setpos_commands)
