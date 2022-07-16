"""
SCRIPT NAME:
    Enigma-ish.py

DESCRIPTION:
    Turns plain text to cypher text and back again.

FUNCTIONS:
    Set_positions()
    Define_rotors()
    Encode()
    Decode()
    Convert_text()

UPDATE RECORD:
Date          Version     Author         Description
03/05/2021    v1.0        Pete Sanders   Created
05/05/2022    v2.0        Pete Sanders   Ammended so that rotors and initial positions
                                         can be set using a single dictionary. Ammended
                                         so that multiple inputs can be used, txt file or 
                                         variable in script.
06/05/2022    v2.1        Pete Sanders   Ammended to convert non-recognised characters to
                                         something recognisable. Made code more efficient.
                                         1000 character: encode = 28.63 sec, decode = 33.91 sec
15/05/2022    v2.2        Pete Sanders   Ammended to change the way that the initial pos is set.                                     
                                         1000 character: encode = 23.40 sec, decode = 24.86 sec
RECOMMENDED FUTURE IMPROVEMENTS:
    Include a reflector and pinboard to properly model enigma.
    Allow the use of additional characters.
    Figure out how to make faster:
        1. Find a more efficient way to set the rotor positions,
        currently there is a bit of wasted processing coding blanks to set the rotors.
"""

#%% Import modules
import pandas as pd
from os.path import exists
import time

# Rotor orders and initial positions.
# Change this based on update from sender. or send in the following format (A1,B2,...,H8)
# where the letter is the rotor number in positional order and the number is the
# initial position of the corresponding rotor.
ROIP = ['A',5,'B',9,'C',10,'D',50,'E',10,'F',40,'G',30,'H',1]

# Text to be encoded or decoded can be entered here either by entering text into the
# "Text_to_be_encoded.txt" and "Text_to_be_decoded.txt"  files in the project folder,
# or by entering text between the '' to insert as a variable.
# Text to be encoded
# 1000 characters

Input_text = ''
if exists("Text_to_be_encoded.txt") == True and Input_text == '':
    Input_text = ''.join(open("Text_to_be_encoded.txt","r").readlines())
   
# Text to be decoded
Cypher_text_3 = ''
if exists("Text_to_be_encoded.txt") == True and Cypher_text_3 == '':
    Cypher_text_3 = ''.join(open("Text_to_be_decoded.txt","r").readlines())

# Print instrustions
print ('Instructions:', '\n',
       'Before entering any text, you will have to "set the rotors":', '\n',
       '    - To do this ammend the "ROIP" dictionary as nessessary,', '\n',
       '    - Rotor letters must be capitals between A and H incl.,', '\n',
       '    - A rotor letter may be used more than once,', '\n',
       '    - Initial positions can be any integer.','\n',
       'When prompted, enter the text to be encoded in the console and press "ENTER"', '\n',
       'If you are only decoding text just press "ENTER"', '\n',
       'When prompted, enter the text to be decoded in the console and press "ENTER"', '\n',
       'Decoded text will be displayed to ensure that the cypher has worked', '\n',)

#%% Set rotor positions
def Set_positions():    
    global Pos

    #This dictionary sets the rotor values and allows the positions of the Rotor_Outputs to be changed    
    Pos = dict([(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10),
                  (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20),
                  (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30),
                  (31, 31), (32, 32), (33, 33), (34, 34), (35, 35), (36, 36), (37, 37)])

#%% Convert text
def Convert_text():
    global Cypher_text_3
    global Input_text
    
    # Convert odd values of input text to something usefull
    Replace = {'\n':' ','!':'','@': 'AT','#':'','$':'','%':'','^':'','&':'','*':'',
               '(':'',')':'','_':'','.':' STOP','?':'',',':'','/':'','|':'','[':'',
               ']':'','{':'','}':'','<':'','>':'',':':'',';':'','':'','':'','':'','':'',
               '':'','':'','':'','':'','':'','':'','':'','':'','':'','':'','':''}
    for key, value in Replace.items():
        Input_text = Input_text.replace(key, value)
        Cypher_text_3 = Cypher_text_3.replace(key, value)
    
#%% Define Rotors
def Define_rotors():
    global Rotor_A
    global Rotor_B
    global Rotor_C
    global Rotor_D
    global Rotor_E
    global Rotor_F
    global Rotor_G
    global Rotor_H
    global Rotor_X
    global Rotor_Input_2
    
    # Setup this DF so that each column is a different rotor and reference this in the
    # encode and decode functions so it doesn't have to be defined each time.
    Rotor_Input_2 = pd.DataFrame ({'Pos':[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                                          21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,36, 37],
                               'Rotor_A':['1', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'J', 'A', 'B', '7', 'D', 'E', 'F', 'G', 'H', 'I', 'T',
                                          '5', '6', 'C', '8', '9', '0', ' ', '2', '3', '4', 'U', 'V', 'W', 'X', 'Y', 'Z', 'K'],
                               'Rotor_B':[' ', '0', '9', '8', '7', '6', '5', '4', '3', '2', '1', 'Z', 'Y', 'X', 'W', 'V', 'U', 'T', 'S', 'R',
                                          'Q','P','O','N','M','L','K','J','I','H', 'G','F','E','D','C', 'B', 'A'],
                               'Rotor_C':['B', 'A', 'D', 'C', 'F', 'E', 'H', 'G', 'J','I', 'L','K','N','M','P','O','R','Q','T','S',
                                          'V','U','X','W','Z','Y','2','1','4','3','6','5','8','7','0', '9', ' '],
                               'Rotor_D':['J', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B','A','T','S','R','Q','P','O','N','M','L','K',
                                          '4','3','2','1','Z','Y','X','W','V','U',' ','0','9','7','8', '6', '5'],
                               'Rotor_E':['L', 'K', 'N', 'M', 'P', 'O', 'R', 'Q', 'T','J','B','A','D','C','F','E','H','3','S','I',
                                          '6','V','8','X','0',' ','1','2','G','4','5','U','7','W','9', 'Y', 'Z'],
                               'Rotor_F':['A', 'K', 'C', 'M', 'E', 'O', 'G', 'Q', 'I','S','B','U','D','W','F','Y','H','1','J','3',
                                          'L','5','N','7','P','9','R',' ','T','4','V','6','X','8','Z', '0', '2'],
                               'Rotor_G':['5', '6', '7', '8', '9', '0', ' ', 'H', 'I','J','U','L','W','N','Y','P','1','2','3','T',
                                          'K','V','M','X','O','Z','Q','R','S','4','A','B','C','D','E', 'F', 'G'],
                               'Rotor_H':['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I','J','K','L','M','N','O','P','Q','R','S','T',
                                          'U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9', '0', ' ']})

    
    # The following dictionaries describe the mapping of each rotor i.e. the letter that appears at position x on the rotor.
    Rotor_A = dict([(37, 'K'), (2, 'L'), (3, 'M'), (4, 'N'), (5, 'O'), (6, 'P'), (7, 'Q'), (8, 'R'), (9, 'S'), (10, 'J'),
                    (11, 'A'), (12, 'B'), (23, 'C'), (14, 'D'), (15, 'E'), (16, 'F'), (17, 'G'), (18, 'H'), (19, 'I'), (30, '4'),
                    (21, '5'), (22, '6'), (13, '7'), (24, '8'), (25, '9'), (26, '0'), (27, ' '), (28, '2'), (29, '3'), (20, 'T'),
                    (31, 'U'), (32, 'V'), (33, 'W'), (34, 'X'), (35, 'Y'), (36, 'Z'), (1, '1')])

    
    Rotor_B = dict([(1, ' '), (2, '0'), (3, '9'), (4, '8'), (5, '7'), (6, '6'), (7, '5'), (8, '4'), (9, '3'), (10, '2'),
                    (11, '1'), (12, 'Z'), (13, 'Y'), (14, 'X'), (15, 'W'), (16, 'V'), (17, 'U'), (18, 'T'), (19, 'S'), (20, 'R'),
                    (21, 'Q'), (22, 'P'), (23, 'O'), (24, 'N'), (25, 'M'), (26, 'L'), (27, 'K'), (28, 'J'), (29, 'I'), (30, 'H'),
                    (31, 'G'), (32, 'F'), (33, 'E'), (34, 'D'), (35, 'C'), (36, 'B'), (37, 'A')])    
    

    Rotor_C = dict([(1, 'B'), (2, 'A'), (3, 'D'), (4, 'C'), (5, 'F'), (6, 'E'), (7, 'H'), (8, 'G'), (9, 'J'), (10, 'I'),
                    (11, 'L'), (12, 'K'), (13, 'N'), (14, 'M'), (15, 'P'), (16, 'O'), (17, 'R'), (18, 'Q'), (19, 'T'), (20, 'S'),
                    (21, 'V'), (22, 'U'), (23, 'X'), (24, 'W'), (25, 'Z'), (26, 'Y'), (27, '2'), (28, '1'), (29, '4'), (30, '3'),
                    (31, '6'), (32, '5'), (33, '8'), (34, '7'), (35, '0'), (36, '9'), (37, ' ')])  

    Rotor_D = dict([(1, 'J'), (2, 'I'), (3, 'H'), (4, 'G'), (5, 'F'), (6, 'E'), (7, 'D'), (8, 'C'), (9, 'B'), (10, 'A'),
                    (11, 'T'), (12, 'S'), (13, 'R'), (14, 'Q'), (15, 'P'), (16, 'O'), (17, 'N'), (18, 'M'), (19, 'L'), (20, 'K'),
                    (21, '4'), (22, '3'), (23, '2'), (24, '1'), (25, 'Z'), (26, 'Y'), (27, 'X'), (28, 'W'), (29, 'V'), (30, 'U'),
                    (31, ' '), (32, '0'), (33, '9'), (34, '7'), (35, '8'), (36, '6'), (37, '5')])

    Rotor_E = dict([(1, 'L'), (2, 'K'), (3, 'N'), (4, 'M'), (5, 'P'), (6, 'O'), (7, 'R'), (8, 'Q'), (9, 'T'), (10, 'J'),
                    (11, 'B'), (12, 'A'), (13, 'D'), (14, 'C'), (15, 'F'), (16, 'E'), (17, 'H'), (18, '3'), (19, 'S'), (20, 'I'),
                    (21, '6'), (22, 'V'), (23, '8'), (24, 'X'), (25, '0'), (26, ' '), (27, '1'), (28, '2'), (29, 'G'), (30, '4'),
                    (31, '5'), (32, 'U'), (33, '7'), (34, 'W'), (35, '9'), (36, 'Y'), (37, 'Z')])  
    
    Rotor_F = dict([(1, 'A'), (2, 'K'), (3, 'C'), (4, 'M'), (5, 'E'), (6, 'O'), (7, 'G'), (8, 'Q'), (9, 'I'), (10, 'S'),
                    (11, 'B'), (12, 'U'), (13, 'D'), (14, 'W'), (15, 'F'), (16, 'Y'), (17, 'H'), (18, '1'), (19, 'J'), (20, '3'),
                    (21, 'L'), (22, '5'), (23, 'N'), (24, '7'), (25, 'P'), (26, '9'), (27, 'R'), (28, ' '), (29, 'T'), (30, '4'),
                    (31, 'V'), (32, '6'), (33, 'X'), (34, '8'), (35, 'Z'), (36, '0'), (37, '2')])
    
    Rotor_G = dict([(1, '5'), (2, '6'), (3, '7'), (4, '8'), (5, '9'), (6, '0'), (7, ' '), (8, 'H'), (9, 'I'), (10, 'J'),
                    (11, 'U'), (12, 'L'), (13, 'W'), (14, 'N'), (15, 'Y'), (16, 'P'), (17, '1'), (18, '2'), (19, '3'), (20, 'T'),
                    (21, 'K'), (22, 'V'), (23, 'M'), (24, 'X'), (25, 'O'), (26, 'Z'), (27, 'Q'), (28, 'R'), (29, 'S'), (30, '4'),
                    (31, 'A'), (32, 'B'), (33, 'C'), (34, 'D'), (35, 'E'), (36, 'F'), (37, 'G')]) 

    Rotor_H = dict([(1, 'A'), (2, 'B'), (3, 'C'), (4, 'D'), (5, 'E'), (6, 'F'), (7, 'G'), (8, 'H'), (9, 'I'), (10, 'J'),
                    (11, 'K'), (12, 'L'), (13, 'M'), (14, 'N'), (15, 'O'), (16, 'P'), (17, 'Q'), (18, 'R'), (19, 'S'), (20, 'T'),
                    (21, 'U'), (22, 'V'), (23, 'W'), (24, 'X'), (25, 'Y'), (26, 'Z'), (27, '1'), (28, '2'), (29, '3'), (30, '4'),
                    (31, '5'), (32, '6'), (33, '7'), (34, '8'), (35, '9'), (36, '0'), (37, ' ')])

Define_rotors()

#%% Encode
def Encode():
    global Rotor_X
    global Cypher_text
    
    # Resets the rotor position
    Set_positions() 
    
    # Define length of text to be decoded
    Input_text_length = len(Input_text)
    
    Letter_num = 0
    
    x = Initial_Pos
    
    # Resets the cypher text given that anything being encoded will be the new cypher text
    Cypher_text = ""
         
    while Letter_num <= Input_text_length:

        # Define rotor inputs and outputs, these will be the letters that are encoded from the rotor.
        # This is just the same as the Rotor_X_ref data frames, I imagine this could be improved
        Rotor_Input = pd.DataFrame ({'Pos':[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
                                    14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24,
                                    25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
                                    36, 37],
                                    'Input':[globals()[Rotor_X][1], globals()[Rotor_X][2], globals()[Rotor_X][3], globals()[Rotor_X][4], globals()[Rotor_X][5], globals()[Rotor_X][6], globals()[Rotor_X][7], globals()[Rotor_X][8], globals()[Rotor_X][9], globals()[Rotor_X][10],
                                        globals()[Rotor_X][11], globals()[Rotor_X][12], globals()[Rotor_X][13], globals()[Rotor_X][14], globals()[Rotor_X][15], globals()[Rotor_X][16], globals()[Rotor_X][17], globals()[Rotor_X][18], globals()[Rotor_X][19], globals()[Rotor_X][20],
                                        globals()[Rotor_X][21], globals()[Rotor_X][22], globals()[Rotor_X][23], globals()[Rotor_X][24], globals()[Rotor_X][25], globals()[Rotor_X][26], globals()[Rotor_X][27], globals()[Rotor_X][28], globals()[Rotor_X][29], globals()[Rotor_X][30],
                                        globals()[Rotor_X][31], globals()[Rotor_X][32], globals()[Rotor_X][33], globals()[Rotor_X][34], globals()[Rotor_X][35], globals()[Rotor_X][36], globals()[Rotor_X][37]]})
      
        # Shifts the Pos value by the initial rotor position
        # Shifts the "Pos" value by 1 (or loops round) which has the effect of moving the 
        # Output column of the Rotor df up by one position but leaving the Input column in place 
        # ((0 + x) % 37) + 1 = take the dictionary ref (0) add the initial position and then add 1
        Rotor_Output = pd.DataFrame ({'Pos':[Pos[((0 + x) % 37) + 1], Pos[((1 + x) % 37) + 1], Pos[((2 + x) % 37) + 1], Pos[((3 + x) % 37) + 1], Pos[((4 + x) % 37) + 1],
                                             Pos[((5 + x) % 37) + 1], Pos[((6 + x) % 37) + 1], Pos[((7 + x) % 37) + 1], Pos[((8 + x) % 37) + 1], Pos[((9 + x) % 37) + 1],
                                             Pos[((10 + x) % 37) + 1], Pos[((11 + x) % 37) + 1], Pos[((12 + x) % 37) + 1], Pos[((13 + x) % 37) + 1], Pos[((14 + x) % 37) + 1],
                                             Pos[((15 + x) % 37) + 1], Pos[((16 + x) % 37) + 1], Pos[((17 + x) % 37) + 1], Pos[((18 + x) % 37) + 1], Pos[((19 + x) % 37) + 1],
                                             Pos[((20 + x) % 37) + 1], Pos[((21 + x) % 37) + 1], Pos[((22 + x) % 37) + 1], Pos[((23 + x) % 37) + 1], Pos[((24 + x) % 37) + 1],
                                             Pos[((25 + x) % 37) + 1], Pos[((26 + x) % 37) + 1], Pos[((27 + x) % 37) + 1], Pos[((28 + x) % 37) + 1], Pos[((29 + x) % 37) + 1],
                                             Pos[((30 + x) % 37) + 1], Pos[((31 + x) % 37) + 1], Pos[((32 + x) % 37) + 1], Pos[((33 + x) % 37) + 1], Pos[((34 + x) % 37) + 1],
                                             Pos[((35 + x) % 37) + 1], Pos[((36 + x) % 37) + 1]],
                                      'Output':[globals()[Rotor_X][1], globals()[Rotor_X][2], globals()[Rotor_X][3], globals()[Rotor_X][4], globals()[Rotor_X][5], globals()[Rotor_X][6], globals()[Rotor_X][7], globals()[Rotor_X][8], globals()[Rotor_X][9], globals()[Rotor_X][10],
                                        globals()[Rotor_X][11], globals()[Rotor_X][12], globals()[Rotor_X][13], globals()[Rotor_X][14], globals()[Rotor_X][15], globals()[Rotor_X][16], globals()[Rotor_X][17], globals()[Rotor_X][18], globals()[Rotor_X][19], globals()[Rotor_X][20],
                                        globals()[Rotor_X][21], globals()[Rotor_X][22], globals()[Rotor_X][23], globals()[Rotor_X][24], globals()[Rotor_X][25], globals()[Rotor_X][26], globals()[Rotor_X][27], globals()[Rotor_X][28], globals()[Rotor_X][29], globals()[Rotor_X][30],
                                        globals()[Rotor_X][31], globals()[Rotor_X][32], globals()[Rotor_X][33], globals()[Rotor_X][34], globals()[Rotor_X][35], globals()[Rotor_X][36], globals()[Rotor_X][37]]})
        
        # If statement ensures encoding 'starts' after the rotor positions have been set.
        # i.e. after the blanks before the start of the text have been encoded.
        if Letter_num >= 1:
            # Merges the 'Rotor_Output' (moving) and 'Rotor_Ref' (fixed) dfs by their positional values  
            Rotor = Rotor_Input.merge(Rotor_Output, how = 'left', on = 'Pos')  
            
            # Identifies the letter to be converted 
            Convert = Input_text_2[Letter_num - 1]

            # Gets the index of the position of the letter to be converted in the Rotor df            
            Cypher_Letter_Index = int(Rotor.index[Rotor['Input'] == Convert].tolist()[0])

            # Returns the 'Output' from the Rotor df i.e. the converted letter        
            Cypher_Letter = Rotor.loc[Cypher_Letter_Index,'Output'] 

            # Creates a string that concatenates all of the converted letters        
            Cypher_text = Cypher_text + Cypher_Letter         
        else:
            pass
        
        # Move the position on one space
        x = x + 1
        
        # Move to the next letter in the text to be encoded
        Letter_num = Letter_num + 1

#%% Decode
def Decode():
    global Rotor_X
    global Decoded_text
    
    Set_positions()  
    
    Cypher_text_length = len(Cypher_text)
    
    Letter_num = 0
    
    x = Initial_Pos    
    
    Decoded_text = ""
                
    while Letter_num <= Cypher_text_length:
        Rotor_Input = pd.DataFrame ({'Pos':[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
                                    14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24,
                                    25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
                                    36, 37],
                                    'Input':[globals()[Rotor_X][1], globals()[Rotor_X][2], globals()[Rotor_X][3], globals()[Rotor_X][4], globals()[Rotor_X][5], globals()[Rotor_X][6], globals()[Rotor_X][7], globals()[Rotor_X][8], globals()[Rotor_X][9], globals()[Rotor_X][10],
                                        globals()[Rotor_X][11], globals()[Rotor_X][12], globals()[Rotor_X][13], globals()[Rotor_X][14], globals()[Rotor_X][15], globals()[Rotor_X][16], globals()[Rotor_X][17], globals()[Rotor_X][18], globals()[Rotor_X][19], globals()[Rotor_X][20],
                                        globals()[Rotor_X][21], globals()[Rotor_X][22], globals()[Rotor_X][23], globals()[Rotor_X][24], globals()[Rotor_X][25], globals()[Rotor_X][26], globals()[Rotor_X][27], globals()[Rotor_X][28], globals()[Rotor_X][29], globals()[Rotor_X][30],
                                        globals()[Rotor_X][31], globals()[Rotor_X][32], globals()[Rotor_X][33], globals()[Rotor_X][34], globals()[Rotor_X][35], globals()[Rotor_X][36], globals()[Rotor_X][37]]})
    
        Rotor_Output = pd.DataFrame ({'Pos':[Pos[((0 - x) % 37) + 1], Pos[((1 - x) % 37) + 1], Pos[((2 - x) % 37) + 1], Pos[((3 - x) % 37) + 1], Pos[((4 - x) % 37) + 1],
                                             Pos[((5 - x) % 37) + 1], Pos[((6 - x) % 37) + 1], Pos[((7 - x) % 37) + 1], Pos[((8 - x) % 37) + 1], Pos[((9 - x) % 37) + 1],
                                             Pos[((10 - x) % 37) + 1], Pos[((11 - x) % 37) + 1], Pos[((12 - x) % 37) + 1], Pos[((13 - x) % 37) + 1], Pos[((14 - x) % 37) + 1],
                                             Pos[((15 - x) % 37) + 1], Pos[((16 - x) % 37) + 1], Pos[((17 - x) % 37) + 1], Pos[((18 - x) % 37) + 1], Pos[((19 - x) % 37) + 1],
                                             Pos[((20 - x) % 37) + 1], Pos[((21 - x) % 37) + 1], Pos[((22 - x) % 37) + 1], Pos[((23 - x) % 37) + 1], Pos[((24 - x) % 37) + 1],
                                             Pos[((25 - x) % 37) + 1], Pos[((26 - x) % 37) + 1], Pos[((27 - x) % 37) + 1], Pos[((28 - x) % 37) + 1], Pos[((29 - x) % 37) + 1],
                                             Pos[((30 - x) % 37) + 1], Pos[((31 - x) % 37) + 1], Pos[((32 - x) % 37) + 1], Pos[((33 - x) % 37) + 1], Pos[((34 - x) % 37) + 1],
                                             Pos[((35 - x) % 37) + 1], Pos[((36 - x) % 37) + 1]],
                                        'Output':[globals()[Rotor_X][1], globals()[Rotor_X][2], globals()[Rotor_X][3], globals()[Rotor_X][4], globals()[Rotor_X][5], globals()[Rotor_X][6], globals()[Rotor_X][7], globals()[Rotor_X][8], globals()[Rotor_X][9], globals()[Rotor_X][10],
                                        globals()[Rotor_X][11], globals()[Rotor_X][12], globals()[Rotor_X][13], globals()[Rotor_X][14], globals()[Rotor_X][15], globals()[Rotor_X][16], globals()[Rotor_X][17], globals()[Rotor_X][18], globals()[Rotor_X][19], globals()[Rotor_X][20],
                                        globals()[Rotor_X][21], globals()[Rotor_X][22], globals()[Rotor_X][23], globals()[Rotor_X][24], globals()[Rotor_X][25], globals()[Rotor_X][26], globals()[Rotor_X][27], globals()[Rotor_X][28], globals()[Rotor_X][29], globals()[Rotor_X][30],
                                        globals()[Rotor_X][31], globals()[Rotor_X][32], globals()[Rotor_X][33], globals()[Rotor_X][34], globals()[Rotor_X][35], globals()[Rotor_X][36], globals()[Rotor_X][37]]})
        
        if Letter_num >= 1:
            Rotor = Rotor_Input.merge(Rotor_Output, how = 'left', on = 'Pos')  
            Convert = Cypher_text_2[Letter_num - 1]
            Decoded_letter_index = int(Rotor.index[Rotor['Input'] == Convert].tolist()[0])
            Decoded_Letter = Rotor.loc[Decoded_letter_index,'Output']            
            Decoded_text = Decoded_text + Decoded_Letter
        else:
            pass

        x = x + 1            
        
        Letter_num = Letter_num + 1
            
#%% Encode Text 
Convert_text()
Define_rotors()
if Input_text == '':
    Input_text = input('Enter text to be encoded: ')
else:
    print('Text to be encoded: provided elsewhere')

if Input_text == '':
    Input_text = 'Trial text'
else:
    pass

Input_text = Input_text.upper()
Input_text_2 = Input_text

Encode_start = time.time()
# All of this could be run as a loop but i wonder if that would slow things down?
#Rotor 1
Initial_Pos = ROIP[1] 
globals()['Rotor_X'] = 'Rotor_' + ROIP[0]
Encode()
Input_text_2 = Cypher_text

#Rotor 2
Initial_Pos = ROIP[3]
globals()['Rotor_X'] = 'Rotor_' + ROIP[2]
Encode()
Input_text_2 = Cypher_text

#Rotor 3
Initial_Pos = ROIP[5]
globals()['Rotor_X'] = 'Rotor_' + ROIP[4]
Encode()
Input_text_2 = Cypher_text

#Rotor 4
Initial_Pos = ROIP[7]
globals()['Rotor_X'] = 'Rotor_' + ROIP[6]
Encode()
Input_text_2 = Cypher_text

#Rotor 5
Initial_Pos = ROIP[9]
globals()['Rotor_X'] = 'Rotor_' + ROIP[8]
Encode()
Input_text_2 = Cypher_text

#Rotor 6
Initial_Pos = ROIP[11]
globals()['Rotor_X'] = 'Rotor_' + ROIP[10]
Encode()
Input_text_2 = Cypher_text

#Rotor 7
Initial_Pos = ROIP[13]
globals()['Rotor_X'] = 'Rotor_' + ROIP[12]
Encode()
Input_text_2 = Cypher_text

#Rotor 8
Initial_Pos = ROIP[15]
globals()['Rotor_X'] = 'Rotor_' + ROIP[14]
Encode()
Input_text_2 = Cypher_text

print('Cypher text: ' + Cypher_text)
Encode_end = time.time()

#%% Decode Text
Convert_text()
Define_rotors()

if Cypher_text_3 == '':
    Cypher_text_3 = input('Enter text to be decoded: ')
else:
    print('Text to be decoded: provided elsewhere')

if Cypher_text_3 == '':
    Cypher_text = Cypher_text
else:
    Cypher_text = Cypher_text_3

Cypher_text_2 = Cypher_text

Decode_start = time.time()
# All of this could be run as a loop but i wonder if that would slow things down?
# Rotor 8
Initial_Pos = ROIP[15]
globals()['Rotor_X'] = 'Rotor_' + ROIP[14]
Decode()
Cypher_text_2 = Decoded_text

#Rotor 7
Initial_Pos = ROIP[13]
globals()['Rotor_X'] = 'Rotor_' + ROIP[12]
Decode()
Cypher_text_2 = Decoded_text

#Rotor 6
Initial_Pos = ROIP[11]
globals()['Rotor_X'] = 'Rotor_' + ROIP[10]
Decode()
Cypher_text_2 = Decoded_text

#Rotor 5
Initial_Pos = ROIP[9]
globals()['Rotor_X'] = 'Rotor_' + ROIP[8]
Decode()
Cypher_text_2 = Decoded_text

#Rotor 4
Initial_Pos = ROIP[7]
globals()['Rotor_X'] = 'Rotor_' + ROIP[6]
Decode()
Cypher_text_2 = Decoded_text

#Rotor 3
Initial_Pos = ROIP[5]
globals()['Rotor_X'] = 'Rotor_' + ROIP[4]
Decode()
Cypher_text_2 = Decoded_text

#Rotor 2
Initial_Pos = ROIP[3]
globals()['Rotor_X'] = 'Rotor_' + ROIP[2]
Decode()
Cypher_text_2 = Decoded_text

#Rotor 1
Initial_Pos = ROIP[1]
globals()['Rotor_X'] = 'Rotor_' + ROIP[0]
Decode()
Cypher_text_2 = Decoded_text

print('Decoded text: ' + Decoded_text)
Decode_end = time.time()

#%% Outputs Cyphr text to txt
File_save = input('Do you want to save the outputs (Y,N): ')

if File_save == 'Y' or File_save == 'y':
    Cypher_txt = open("Cypher_text.txt","w")
    Cypher_txt.write(Cypher_text)
    Cypher_txt.close()

    Decoded_txt = open("Decoded_text.txt","w")
    Decoded_txt.write(Decoded_text)
    Decoded_txt.close()
    
    print('Files saved')
    
else:
    print('Files not saved')

print("Encode length = %s characters" % (len(Cypher_text))) 
print("Encode time = %s sec" % (Encode_end - Encode_start)) 
print("Decode length = %s characters" % (len(Decoded_text)))    
print("Decode time = %s sec" % (Decode_end - Decode_start))
