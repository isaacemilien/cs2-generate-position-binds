def remove_text_before_setpos(input_text):
    """
    Removes all text before the word "setpos" on each line of the given string of text.

    Parameters:
    input_text (str): The input string containing multiple lines of text.

    Returns:
    str: A string with text before "setpos" removed from each line.
    """
    lines = input_text.split('\n')
    
    processed_lines = [line[line.find('setpos'):] if 'setpos' in line else '' for line in lines]
    
    processed_lines = [line for line in processed_lines if line]
    
    output_text = '\n'.join(processed_lines)
    
    return output_text

input_text = """Spawn 1: setpos 1296.000000 32.000000 -103.968750;setang -28.974077 -165.835419 0.000000
Spawn 2: setpos 1296.000000 -352.000000 -103.968750;setang -42.373402 -173.123993 0.000000
Spawn 3: setpos 1216.000000 -16.000000 -102.953156;setang -42.527588 -165.856613 0.000000
Spawn 4: setpos 1216.000000 -115.000000 -102.953156;setang -44.594982 -167.799286 0.000000
Spawn 5: setpos 1216.000000 -211.000000 -100.616211;setang -45.990883 -170.314789 0.000000
Spawn 6: setpos 1216.000000 -307.000000 -100.823303;setang -46.432842 -170.927490 0.000000
SPAWN 7: setpos 1135.998657 32.001320 -100.788452;setang -45.408260 -164.407379 0.000000
SPAWN 8: setpos 1136.024658 -63.986389 -100.699768;setang -42.207283 -166.401123 0.000000
SPAWN 9: setpos 1136.052612 -160.017456 -100.667618;setang -42.878700 -168.192429 0.000000
SPAWN 10: setpos 1135.997070 -256.000000 -100.836365;setang -27.521547 -171.046158 0.000000"""

processed_text = remove_text_before_setpos(input_text)
print(processed_text.splitlines())
