def find_keypad_position(keypad, key):
    for row in range(3):
        for col in range(3):
            if keypad[row][col] == key:
                return row, col

def time_to_type_security_code(security_code, keypad):
    prev_row, prev_col = find_keypad_position(keypad, security_code[0])
    time = 0
    
    for i in range(1, len(security_code)):
        curr_row, curr_col = find_keypad_position(keypad, security_code[i])
        time += max(abs(curr_row - prev_row), abs(curr_col - prev_col))
        prev_row, prev_col = curr_row, curr_col
        
    return time

# Example usage
security_code = "11155477859398971132961998532135614872553497529583463454768527245372149482886656721688398794219213151993969924986364673428956257888563261646413388287127458486219764179416164772599593996467797627719969413572749897992478243144878947425442749753688987693851767249945958455313341589232625915632593597264614124212744378584992258641341142961521962839965877466471718687745348357344684195878191793792392781963529558759594428349918983771442736522827227147187814577213667863172655968964391114263718568899481733313539792528614229496543829484542855459434582412519547192985977916512114955926516538118838611661638226227334951264753351513928326439243655291446257546198398385254226936695278127798798"
keypad_str = "521837496"
keypad_matrix = [[int(keypad_str[i*3+j]) for j in range(3)] for i in range(3)]

# Convert security_code string to list of integers
security_code_list = [int(x) for x in security_code]

result = time_to_type_security_code(security_code_list, keypad_matrix)
print(result)
