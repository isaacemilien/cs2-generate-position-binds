def create_and_populate_cfg_file(file_name, coords):
    """
    Creates a .cfg file, inserts default text, and writes additional lines.

    Parameters:
    file_name (str): The name of the file without the extension.
    num_lines (int): The number of lines to write after the default text.
    """
    if not file_name.endswith('.cfg'):
        file_name += '.cfg'

    num_lines = len(coords) + 1

    default_text = [f'// Aliases \nalias "prevWinSmoke" "WinSmoke{num_lines - 1}" \nalias "nextWinSmoke" "WinSmoke1"\n\n',
                    '\n// Binds \nbind "mouse4" "prevWinSmoke" \nbind "mouse5" "nextWinSmoke"']

    try:
        with open(file_name, 'w') as file:
            file.write(default_text[0])

            for i in range(1, num_lines):
                file.write(f'alias "WinSmoke{i}" "{coords[i - 1]}; alias prevWinSmoke WinSmoke{len(coords) if i == 1 else i - 1}; alias nextWinSmoke WinSmoke{1 if i == len(coords) else i + 1}; say SPAWN {i};"\n')
            
            file.write(default_text[1])

        print(f"File '{file_name}' has been created and populated successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

spawn_coords = ['setpos 1296.000000 32.000000 -103.968750;setang -28.974077 -165.835419 0.000000', 'setpos 1296.000000 -352.000000 -103.968750;setang -42.373402 -173.123993 0.000000', 'setpos 1216.000000 -16.000000 -102.953156;setang -42.527588 -165.856613 0.000000', 'setpos 1216.000000 -115.000000 -102.953156;setang -44.594982 -167.799286 0.000000', 'setpos 1216.000000 -211.000000 -100.616211;setang -45.990883 -170.314789 0.000000', 'setpos 1216.000000 -307.000000 -100.823303;setang -46.432842 -170.927490 0.000000', 'setpos 1135.998657 32.001320 -100.788452;setang -45.408260 -164.407379 0.000000', 'setpos 1136.024658 -63.986389 -100.699768;setang -42.207283 -166.401123 0.000000', 'setpos 1136.052612 -160.017456 -100.667618;setang -42.878700 -168.192429 0.000000', 'setpos 1135.997070 -256.000000 -100.836365;setang -27.521547 -171.046158 0.000000']       

if __name__ == "__main__":
    create_and_populate_cfg_file("mirage_instant_new", spawn_coords)
