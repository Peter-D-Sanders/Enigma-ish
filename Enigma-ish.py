"""
SCRIPT NAME:
    Enigma-ish.py

DESCRIPTION:
    Turns plain text to cypher text and back again.

FUNCTIONS:
    Set_positions()
    Define_rotors()
    Rotor_A-H_Encode()
    Rotor_A-H_Decode()
    
UPDATE RECORD:
Date          Version     Author         Description
03/05/2021    v1.0        Pete Sanders   Created
                                         
RECOMMENDED FUTURE IMPROVEMENTS:
    Include a reflector and pinboard to properly model enigma.
    Check to see if input text is alphanumeric with spaces.
"""

#%% Import modules
import pandas as pd

# Print instrustions
print ('Instructions:', '\n',
       'Before entering any text, you will have to "set the rotors":', '\n',
       '    To do this ensure that the rotors, and their initial positions in the "Encode Text",', '\n',
       '    and "Decode Text", sections are the same.', '\n',
       '    The rotors in the decode text section should be in reverse order.', '\n',   
       'When prompted, enter the text to be encoded in the console and press "ENTER"', '\n',
       'If you are only decoding text just press "ENTER"', '\n',
       'When prompted, enter the text to be decoded in the console and press "ENTER"', '\n',
       'Decoded text will be displayed to ensure that the cypher has worked', '\n',)

Initial_Pos = 0

#%% Set rotor positions
def Set_positions():    
    global Pos

#This dictionary sets the rotor values and allows the positions of the Rotor_Outputs to be changed    
    Pos = dict([(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10),
                  (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20),
                  (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30),
                  (31, 31), (32, 32), (33, 33), (34, 34), (35, 35), (36, 36), (37, 37)]) 

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
    
    global Rotor_A_Ref
    global Rotor_B_Ref
    global Rotor_C_Ref
    global Rotor_D_Ref
    global Rotor_E_Ref
    global Rotor_F_Ref
    global Rotor_G_Ref
    global Rotor_H_Ref
    
#Dictionaries that describe the mapping of each rotor.
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

#References for each rotor, reference rotors have fixed positions.
    Rotor_A_Ref = pd.DataFrame ({'Pos':[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
                                    14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24,
                                    25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
                                    36, 37],
                                 'Input':[Rotor_A[1], Rotor_A[2], Rotor_A[3], Rotor_A[4], Rotor_A[5], Rotor_A[6], Rotor_A[7], Rotor_A[8], Rotor_A[9], Rotor_A[10],
                                        Rotor_A[11], Rotor_A[12], Rotor_A[13], Rotor_A[14], Rotor_A[15], Rotor_A[16], Rotor_A[17], Rotor_A[18], Rotor_A[19], Rotor_A[20],
                                        Rotor_A[21], Rotor_A[22], Rotor_A[23], Rotor_A[24], Rotor_A[25], Rotor_A[26], Rotor_A[27], Rotor_A[28], Rotor_A[29], Rotor_A[30],
                                        Rotor_A[31], Rotor_A[32], Rotor_A[33], Rotor_A[34], Rotor_A[35], Rotor_A[36], Rotor_A[37]]})
    
    Rotor_B_Ref = pd.DataFrame ({'Pos':[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
                                    14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24,
                                    25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
                                    36, 37],
                                 'Input':[Rotor_B[1], Rotor_B[2], Rotor_B[3], Rotor_B[4], Rotor_B[5], Rotor_B[6], Rotor_B[7], Rotor_B[8], Rotor_B[9], Rotor_B[10],
                                        Rotor_B[11], Rotor_B[12], Rotor_B[13], Rotor_B[14], Rotor_B[15], Rotor_B[16], Rotor_B[17], Rotor_B[18], Rotor_B[19], Rotor_B[20],
                                        Rotor_B[21], Rotor_B[22], Rotor_B[23], Rotor_B[24], Rotor_B[25], Rotor_B[26], Rotor_B[27], Rotor_B[28], Rotor_B[29], Rotor_B[30],
                                        Rotor_B[31], Rotor_B[32], Rotor_B[33], Rotor_B[34], Rotor_B[35], Rotor_B[36], Rotor_B[37]]})    
    
    Rotor_C_Ref = pd.DataFrame ({'Pos':[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
                                    14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24,
                                    25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
                                    36, 37],
                                 'Input':[Rotor_C[1], Rotor_C[2], Rotor_C[3], Rotor_C[4], Rotor_C[5], Rotor_C[6], Rotor_C[7], Rotor_C[8], Rotor_C[9], Rotor_C[10],
                                        Rotor_C[11], Rotor_C[12], Rotor_C[13], Rotor_C[14], Rotor_C[15], Rotor_C[16], Rotor_C[17], Rotor_C[18], Rotor_C[19], Rotor_C[20],
                                        Rotor_C[21], Rotor_C[22], Rotor_C[23], Rotor_C[24], Rotor_C[25], Rotor_C[26], Rotor_C[27], Rotor_C[28], Rotor_C[29], Rotor_C[30],
                                        Rotor_C[31], Rotor_C[32], Rotor_C[33], Rotor_C[34], Rotor_C[35], Rotor_C[36], Rotor_C[37]]})

    Rotor_D_Ref = pd.DataFrame ({'Pos':[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
                                    14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24,
                                    25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
                                    36, 37],
                                 'Input':[Rotor_D[1], Rotor_D[2], Rotor_D[3], Rotor_D[4], Rotor_D[5], Rotor_D[6], Rotor_D[7], Rotor_D[8], Rotor_D[9], Rotor_D[10],
                                        Rotor_D[11], Rotor_D[12], Rotor_D[13], Rotor_D[14], Rotor_D[15], Rotor_D[16], Rotor_D[17], Rotor_D[18], Rotor_D[19], Rotor_D[20],
                                        Rotor_D[21], Rotor_D[22], Rotor_D[23], Rotor_D[24], Rotor_D[25], Rotor_D[26], Rotor_D[27], Rotor_D[28], Rotor_D[29], Rotor_D[30],
                                        Rotor_D[31], Rotor_D[32], Rotor_D[33], Rotor_D[34], Rotor_D[35], Rotor_D[36], Rotor_D[37]]})
    
    Rotor_E_Ref = pd.DataFrame ({'Pos':[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
                                    14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24,
                                    25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
                                    36, 37],
                                 'Input':[Rotor_E[1], Rotor_E[2], Rotor_E[3], Rotor_E[4], Rotor_E[5], Rotor_E[6], Rotor_E[7], Rotor_E[8], Rotor_E[9], Rotor_E[10],
                                        Rotor_E[11], Rotor_E[12], Rotor_E[13], Rotor_E[14], Rotor_E[15], Rotor_E[16], Rotor_E[17], Rotor_E[18], Rotor_E[19], Rotor_E[20],
                                        Rotor_E[21], Rotor_E[22], Rotor_E[23], Rotor_E[24], Rotor_E[25], Rotor_E[26], Rotor_E[27], Rotor_E[28], Rotor_E[29], Rotor_E[30],
                                        Rotor_E[31], Rotor_E[32], Rotor_E[33], Rotor_E[34], Rotor_E[35], Rotor_E[36], Rotor_E[37]]})

    Rotor_F_Ref = pd.DataFrame ({'Pos':[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
                                    14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24,
                                    25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
                                    36, 37],
                                 'Input':[Rotor_F[1], Rotor_F[2], Rotor_F[3], Rotor_F[4], Rotor_F[5], Rotor_F[6], Rotor_F[7], Rotor_F[8], Rotor_F[9], Rotor_F[10],
                                        Rotor_F[11], Rotor_F[12], Rotor_F[13], Rotor_F[14], Rotor_F[15], Rotor_F[16], Rotor_F[17], Rotor_F[18], Rotor_F[19], Rotor_F[20],
                                        Rotor_F[21], Rotor_F[22], Rotor_F[23], Rotor_F[24], Rotor_F[25], Rotor_F[26], Rotor_F[27], Rotor_F[28], Rotor_F[29], Rotor_F[30],
                                        Rotor_F[31], Rotor_F[32], Rotor_F[33], Rotor_F[34], Rotor_F[35], Rotor_F[36], Rotor_F[37]]})

    Rotor_G_Ref = pd.DataFrame ({'Pos':[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
                                    14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24,
                                    25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
                                    36, 37],
                                 'Input':[Rotor_G[1], Rotor_G[2], Rotor_G[3], Rotor_G[4], Rotor_G[5], Rotor_G[6], Rotor_G[7], Rotor_G[8], Rotor_G[9], Rotor_G[10],
                                        Rotor_G[11], Rotor_G[12], Rotor_G[13], Rotor_G[14], Rotor_G[15], Rotor_G[16], Rotor_G[17], Rotor_G[18], Rotor_G[19], Rotor_G[20],
                                        Rotor_G[21], Rotor_G[22], Rotor_G[23], Rotor_G[24], Rotor_G[25], Rotor_G[26], Rotor_G[27], Rotor_G[28], Rotor_G[29], Rotor_G[30],
                                        Rotor_G[31], Rotor_G[32], Rotor_G[33], Rotor_G[34], Rotor_G[35], Rotor_G[36], Rotor_G[37]]})

    Rotor_H_Ref = pd.DataFrame ({'Pos':[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
                                    14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24,
                                    25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
                                    36, 37],
                                 'Input':[Rotor_H[1], Rotor_H[2], Rotor_H[3], Rotor_H[4], Rotor_H[5], Rotor_H[6], Rotor_H[7], Rotor_H[8], Rotor_H[9], Rotor_H[10],
                                        Rotor_H[11], Rotor_H[12], Rotor_H[13], Rotor_H[14], Rotor_H[15], Rotor_H[16], Rotor_H[17], Rotor_H[18], Rotor_H[19], Rotor_H[20],
                                        Rotor_H[21], Rotor_H[22], Rotor_H[23], Rotor_H[24], Rotor_H[25], Rotor_H[26], Rotor_H[27], Rotor_H[28], Rotor_H[29], Rotor_H[30],
                                        Rotor_H[31], Rotor_H[32], Rotor_H[33], Rotor_H[34], Rotor_H[35], Rotor_H[36], Rotor_H[37]]})

#%% Encode text, each rotor is encoded seperately
def Rotor_A_Encode():

    Set_positions()    

    global Cypher_text
    Input_text_length = len(Input_text)
    Letter_num = Initial_Pos * -1
    
    Cypher_text = ""
          
    while Letter_num <= Input_text_length:

#Rotor_Outputs (poor name) have mutable positions, and therefore move 'against' the rotor references to produce a different output.
#Both Rotor_Outputs and reference rotors 'look' at the same rotor dictionary.        
        Rotor_Output = pd.DataFrame ({'Pos':[Pos[1], Pos[2], Pos[3], Pos[4], Pos[5], Pos[6], Pos[7], Pos[8], Pos[9], Pos[10],
                                        Pos[11], Pos[12], Pos[13], Pos[14], Pos[15], Pos[16], Pos[17], Pos[18], Pos[19], Pos[20],
                                        Pos[21], Pos[22], Pos[23], Pos[24], Pos[25], Pos[26], Pos[27], Pos[28], Pos[29], Pos[30],
                                        Pos[31], Pos[32], Pos[33], Pos[34], Pos[35], Pos[36], Pos[37]],
                                      'Output':[Rotor_A[1], Rotor_A[2], Rotor_A[3], Rotor_A[4], Rotor_A[5], Rotor_A[6], Rotor_A[7], Rotor_A[8], Rotor_A[9], Rotor_A[10],
                                        Rotor_A[11], Rotor_A[12], Rotor_A[13], Rotor_A[14], Rotor_A[15], Rotor_A[16], Rotor_A[17], Rotor_A[18], Rotor_A[19], Rotor_A[20],
                                        Rotor_A[21], Rotor_A[22], Rotor_A[23], Rotor_A[24], Rotor_A[25], Rotor_A[26], Rotor_A[27], Rotor_A[28], Rotor_A[29], Rotor_A[30],
                                        Rotor_A[31], Rotor_A[32], Rotor_A[33], Rotor_A[34], Rotor_A[35], Rotor_A[36], Rotor_A[37]]})
        
        if Letter_num >= 1:
            Rotor = Rotor_A_Ref.merge(Rotor_Output, how = 'left', on = 'Pos')  
        
            Convert = pd.DataFrame ({'Input': [Input_text_2[Letter_num - 1]]})
        
            Cypher_Letter = Convert.merge(Rotor, how = 'left', on = 'Input')
        
            Cypher_text = Cypher_text + Cypher_Letter.iloc[0]['Output']
        else:
            pass
        
        x = 1
        
        while x < 38:
            if Pos[x] + 1 == 38:
                Pos[x] = 1
            else:
                Pos[x] = Pos[x] + 1  
            
            x = x + 1
        
        Letter_num = Letter_num + 1

def Rotor_B_Encode():
    global Cypher_text
    Input_text_length = len(Input_text)
    Letter_num = Initial_Pos * -1

    Set_positions()    
    
    Cypher_text = ""
      
    while Letter_num <= Input_text_length:
        
        x = 1        
        
        Rotor_Output = pd.DataFrame ({'Pos':[Pos[1], Pos[2], Pos[3], Pos[4], Pos[5], Pos[6], Pos[7], Pos[8], Pos[9], Pos[10],
                                        Pos[11], Pos[12], Pos[13], Pos[14], Pos[15], Pos[16], Pos[17], Pos[18], Pos[19], Pos[20],
                                        Pos[21], Pos[22], Pos[23], Pos[24], Pos[25], Pos[26], Pos[27], Pos[28], Pos[29], Pos[30],
                                        Pos[31], Pos[32], Pos[33], Pos[34], Pos[35], Pos[36], Pos[37]],
                                      'Output':[Rotor_B[1], Rotor_B[2], Rotor_B[3], Rotor_B[4], Rotor_B[5], Rotor_B[6], Rotor_B[7], Rotor_B[8], Rotor_B[9], Rotor_B[10],
                                        Rotor_B[11], Rotor_B[12], Rotor_B[13], Rotor_B[14], Rotor_B[15], Rotor_B[16], Rotor_B[17], Rotor_B[18], Rotor_B[19], Rotor_B[20],
                                        Rotor_B[21], Rotor_B[22], Rotor_B[23], Rotor_B[24], Rotor_B[25], Rotor_B[26], Rotor_B[27], Rotor_B[28], Rotor_B[29], Rotor_B[30],
                                        Rotor_B[31], Rotor_B[32], Rotor_B[33], Rotor_B[34], Rotor_B[35], Rotor_B[36], Rotor_B[37]]})
    
        if Letter_num >= 1:
            Rotor = Rotor_B_Ref.merge(Rotor_Output, how = 'left', on = 'Pos')  
        
            Convert = pd.DataFrame ({'Input': [Input_text_2[Letter_num - 1]]})
        
            Cypher_Letter = Convert.merge(Rotor, how = 'left', on = 'Input')
        
            Cypher_text = Cypher_text + Cypher_Letter.iloc[0]['Output']
        else:
            pass
        
        x = 1
        
        while x < 38:
            if Pos[x] + 1 == 38:
                Pos[x] = 1
            else:
                Pos[x] = Pos[x] + 1  
            
            x = x + 1
        
        Letter_num = Letter_num + 1

def Rotor_C_Encode():
    global Cypher_text
    Input_text_length = len(Input_text)
    Letter_num = Initial_Pos * -1

    Set_positions()    

    
    Cypher_text = ""
      
    while Letter_num <= Input_text_length:
        
        x = 1        
        
        Rotor_Output = pd.DataFrame ({'Pos':[Pos[1], Pos[2], Pos[3], Pos[4], Pos[5], Pos[6], Pos[7], Pos[8], Pos[9], Pos[10],
                                        Pos[11], Pos[12], Pos[13], Pos[14], Pos[15], Pos[16], Pos[17], Pos[18], Pos[19], Pos[20],
                                        Pos[21], Pos[22], Pos[23], Pos[24], Pos[25], Pos[26], Pos[27], Pos[28], Pos[29], Pos[30],
                                        Pos[31], Pos[32], Pos[33], Pos[34], Pos[35], Pos[36], Pos[37]],
                                      'Output':[Rotor_C[1], Rotor_C[2], Rotor_C[3], Rotor_C[4], Rotor_C[5], Rotor_C[6], Rotor_C[7], Rotor_C[8], Rotor_C[9], Rotor_C[10],
                                        Rotor_C[11], Rotor_C[12], Rotor_C[13], Rotor_C[14], Rotor_C[15], Rotor_C[16], Rotor_C[17], Rotor_C[18], Rotor_C[19], Rotor_C[20],
                                        Rotor_C[21], Rotor_C[22], Rotor_C[23], Rotor_C[24], Rotor_C[25], Rotor_C[26], Rotor_C[27], Rotor_C[28], Rotor_C[29], Rotor_C[30],
                                        Rotor_C[31], Rotor_C[32], Rotor_C[33], Rotor_C[34], Rotor_C[35], Rotor_C[36], Rotor_C[37]]})
    
        if Letter_num >= 1:
            Rotor = Rotor_C_Ref.merge(Rotor_Output, how = 'left', on = 'Pos')  
        
            Convert = pd.DataFrame ({'Input': [Input_text_2[Letter_num - 1]]})
        
            Cypher_Letter = Convert.merge(Rotor, how = 'left', on = 'Input')
        
            Cypher_text = Cypher_text + Cypher_Letter.iloc[0]['Output']
        else:
            pass
        
        x = 1
        
        while x < 38:
            if Pos[x] + 1 == 38:
                Pos[x] = 1
            else:
                Pos[x] = Pos[x] + 1  
            
            x = x + 1
        
        Letter_num = Letter_num + 1


def Rotor_D_Encode():
    global Cypher_text
    Input_text_length = len(Input_text)
    Letter_num = Initial_Pos * -1

    Set_positions()    

    
    Cypher_text = ""
      
    while Letter_num <= Input_text_length:
        
        x = 1        
        
        Rotor_Output = pd.DataFrame ({'Pos':[Pos[1], Pos[2], Pos[3], Pos[4], Pos[5], Pos[6], Pos[7], Pos[8], Pos[9], Pos[10],
                                        Pos[11], Pos[12], Pos[13], Pos[14], Pos[15], Pos[16], Pos[17], Pos[18], Pos[19], Pos[20],
                                        Pos[21], Pos[22], Pos[23], Pos[24], Pos[25], Pos[26], Pos[27], Pos[28], Pos[29], Pos[30],
                                        Pos[31], Pos[32], Pos[33], Pos[34], Pos[35], Pos[36], Pos[37]],
                                      'Output':[Rotor_D[1], Rotor_D[2], Rotor_D[3], Rotor_D[4], Rotor_D[5], Rotor_D[6], Rotor_D[7], Rotor_D[8], Rotor_D[9], Rotor_D[10],
                                        Rotor_D[11], Rotor_D[12], Rotor_D[13], Rotor_D[14], Rotor_D[15], Rotor_D[16], Rotor_D[17], Rotor_D[18], Rotor_D[19], Rotor_D[20],
                                        Rotor_D[21], Rotor_D[22], Rotor_D[23], Rotor_D[24], Rotor_D[25], Rotor_D[26], Rotor_D[27], Rotor_D[28], Rotor_D[29], Rotor_D[30],
                                        Rotor_D[31], Rotor_D[32], Rotor_D[33], Rotor_D[34], Rotor_D[35], Rotor_D[36], Rotor_D[37]]})
    
        if Letter_num >= 1:
            Rotor = Rotor_D_Ref.merge(Rotor_Output, how = 'left', on = 'Pos')  
        
            Convert = pd.DataFrame ({'Input': [Input_text_2[Letter_num - 1]]})
        
            Cypher_Letter = Convert.merge(Rotor, how = 'left', on = 'Input')
        
            Cypher_text = Cypher_text + Cypher_Letter.iloc[0]['Output']
        else:
            pass
        
        x = 1
        
        while x < 38:
            if Pos[x] + 1 == 38:
                Pos[x] = 1
            else:
                Pos[x] = Pos[x] + 1  
            
            x = x + 1
        
        Letter_num = Letter_num + 1

def Rotor_E_Encode():
    global Cypher_text
    Input_text_length = len(Input_text)
    Letter_num = Initial_Pos * -1

    Set_positions()    

    
    Cypher_text = ""
      
    while Letter_num <= Input_text_length:
        
        x = 1        
        
        Rotor_Output = pd.DataFrame ({'Pos':[Pos[1], Pos[2], Pos[3], Pos[4], Pos[5], Pos[6], Pos[7], Pos[8], Pos[9], Pos[10],
                                        Pos[11], Pos[12], Pos[13], Pos[14], Pos[15], Pos[16], Pos[17], Pos[18], Pos[19], Pos[20],
                                        Pos[21], Pos[22], Pos[23], Pos[24], Pos[25], Pos[26], Pos[27], Pos[28], Pos[29], Pos[30],
                                        Pos[31], Pos[32], Pos[33], Pos[34], Pos[35], Pos[36], Pos[37]],
                                      'Output':[Rotor_E[1], Rotor_E[2], Rotor_E[3], Rotor_E[4], Rotor_E[5], Rotor_E[6], Rotor_E[7], Rotor_E[8], Rotor_E[9], Rotor_E[10],
                                        Rotor_E[11], Rotor_E[12], Rotor_E[13], Rotor_E[14], Rotor_E[15], Rotor_E[16], Rotor_E[17], Rotor_E[18], Rotor_E[19], Rotor_E[20],
                                        Rotor_E[21], Rotor_E[22], Rotor_E[23], Rotor_E[24], Rotor_E[25], Rotor_E[26], Rotor_E[27], Rotor_E[28], Rotor_E[29], Rotor_E[30],
                                        Rotor_E[31], Rotor_E[32], Rotor_E[33], Rotor_E[34], Rotor_E[35], Rotor_E[36], Rotor_E[37]]})
    
        if Letter_num >= 1:
            Rotor = Rotor_E_Ref.merge(Rotor_Output, how = 'left', on = 'Pos')  
        
            Convert = pd.DataFrame ({'Input': [Input_text_2[Letter_num - 1]]})
        
            Cypher_Letter = Convert.merge(Rotor, how = 'left', on = 'Input')
        
            Cypher_text = Cypher_text + Cypher_Letter.iloc[0]['Output']
        else:
            pass
        
        x = 1
        
        while x < 38:
            if Pos[x] + 1 == 38:
                Pos[x] = 1
            else:
                Pos[x] = Pos[x] + 1  
            
            x = x + 1
        
        Letter_num = Letter_num + 1

def Rotor_F_Encode():
    global Cypher_text
    Input_text_length = len(Input_text)
    Letter_num = Initial_Pos * -1

    Set_positions()    

    
    Cypher_text = ""
      
    while Letter_num <= Input_text_length:
        
        x = 1        
        
        Rotor_Output = pd.DataFrame ({'Pos':[Pos[1], Pos[2], Pos[3], Pos[4], Pos[5], Pos[6], Pos[7], Pos[8], Pos[9], Pos[10],
                                        Pos[11], Pos[12], Pos[13], Pos[14], Pos[15], Pos[16], Pos[17], Pos[18], Pos[19], Pos[20],
                                        Pos[21], Pos[22], Pos[23], Pos[24], Pos[25], Pos[26], Pos[27], Pos[28], Pos[29], Pos[30],
                                        Pos[31], Pos[32], Pos[33], Pos[34], Pos[35], Pos[36], Pos[37]],
                                      'Output':[Rotor_F[1], Rotor_F[2], Rotor_F[3], Rotor_F[4], Rotor_F[5], Rotor_F[6], Rotor_F[7], Rotor_F[8], Rotor_F[9], Rotor_F[10],
                                        Rotor_F[11], Rotor_F[12], Rotor_F[13], Rotor_F[14], Rotor_F[15], Rotor_F[16], Rotor_F[17], Rotor_F[18], Rotor_F[19], Rotor_F[20],
                                        Rotor_F[21], Rotor_F[22], Rotor_F[23], Rotor_F[24], Rotor_F[25], Rotor_F[26], Rotor_F[27], Rotor_F[28], Rotor_F[29], Rotor_F[30],
                                        Rotor_F[31], Rotor_F[32], Rotor_F[33], Rotor_F[34], Rotor_F[35], Rotor_F[36], Rotor_F[37]]})
    
        if Letter_num >= 1:
            Rotor = Rotor_F_Ref.merge(Rotor_Output, how = 'left', on = 'Pos')  
        
            Convert = pd.DataFrame ({'Input': [Input_text_2[Letter_num - 1]]})
        
            Cypher_Letter = Convert.merge(Rotor, how = 'left', on = 'Input')
        
            Cypher_text = Cypher_text + Cypher_Letter.iloc[0]['Output']
        else:
            pass
        
        x = 1
        
        while x < 38:
            if Pos[x] + 1 == 38:
                Pos[x] = 1
            else:
                Pos[x] = Pos[x] + 1  
            
            x = x + 1
        
        Letter_num = Letter_num + 1

def Rotor_G_Encode():
    global Cypher_text
    Input_text_length = len(Input_text)
    Letter_num = Initial_Pos * -1
    
    Set_positions()    

    
    Cypher_text = ""
      
    while Letter_num <= Input_text_length:
        
        x = 1        
        
        Rotor_Output = pd.DataFrame ({'Pos':[Pos[1], Pos[2], Pos[3], Pos[4], Pos[5], Pos[6], Pos[7], Pos[8], Pos[9], Pos[10],
                                        Pos[11], Pos[12], Pos[13], Pos[14], Pos[15], Pos[16], Pos[17], Pos[18], Pos[19], Pos[20],
                                        Pos[21], Pos[22], Pos[23], Pos[24], Pos[25], Pos[26], Pos[27], Pos[28], Pos[29], Pos[30],
                                        Pos[31], Pos[32], Pos[33], Pos[34], Pos[35], Pos[36], Pos[37]],
                                      'Output':[Rotor_G[1], Rotor_G[2], Rotor_G[3], Rotor_G[4], Rotor_G[5], Rotor_G[6], Rotor_G[7], Rotor_G[8], Rotor_G[9], Rotor_G[10],
                                        Rotor_G[11], Rotor_G[12], Rotor_G[13], Rotor_G[14], Rotor_G[15], Rotor_G[16], Rotor_G[17], Rotor_G[18], Rotor_G[19], Rotor_G[20],
                                        Rotor_G[21], Rotor_G[22], Rotor_G[23], Rotor_G[24], Rotor_G[25], Rotor_G[26], Rotor_G[27], Rotor_G[28], Rotor_G[29], Rotor_G[30],
                                        Rotor_G[31], Rotor_G[32], Rotor_G[33], Rotor_G[34], Rotor_G[35], Rotor_G[36], Rotor_G[37]]})
    
        if Letter_num >= 1:
            Rotor = Rotor_G_Ref.merge(Rotor_Output, how = 'left', on = 'Pos')  
        
            Convert = pd.DataFrame ({'Input': [Input_text_2[Letter_num - 1]]})
        
            Cypher_Letter = Convert.merge(Rotor, how = 'left', on = 'Input')
        
            Cypher_text = Cypher_text + Cypher_Letter.iloc[0]['Output']
        else:
            pass
        
        x = 1
        
        while x < 38:
            if Pos[x] + 1 == 38:
                Pos[x] = 1
            else:
                Pos[x] = Pos[x] + 1  
            
            x = x + 1
        
        Letter_num = Letter_num + 1

def Rotor_H_Encode():
    global Cypher_text
    Input_text_length = len(Input_text)
    Letter_num = Initial_Pos * -1
    
    Set_positions()    

        
    Cypher_text = ""
      
    while Letter_num <= Input_text_length:
        
        x = 1        
        
        Rotor_Output = pd.DataFrame ({'Pos':[Pos[1], Pos[2], Pos[3], Pos[4], Pos[5], Pos[6], Pos[7], Pos[8], Pos[9], Pos[10],
                                        Pos[11], Pos[12], Pos[13], Pos[14], Pos[15], Pos[16], Pos[17], Pos[18], Pos[19], Pos[20],
                                        Pos[21], Pos[22], Pos[23], Pos[24], Pos[25], Pos[26], Pos[27], Pos[28], Pos[29], Pos[30],
                                        Pos[31], Pos[32], Pos[33], Pos[34], Pos[35], Pos[36], Pos[37]],
                                      'Output':[Rotor_H[1], Rotor_H[2], Rotor_H[3], Rotor_H[4], Rotor_H[5], Rotor_H[6], Rotor_H[7], Rotor_H[8], Rotor_H[9], Rotor_H[10],
                                        Rotor_H[11], Rotor_H[12], Rotor_H[13], Rotor_H[14], Rotor_H[15], Rotor_H[16], Rotor_H[17], Rotor_H[18], Rotor_H[19], Rotor_H[20],
                                        Rotor_H[21], Rotor_H[22], Rotor_H[23], Rotor_H[24], Rotor_H[25], Rotor_H[26], Rotor_H[27], Rotor_H[28], Rotor_H[29], Rotor_H[30],
                                        Rotor_H[31], Rotor_H[32], Rotor_H[33], Rotor_H[34], Rotor_H[35], Rotor_H[36], Rotor_H[37]]})
    
        if Letter_num >= 1:
            Rotor = Rotor_H_Ref.merge(Rotor_Output, how = 'left', on = 'Pos')  
        
            Convert = pd.DataFrame ({'Input': [Input_text_2[Letter_num - 1]]})
        
            Cypher_Letter = Convert.merge(Rotor, how = 'left', on = 'Input')
        
            Cypher_text = Cypher_text + Cypher_Letter.iloc[0]['Output']
        else:
            pass
        
        x = 1
        
        while x < 38:
            if Pos[x] + 1 == 38:
                Pos[x] = 1
            else:
                Pos[x] = Pos[x] + 1  
            
            x = x + 1
        
        Letter_num = Letter_num + 1
        
#%% Decode text
def Rotor_A_Decode():

    Set_positions()    

    global Decoded_text
    Cypher_text_length = len(Cypher_text)
    Letter_num = Initial_Pos * -1
    
    Decoded_text = ""
   
    while Letter_num <= Cypher_text_length:

        Rotor_Output = pd.DataFrame ({'Pos':[Pos[1], Pos[2], Pos[3], Pos[4], Pos[5], Pos[6], Pos[7], Pos[8], Pos[9], Pos[10],
                                        Pos[11], Pos[12], Pos[13], Pos[14], Pos[15], Pos[16], Pos[17], Pos[18], Pos[19], Pos[20],
                                        Pos[21], Pos[22], Pos[23], Pos[24], Pos[25], Pos[26], Pos[27], Pos[28], Pos[29], Pos[30],
                                        Pos[31], Pos[32], Pos[33], Pos[34], Pos[35], Pos[36], Pos[37]],
                                      'Output':[Rotor_A[1], Rotor_A[2], Rotor_A[3], Rotor_A[4], Rotor_A[5], Rotor_A[6], Rotor_A[7], Rotor_A[8], Rotor_A[9], Rotor_A[10],
                                        Rotor_A[11], Rotor_A[12], Rotor_A[13], Rotor_A[14], Rotor_A[15], Rotor_A[16], Rotor_A[17], Rotor_A[18], Rotor_A[19], Rotor_A[20],
                                        Rotor_A[21], Rotor_A[22], Rotor_A[23], Rotor_A[24], Rotor_A[25], Rotor_A[26], Rotor_A[27], Rotor_A[28], Rotor_A[29], Rotor_A[30],
                                        Rotor_A[31], Rotor_A[32], Rotor_A[33], Rotor_A[34], Rotor_A[35], Rotor_A[36], Rotor_A[37]]})
        
        if Letter_num >= 1:
        
            Rotor = Rotor_A_Ref.merge(Rotor_Output, how = 'left', on = 'Pos')  
        
            Convert = pd.DataFrame ({'Input': [Cypher_text_2[Letter_num - 1]]})
        
            Decoded_Letter = Convert.merge(Rotor, how = 'left', on = 'Input')
        
            Decoded_text = Decoded_text + Decoded_Letter.iloc[0]['Output']
        else:
            pass
                           
        x = 1
        
        while x < 38:
            if Pos[x] - 1 == 0:
                Pos[x] = 37
            else:
                Pos[x] = Pos[x] - 1  
            x = x + 1            
        
        Letter_num = Letter_num + 1

def Rotor_B_Decode():
    global Decoded_text
    Cypher_text_length = len(Cypher_text)
    Letter_num = Initial_Pos * -1
    
    Set_positions()    
    
    
    Decoded_text = ""
    
    while Letter_num <= Cypher_text_length:
        
        x = 1
        
        Rotor_Output = pd.DataFrame ({'Pos':[Pos[1], Pos[2], Pos[3], Pos[4], Pos[5], Pos[6], Pos[7], Pos[8], Pos[9], Pos[10],
                                        Pos[11], Pos[12], Pos[13], Pos[14], Pos[15], Pos[16], Pos[17], Pos[18], Pos[19], Pos[20],
                                        Pos[21], Pos[22], Pos[23], Pos[24], Pos[25], Pos[26], Pos[27], Pos[28], Pos[29], Pos[30],
                                        Pos[31], Pos[32], Pos[33], Pos[34], Pos[35], Pos[36], Pos[37]],
                                      'Output':[Rotor_B[1], Rotor_B[2], Rotor_B[3], Rotor_B[4], Rotor_B[5], Rotor_B[6], Rotor_B[7], Rotor_B[8], Rotor_B[9], Rotor_B[10],
                                        Rotor_B[11], Rotor_B[12], Rotor_B[13], Rotor_B[14], Rotor_B[15], Rotor_B[16], Rotor_B[17], Rotor_B[18], Rotor_B[19], Rotor_B[20],
                                        Rotor_B[21], Rotor_B[22], Rotor_B[23], Rotor_B[24], Rotor_B[25], Rotor_B[26], Rotor_B[27], Rotor_B[28], Rotor_B[29], Rotor_B[30],
                                        Rotor_B[31], Rotor_B[32], Rotor_B[33], Rotor_B[34], Rotor_B[35], Rotor_B[36], Rotor_B[37]]})
    
        if Letter_num >= 1:
        
            Rotor = Rotor_B_Ref.merge(Rotor_Output, how = 'left', on = 'Pos')  
        
            Convert = pd.DataFrame ({'Input': [Cypher_text_2[Letter_num - 1]]})
        
            Decoded_Letter = Convert.merge(Rotor, how = 'left', on = 'Input')
        
            Decoded_text = Decoded_text + Decoded_Letter.iloc[0]['Output']
        else:
            pass
                           
        x = 1
        
        while x < 38:
            if Pos[x] - 1 == 0:
                Pos[x] = 37
            else:
                Pos[x] = Pos[x] - 1  
            x = x + 1            
        
        Letter_num = Letter_num + 1
    
def Rotor_C_Decode():
    global Decoded_text
    Cypher_text_length = len(Cypher_text)
    Letter_num = Initial_Pos * -1
    
    Set_positions()    
    
    
    Decoded_text = ""
    
    while Letter_num <= Cypher_text_length:
        
        x = 1
        
        Rotor_Output = pd.DataFrame ({'Pos':[Pos[1], Pos[2], Pos[3], Pos[4], Pos[5], Pos[6], Pos[7], Pos[8], Pos[9], Pos[10],
                                        Pos[11], Pos[12], Pos[13], Pos[14], Pos[15], Pos[16], Pos[17], Pos[18], Pos[19], Pos[20],
                                        Pos[21], Pos[22], Pos[23], Pos[24], Pos[25], Pos[26], Pos[27], Pos[28], Pos[29], Pos[30],
                                        Pos[31], Pos[32], Pos[33], Pos[34], Pos[35], Pos[36], Pos[37]],
                                      'Output':[Rotor_C[1], Rotor_C[2], Rotor_C[3], Rotor_C[4], Rotor_C[5], Rotor_C[6], Rotor_C[7], Rotor_C[8], Rotor_C[9], Rotor_C[10],
                                        Rotor_C[11], Rotor_C[12], Rotor_C[13], Rotor_C[14], Rotor_C[15], Rotor_C[16], Rotor_C[17], Rotor_C[18], Rotor_C[19], Rotor_C[20],
                                        Rotor_C[21], Rotor_C[22], Rotor_C[23], Rotor_C[24], Rotor_C[25], Rotor_C[26], Rotor_C[27], Rotor_C[28], Rotor_C[29], Rotor_C[30],
                                        Rotor_C[31], Rotor_C[32], Rotor_C[33], Rotor_C[34], Rotor_C[35], Rotor_C[36], Rotor_C[37]]})
    
        if Letter_num >= 1:
        
            Rotor = Rotor_C_Ref.merge(Rotor_Output, how = 'left', on = 'Pos')  
        
            Convert = pd.DataFrame ({'Input': [Cypher_text_2[Letter_num - 1]]})
        
            Decoded_Letter = Convert.merge(Rotor, how = 'left', on = 'Input')
        
            Decoded_text = Decoded_text + Decoded_Letter.iloc[0]['Output']
        else:
            pass
                           
        x = 1
        
        while x < 38:
            if Pos[x] - 1 == 0:
                Pos[x] = 37
            else:
                Pos[x] = Pos[x] - 1  
            x = x + 1            
        
        Letter_num = Letter_num + 1

def Rotor_D_Decode():
    global Decoded_text
    Cypher_text_length = len(Cypher_text)
    Letter_num = Initial_Pos * -1
    
    Set_positions()    
    
    
    Decoded_text = ""
    
    while Letter_num <= Cypher_text_length:
        
        x = 1
        
        Rotor_Output = pd.DataFrame ({'Pos':[Pos[1], Pos[2], Pos[3], Pos[4], Pos[5], Pos[6], Pos[7], Pos[8], Pos[9], Pos[10],
                                        Pos[11], Pos[12], Pos[13], Pos[14], Pos[15], Pos[16], Pos[17], Pos[18], Pos[19], Pos[20],
                                        Pos[21], Pos[22], Pos[23], Pos[24], Pos[25], Pos[26], Pos[27], Pos[28], Pos[29], Pos[30],
                                        Pos[31], Pos[32], Pos[33], Pos[34], Pos[35], Pos[36], Pos[37]],
                                      'Output':[Rotor_D[1], Rotor_D[2], Rotor_D[3], Rotor_D[4], Rotor_D[5], Rotor_D[6], Rotor_D[7], Rotor_D[8], Rotor_D[9], Rotor_D[10],
                                        Rotor_D[11], Rotor_D[12], Rotor_D[13], Rotor_D[14], Rotor_D[15], Rotor_D[16], Rotor_D[17], Rotor_D[18], Rotor_D[19], Rotor_D[20],
                                        Rotor_D[21], Rotor_D[22], Rotor_D[23], Rotor_D[24], Rotor_D[25], Rotor_D[26], Rotor_D[27], Rotor_D[28], Rotor_D[29], Rotor_D[30],
                                        Rotor_D[31], Rotor_D[32], Rotor_D[33], Rotor_D[34], Rotor_D[35], Rotor_D[36], Rotor_D[37]]})
    
        if Letter_num >= 1:
        
            Rotor = Rotor_D_Ref.merge(Rotor_Output, how = 'left', on = 'Pos')  
        
            Convert = pd.DataFrame ({'Input': [Cypher_text_2[Letter_num - 1]]})
        
            Decoded_Letter = Convert.merge(Rotor, how = 'left', on = 'Input')
        
            Decoded_text = Decoded_text + Decoded_Letter.iloc[0]['Output']
        else:
            pass
                           
        x = 1
        
        while x < 38:
            if Pos[x] - 1 == 0:
                Pos[x] = 37
            else:
                Pos[x] = Pos[x] - 1  
            x = x + 1            
        
        Letter_num = Letter_num + 1

def Rotor_E_Decode():
    global Decoded_text
    Cypher_text_length = len(Cypher_text)
    Letter_num = Initial_Pos * -1
    
    Set_positions()    
   
    
    Decoded_text = ""
    
    while Letter_num <= Cypher_text_length:
        
        x = 1
        
        Rotor_Output = pd.DataFrame ({'Pos':[Pos[1], Pos[2], Pos[3], Pos[4], Pos[5], Pos[6], Pos[7], Pos[8], Pos[9], Pos[10],
                                        Pos[11], Pos[12], Pos[13], Pos[14], Pos[15], Pos[16], Pos[17], Pos[18], Pos[19], Pos[20],
                                        Pos[21], Pos[22], Pos[23], Pos[24], Pos[25], Pos[26], Pos[27], Pos[28], Pos[29], Pos[30],
                                        Pos[31], Pos[32], Pos[33], Pos[34], Pos[35], Pos[36], Pos[37]],
                                      'Output':[Rotor_E[1], Rotor_E[2], Rotor_E[3], Rotor_E[4], Rotor_E[5], Rotor_E[6], Rotor_E[7], Rotor_E[8], Rotor_E[9], Rotor_E[10],
                                        Rotor_E[11], Rotor_E[12], Rotor_E[13], Rotor_E[14], Rotor_E[15], Rotor_E[16], Rotor_E[17], Rotor_E[18], Rotor_E[19], Rotor_E[20],
                                        Rotor_E[21], Rotor_E[22], Rotor_E[23], Rotor_E[24], Rotor_E[25], Rotor_E[26], Rotor_E[27], Rotor_E[28], Rotor_E[29], Rotor_E[30],
                                        Rotor_E[31], Rotor_E[32], Rotor_E[33], Rotor_E[34], Rotor_E[35], Rotor_E[36], Rotor_E[37]]})
    
        if Letter_num >= 1:
        
            Rotor = Rotor_E_Ref.merge(Rotor_Output, how = 'left', on = 'Pos')  
        
            Convert = pd.DataFrame ({'Input': [Cypher_text_2[Letter_num - 1]]})
        
            Decoded_Letter = Convert.merge(Rotor, how = 'left', on = 'Input')
        
            Decoded_text = Decoded_text + Decoded_Letter.iloc[0]['Output']
        else:
            pass
                           
        x = 1
        
        while x < 38:
            if Pos[x] - 1 == 0:
                Pos[x] = 37
            else:
                Pos[x] = Pos[x] - 1  
            x = x + 1            
        
        Letter_num = Letter_num + 1

def Rotor_F_Decode():
    global Decoded_text
    Cypher_text_length = len(Cypher_text)
    Letter_num = Initial_Pos * -1
    
    Set_positions()    
  
    
    Decoded_text = ""
    
    while Letter_num <= Cypher_text_length:
        
        x = 1
        
        Rotor_Output = pd.DataFrame ({'Pos':[Pos[1], Pos[2], Pos[3], Pos[4], Pos[5], Pos[6], Pos[7], Pos[8], Pos[9], Pos[10],
                                        Pos[11], Pos[12], Pos[13], Pos[14], Pos[15], Pos[16], Pos[17], Pos[18], Pos[19], Pos[20],
                                        Pos[21], Pos[22], Pos[23], Pos[24], Pos[25], Pos[26], Pos[27], Pos[28], Pos[29], Pos[30],
                                        Pos[31], Pos[32], Pos[33], Pos[34], Pos[35], Pos[36], Pos[37]],
                                      'Output':[Rotor_F[1], Rotor_F[2], Rotor_F[3], Rotor_F[4], Rotor_F[5], Rotor_F[6], Rotor_F[7], Rotor_F[8], Rotor_F[9], Rotor_F[10],
                                        Rotor_F[11], Rotor_F[12], Rotor_F[13], Rotor_F[14], Rotor_F[15], Rotor_F[16], Rotor_F[17], Rotor_F[18], Rotor_F[19], Rotor_F[20],
                                        Rotor_F[21], Rotor_F[22], Rotor_F[23], Rotor_F[24], Rotor_F[25], Rotor_F[26], Rotor_F[27], Rotor_F[28], Rotor_F[29], Rotor_F[30],
                                        Rotor_F[31], Rotor_F[32], Rotor_F[33], Rotor_F[34], Rotor_F[35], Rotor_F[36], Rotor_F[37]]})
    
        if Letter_num >= 1:
        
            Rotor = Rotor_F_Ref.merge(Rotor_Output, how = 'left', on = 'Pos')  
        
            Convert = pd.DataFrame ({'Input': [Cypher_text_2[Letter_num - 1]]})
        
            Decoded_Letter = Convert.merge(Rotor, how = 'left', on = 'Input')
        
            Decoded_text = Decoded_text + Decoded_Letter.iloc[0]['Output']
        else:
            pass
                           
        x = 1
        
        while x < 38:
            if Pos[x] - 1 == 0:
                Pos[x] = 37
            else:
                Pos[x] = Pos[x] - 1  
            x = x + 1            
        
        Letter_num = Letter_num + 1

def Rotor_G_Decode():
    global Decoded_text
    Cypher_text_length = len(Cypher_text)
    Letter_num = Initial_Pos * -1
    
    Set_positions()    
   
    
    Decoded_text = ""
    
    while Letter_num <= Cypher_text_length:
        
        x = 1
        
        Rotor_Output = pd.DataFrame ({'Pos':[Pos[1], Pos[2], Pos[3], Pos[4], Pos[5], Pos[6], Pos[7], Pos[8], Pos[9], Pos[10],
                                        Pos[11], Pos[12], Pos[13], Pos[14], Pos[15], Pos[16], Pos[17], Pos[18], Pos[19], Pos[20],
                                        Pos[21], Pos[22], Pos[23], Pos[24], Pos[25], Pos[26], Pos[27], Pos[28], Pos[29], Pos[30],
                                        Pos[31], Pos[32], Pos[33], Pos[34], Pos[35], Pos[36], Pos[37]],
                                      'Output':[Rotor_G[1], Rotor_G[2], Rotor_G[3], Rotor_G[4], Rotor_G[5], Rotor_G[6], Rotor_G[7], Rotor_G[8], Rotor_G[9], Rotor_G[10],
                                        Rotor_G[11], Rotor_G[12], Rotor_G[13], Rotor_G[14], Rotor_G[15], Rotor_G[16], Rotor_G[17], Rotor_G[18], Rotor_G[19], Rotor_G[20],
                                        Rotor_G[21], Rotor_G[22], Rotor_G[23], Rotor_G[24], Rotor_G[25], Rotor_G[26], Rotor_G[27], Rotor_G[28], Rotor_G[29], Rotor_G[30],
                                        Rotor_G[31], Rotor_G[32], Rotor_G[33], Rotor_G[34], Rotor_G[35], Rotor_G[36], Rotor_G[37]]})
    
        if Letter_num >= 1:
        
            Rotor = Rotor_G_Ref.merge(Rotor_Output, how = 'left', on = 'Pos')  
        
            Convert = pd.DataFrame ({'Input': [Cypher_text_2[Letter_num - 1]]})
        
            Decoded_Letter = Convert.merge(Rotor, how = 'left', on = 'Input')
        
            Decoded_text = Decoded_text + Decoded_Letter.iloc[0]['Output']
        else:
            pass
                           
        x = 1
        
        while x < 38:
            if Pos[x] - 1 == 0:
                Pos[x] = 37
            else:
                Pos[x] = Pos[x] - 1  
            x = x + 1            
        
        Letter_num = Letter_num + 1

def Rotor_H_Decode():
    global Decoded_text
    Cypher_text_length = len(Cypher_text)
    Letter_num = Initial_Pos * -1
    
    Set_positions()    
 
    Decoded_text = ""
    
    while Letter_num <= Cypher_text_length:
        
        x = 1
        
        Rotor_Output = pd.DataFrame ({'Pos':[Pos[1], Pos[2], Pos[3], Pos[4], Pos[5], Pos[6], Pos[7], Pos[8], Pos[9], Pos[10],
                                        Pos[11], Pos[12], Pos[13], Pos[14], Pos[15], Pos[16], Pos[17], Pos[18], Pos[19], Pos[20],
                                        Pos[21], Pos[22], Pos[23], Pos[24], Pos[25], Pos[26], Pos[27], Pos[28], Pos[29], Pos[30],
                                        Pos[31], Pos[32], Pos[33], Pos[34], Pos[35], Pos[36], Pos[37]],
                                      'Output':[Rotor_H[1], Rotor_H[2], Rotor_H[3], Rotor_H[4], Rotor_H[5], Rotor_H[6], Rotor_H[7], Rotor_H[8], Rotor_H[9], Rotor_H[10],
                                        Rotor_H[11], Rotor_H[12], Rotor_H[13], Rotor_H[14], Rotor_H[15], Rotor_H[16], Rotor_H[17], Rotor_H[18], Rotor_H[19], Rotor_H[20],
                                        Rotor_H[21], Rotor_H[22], Rotor_H[23], Rotor_H[24], Rotor_H[25], Rotor_H[26], Rotor_H[27], Rotor_H[28], Rotor_H[29], Rotor_H[30],
                                        Rotor_H[31], Rotor_H[32], Rotor_H[33], Rotor_H[34], Rotor_H[35], Rotor_H[36], Rotor_H[37]]})
    
        if Letter_num >= 1:
        
            Rotor = Rotor_H_Ref.merge(Rotor_Output, how = 'left', on = 'Pos')  
        
            Convert = pd.DataFrame ({'Input': [Cypher_text_2[Letter_num - 1]]})
        
            Decoded_Letter = Convert.merge(Rotor, how = 'left', on = 'Input')
        
            Decoded_text = Decoded_text + Decoded_Letter.iloc[0]['Output']
        else:
            pass
                           
        x = 1
        
        while x < 38:
            if Pos[x] - 1 == 0:
                Pos[x] = 37
            else:
                Pos[x] = Pos[x] - 1  
            x = x + 1            
        
        Letter_num = Letter_num + 1

#%% Encode Text    
        
Define_rotors()
Input_text = ''
Input_text = input('Enter text to be encoded: ')

if Input_text == "":
    Input_text = 'Trial text'
else:
    pass

Input_text = Input_text.upper()
Input_text_2 = Input_text

#Rotor 1
Initial_Pos = 5
Rotor_A_Encode()
Input_text_2 = Cypher_text

#Rotor 2
Initial_Pos = 9
Rotor_B_Encode()
Input_text_2 = Cypher_text

#Rotor 3
Initial_Pos = 10
Rotor_C_Encode()
Input_text_2 = Cypher_text

#Rotor 4
Initial_Pos = 50
Rotor_D_Encode()
Input_text_2 = Cypher_text

#Rotor 5
Initial_Pos = 10
Rotor_E_Encode()
Input_text_2 = Cypher_text

#Rotor 6
Initial_Pos = 40
Rotor_F_Encode()
Input_text_2 = Cypher_text

#Rotor 7
Initial_Pos = 30
Rotor_G_Encode()
Input_text_2 = Cypher_text

#Rotor 8
Initial_Pos = 1
Rotor_H_Encode()
Input_text_2 = Cypher_text

print('Cypher text: ' + Cypher_text)

#%% Decode Text
Define_rotors()
Cypher_text_3 = input('Enter text to be decoded: ')

if Cypher_text_3 == "":
    Cypher_text = Cypher_text
else:
    Cypher_text = Cypher_text_3

Cypher_text_2 = Cypher_text

#Rotor 8
Initial_Pos = 1
Rotor_H_Decode()
Cypher_text_2 = Decoded_text

#Rotor 7
Initial_Pos = 30
Rotor_G_Decode()
Cypher_text_2 = Decoded_text

#Rotor 6
Initial_Pos = 40
Rotor_F_Decode()
Cypher_text_2 = Decoded_text

#Rotor 5
Initial_Pos = 10
Rotor_E_Decode()
Cypher_text_2 = Decoded_text

#Rotor 4
Initial_Pos = 50
Rotor_D_Decode()
Cypher_text_2 = Decoded_text

#Rotor 3
Initial_Pos = 10
Rotor_C_Decode()
Cypher_text_2 = Decoded_text

#Rotor 2
Initial_Pos = 9
Rotor_B_Decode()
Cypher_text_2 = Decoded_text

#Rotor 1
Initial_Pos = 5
Rotor_A_Decode()
Cypher_text_2 = Decoded_text

print('Decoded text: ' + Decoded_text)
