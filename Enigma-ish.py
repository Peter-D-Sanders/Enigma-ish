"""
SCRIPT NAME:
    Enigma-ish.py

DESCRIPTION:
    Turns plain text to cypher text and vice-versa again.

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
15/05/2022    v2.3        Pete Sanders   More code improvements.
16/05/2022    v3.0        Pete Sanders   Made as a .exe and added some front end.
19/05/2022    v3.1        Pete Sanders   Allowed the use of any number of rotors.
16/07/2022    v3.2        Pete Sanders   Made some efficiencty changes.
16/07/2022    v3.3        Pete Sanders   Bug fix.
21/07/2022    v3.4        Pete Sanders   Added functionality to rotate rotors better.
                                         Changed 'decode' to 'decypher'
        
RECOMMENDED FUTURE IMPROVEMENTS:
    Include a reflector and pinboard to properly model enigma.
    Allow the use of additional characters.
    Figure out how to make faster.
    Include a random character generator to hide the length of the input text.
        
Bugs:
    
"""

#%% Import modules
import pandas as pd
import time
import tkinter as tk

#%% Front end stuff
global RP
global IT
global OT
global var1
global ROIP
global IN
global OUT
global ROT
    
# Assignes some function within tk to root
root = tk.Tk()
root.title('Enigma-ish v3.4')

# Sets up the encode/decode message logic
def print_selection():
    if var1.get() == 1:
        l.config(text= 'Decypher')
    elif var1.get() == 0:
        l.config(text='Encode')


# Create text widget and specify size.
ROT = tk.Text(root, height = 5, width = 52)
 
# Create label
lROT = tk.Label(root, text = "Rotor settings")
lROT.config(font =("Courier", 14))
ROT.insert(tk.END, 'A,5,B,9,C,10,D,50,E,10,F,40,G,30,H,1')
lROT.pack()
ROT.pack()

# Create text widget and specify size.
IN = tk.Text(root, height = 5, width = 52)
 
# Create label
lIN = tk.Label(root, text = "Input text")
lIN.config(font =("Courier", 14))
IN.insert(tk.END, 'Type or copy paste the text to be converted here')
lIN.pack()
IN.pack()

# Create text widget and specify size.
OUT = tk.Text(root, height = 5, width = 52)
 
# Create label
lOUT = tk.Label(root, text = "Output text")
lOUT.config(font =("Courier", 14))
OUT.insert(tk.END, 'Converted text will be displayed here')
lOUT.pack()
OUT.pack()

# Sets up a message label
l = tk.Label(root, bg='white', text = 'Encode')
l.pack()

# sets up a tick box
var1 = tk.IntVar()
c1 = tk.Checkbutton(root, text='Decypher', variable = var1, onvalue=1, offvalue=0, command = print_selection)
c1.pack()

IT = IN.get(1.0, "end-1c")
OT = OUT.get(1.0, "end-1c")
RP = ROT.get(1.0, "end-1c")

# Define Input_text, Cypher_text, and ROIP.
Input_text = ''
Cypher_text = ''
ROIP = ''
Rotor_num = 0

#%% Instructions
# Print instrustions
print ('Instructions:', '\n',
       'Before entering any text, you will have to "set the rotors":', '\n',
       '    - To do this enter the rotor letters and initial positions in the "Rotor settings" box,', '\n',
       '    - A rotor must be entered as rotor letter and initial postion pairs, seperated by commas,', '\n',
       '    - Any number of rotors can be used,', '\n',
       '    - Rotor letters must be capitals between A and H incl.,', '\n',
       '    - A rotor letter may be used more than once,', '\n',
       '    - Initial positions can be any integer.','\n',
       'Enter the text to be converted in the "Input text" box', '\n',
       'If this is cypher text also check the "Decypher" box', '\n',
       'Press "Encode/Decypher"', '\n',
       'Converted text will be displayed in the "Output text" box', '\n',)

#%% Set rotor positions
def Set_positions():    
    global Pos

    #This dictionary sets the rotor values and allows the positions of the Rotor_Outputs to be changed    
    Pos = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37]

#%% Convert text
def Convert_text():
    global Cypher_text
    global Input_text
    
    # Convert odd values of input text to something usefull
    Replace = {'\n':' ','!':'','@': 'AT','#':'','$':'','%':'','^':'','&':'','*':'',
               '(':'',')':'','_':'','.':' STOP','?':'',',':'','/':'','|':'','[':'',
               ']':'','{':'','}':'','<':'','>':'',':':'',';':'','':'','':'','':'','':'',
               '':'','':'','':'','':'','':'','':'','':'','':'','':'','':'','':''}
    for key, value in Replace.items():
        Input_text = Input_text.replace(key, value)
        Cypher_text = Cypher_text.replace(key, value)
    
#%% Define Rotors
def Define_rotors():
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

#%% Encode
def Encode():
    global Rotor_X
    global Cypher_text
    global Rotor_Input_2
    global Initial_Pos
    global Rotor_num

    # Resets the rotor position
    Set_positions() 
    
    Letter_num = 0
    
    x = Initial_Pos
    
    
    # Resets the cypher text so  that anything being encoded will be the new cypher text
    Cypher_text = ""
    
    Rotor_Output = pd.DataFrame ({'Pos':[Pos[((0 + x) % 37)], Pos[((1 + x) % 37)], Pos[((2 + x) % 37)], Pos[((3 + x) % 37)], Pos[((4 + x) % 37)],
                                         Pos[((5 + x) % 37)], Pos[((6 + x) % 37)], Pos[((7 + x) % 37)], Pos[((8 + x) % 37)], Pos[((9 + x) % 37)],
                                         Pos[((10 + x) % 37)], Pos[((11 + x) % 37)], Pos[((12 + x) % 37)], Pos[((13 + x) % 37)], Pos[((14 + x) % 37)],
                                         Pos[((15 + x) % 37)], Pos[((16 + x) % 37)], Pos[((17 + x) % 37)], Pos[((18 + x) % 37)], Pos[((19 + x) % 37)],
                                         Pos[((20 + x) % 37)], Pos[((21 + x) % 37)], Pos[((22 + x) % 37)], Pos[((23 + x) % 37)], Pos[((24 + x) % 37)],
                                         Pos[((25 + x) % 37)], Pos[((26 + x) % 37)], Pos[((27 + x) % 37)], Pos[((28 + x) % 37)], Pos[((29 + x) % 37)],
                                         Pos[((30 + x) % 37)], Pos[((31 + x) % 37)], Pos[((32 + x) % 37)], Pos[((33 + x) % 37)], Pos[((34 + x) % 37)],
                                         Pos[((35 + x) % 37)], Pos[((36 + x) % 37)]],
                                   'Output':[Rotor_Input_2[Rotor_X].loc[0], Rotor_Input_2[Rotor_X].loc[1], Rotor_Input_2[Rotor_X].loc[2], Rotor_Input_2[Rotor_X].loc[3], Rotor_Input_2[Rotor_X].loc[4], Rotor_Input_2[Rotor_X].loc[5], Rotor_Input_2[Rotor_X].loc[6], Rotor_Input_2[Rotor_X].loc[7], Rotor_Input_2[Rotor_X].loc[8], Rotor_Input_2[Rotor_X].loc[9],
                                             Rotor_Input_2[Rotor_X].loc[10], Rotor_Input_2[Rotor_X].loc[11], Rotor_Input_2[Rotor_X].loc[12], Rotor_Input_2[Rotor_X].loc[13], Rotor_Input_2[Rotor_X].loc[14], Rotor_Input_2[Rotor_X].loc[15], Rotor_Input_2[Rotor_X].loc[16], Rotor_Input_2[Rotor_X].loc[17], Rotor_Input_2[Rotor_X].loc[18], Rotor_Input_2[Rotor_X].loc[19],
                                             Rotor_Input_2[Rotor_X].loc[20], Rotor_Input_2[Rotor_X].loc[21], Rotor_Input_2[Rotor_X].loc[22], Rotor_Input_2[Rotor_X].loc[23], Rotor_Input_2[Rotor_X].loc[24], Rotor_Input_2[Rotor_X].loc[25], Rotor_Input_2[Rotor_X].loc[26], Rotor_Input_2[Rotor_X].loc[27], Rotor_Input_2[Rotor_X].loc[28], Rotor_Input_2[Rotor_X].loc[29],
                                             Rotor_Input_2[Rotor_X].loc[30], Rotor_Input_2[Rotor_X].loc[31], Rotor_Input_2[Rotor_X].loc[32], Rotor_Input_2[Rotor_X].loc[33], Rotor_Input_2[Rotor_X].loc[34], Rotor_Input_2[Rotor_X].loc[35], Rotor_Input_2[Rotor_X].loc[36]]})
    
    for i in Input_text:      
        # Shifts the Pos value by the initial rotor position
        # Shifts the "Pos" value by 1 (or loops round) which has the effect of moving the 
        # Output column of the Rotor df up by one position but leaving the Input column in place 
        # ((0 + x) % 37) + 1 = take the dictionary ref (0) add the initial position and then add 1
        Rotor_Output['Pos'] = [Pos[((0 + x) % 37)], Pos[((1 + x) % 37)], Pos[((2 + x) % 37)], Pos[((3 + x) % 37)], Pos[((4 + x) % 37)],
                               Pos[((5 + x) % 37)], Pos[((6 + x) % 37)], Pos[((7 + x) % 37)], Pos[((8 + x) % 37)], Pos[((9 + x) % 37)],
                               Pos[((10 + x) % 37)], Pos[((11 + x) % 37)], Pos[((12 + x) % 37)], Pos[((13 + x) % 37)], Pos[((14 + x) % 37)],
                               Pos[((15 + x) % 37)], Pos[((16 + x) % 37)], Pos[((17 + x) % 37)], Pos[((18 + x) % 37)], Pos[((19 + x) % 37)],
                               Pos[((20 + x) % 37)], Pos[((21 + x) % 37)], Pos[((22 + x) % 37)], Pos[((23 + x) % 37)], Pos[((24 + x) % 37)],
                               Pos[((25 + x) % 37)], Pos[((26 + x) % 37)], Pos[((27 + x) % 37)], Pos[((28 + x) % 37)], Pos[((29 + x) % 37)],
                               Pos[((30 + x) % 37)], Pos[((31 + x) % 37)], Pos[((32 + x) % 37)], Pos[((33 + x) % 37)], Pos[((34 + x) % 37)],
                               Pos[((35 + x) % 37)], Pos[((36 + x) % 37)]]
       
        # If statement ensures encoding 'starts' after the rotor positions have been set.
        # i.e. after the blanks before the start of the text have been encoded.
        if Letter_num >= 1:
            # Merges the 'Rotor_Output' (moving) and 'Rotor_Ref' (fixed) dfs by their positional values  
            Rotor_Input_2 = Rotor_Input_2.merge(Rotor_Output, how = 'left', on = 'Pos')  
            
            # Identifies the letter to be converted 
            Convert = Input_text_2[Letter_num - 1]

            # Gets the index of the position of the letter to be converted in the Rotor df 
            
            Cypher_Letter_Index = int(Rotor_Input_2.index[Rotor_Input_2[Rotor_X] == Convert].tolist()[0])

            # Returns the 'Output' from the Rotor df i.e. the converted letter        
            Cypher_Letter = Rotor_Input_2.loc[Cypher_Letter_Index,'Output'] 

            # Creates a string that concatenates all of the converted letters        
            Cypher_text = Cypher_text + Cypher_Letter    
            
            # Drops the 'output' column ready for the next loop
            Rotor_Input_2 = Rotor_Input_2.drop(columns = ['Output'])            
        else:
            pass
        
        # Move the rotor position one space, for Rotor n this is carried out every n*26th letter.
        if Rotor_num == 0:
            x = x + 1
        elif int(int(Letter_num) % int(26 * Rotor_num)) == 0:
            x = x + 1
        else:
            pass
        
        # Move to the next letter in the text to be encoded
        Letter_num = Letter_num + 1
               
#%% Decode
def Decode():
    global Initial_Pos
    global Decoded_text
    global Rotor_X
    global Rotor_Input_2
    global Rotor_num
    
    Set_positions()  
    
    Letter_num = 0
    
    x = Initial_Pos    
    
    Decoded_text = ""
    
    Rotor_Output = pd.DataFrame ({'Pos':[Pos[((0 - x) % 37)], Pos[((1 - x) % 37)], Pos[((2 - x) % 37)], Pos[((3 - x) % 37)], Pos[((4 - x) % 37)],
                                         Pos[((5 - x) % 37)], Pos[((6 - x) % 37)], Pos[((7 - x) % 37)], Pos[((8 - x) % 37)], Pos[((9 - x) % 37)],
                                         Pos[((10 - x) % 37)], Pos[((11 - x) % 37)], Pos[((12 - x) % 37)], Pos[((13 - x) % 37)], Pos[((14 - x) % 37)],
                                         Pos[((15 - x) % 37)], Pos[((16 - x) % 37)], Pos[((17 - x) % 37)], Pos[((18 - x) % 37)], Pos[((19 - x) % 37)],
                                         Pos[((20 - x) % 37)], Pos[((21 - x) % 37)], Pos[((22 - x) % 37)], Pos[((23 - x) % 37)], Pos[((24 - x) % 37)],
                                         Pos[((25 - x) % 37)], Pos[((26 - x) % 37)], Pos[((27 - x) % 37)], Pos[((28 - x) % 37)], Pos[((29 - x) % 37)],
                                         Pos[((30 - x) % 37)], Pos[((31 - x) % 37)], Pos[((32 - x) % 37)], Pos[((33 - x) % 37)], Pos[((34 - x) % 37)],
                                         Pos[((35 - x) % 37)], Pos[((36 - x) % 37)]],
                                   'Output':[Rotor_Input_2[Rotor_X].loc[0], Rotor_Input_2[Rotor_X].loc[1], Rotor_Input_2[Rotor_X].loc[2], Rotor_Input_2[Rotor_X].loc[3], Rotor_Input_2[Rotor_X].loc[4], Rotor_Input_2[Rotor_X].loc[5], Rotor_Input_2[Rotor_X].loc[6], Rotor_Input_2[Rotor_X].loc[7], Rotor_Input_2[Rotor_X].loc[8], Rotor_Input_2[Rotor_X].loc[9],
                                             Rotor_Input_2[Rotor_X].loc[10], Rotor_Input_2[Rotor_X].loc[11], Rotor_Input_2[Rotor_X].loc[12], Rotor_Input_2[Rotor_X].loc[13], Rotor_Input_2[Rotor_X].loc[14], Rotor_Input_2[Rotor_X].loc[15], Rotor_Input_2[Rotor_X].loc[16], Rotor_Input_2[Rotor_X].loc[17], Rotor_Input_2[Rotor_X].loc[18], Rotor_Input_2[Rotor_X].loc[19],
                                             Rotor_Input_2[Rotor_X].loc[20], Rotor_Input_2[Rotor_X].loc[21], Rotor_Input_2[Rotor_X].loc[22], Rotor_Input_2[Rotor_X].loc[23], Rotor_Input_2[Rotor_X].loc[24], Rotor_Input_2[Rotor_X].loc[25], Rotor_Input_2[Rotor_X].loc[26], Rotor_Input_2[Rotor_X].loc[27], Rotor_Input_2[Rotor_X].loc[28], Rotor_Input_2[Rotor_X].loc[29],
                                             Rotor_Input_2[Rotor_X].loc[30], Rotor_Input_2[Rotor_X].loc[31], Rotor_Input_2[Rotor_X].loc[32], Rotor_Input_2[Rotor_X].loc[33], Rotor_Input_2[Rotor_X].loc[34], Rotor_Input_2[Rotor_X].loc[35], Rotor_Input_2[Rotor_X].loc[36]]})

    for i in Cypher_text:  
        Rotor_Output['Pos'] = [Pos[((0 - x) % 37)], Pos[((1 - x) % 37)], Pos[((2 - x) % 37)], Pos[((3 - x) % 37)], Pos[((4 - x) % 37)],
                               Pos[((5 - x) % 37)], Pos[((6 - x) % 37)], Pos[((7 - x) % 37)], Pos[((8 - x) % 37)], Pos[((9 - x) % 37)],
                               Pos[((10 - x) % 37)], Pos[((11 - x) % 37)], Pos[((12 - x) % 37)], Pos[((13 - x) % 37)], Pos[((14 - x) % 37)],
                               Pos[((15 - x) % 37)], Pos[((16 - x) % 37)], Pos[((17 - x) % 37)], Pos[((18 - x) % 37)], Pos[((19 - x) % 37)],
                               Pos[((20 - x) % 37)], Pos[((21 - x) % 37)], Pos[((22 - x) % 37)], Pos[((23 - x) % 37)], Pos[((24 - x) % 37)],
                               Pos[((25 - x) % 37)], Pos[((26 - x) % 37)], Pos[((27 - x) % 37)], Pos[((28 - x) % 37)], Pos[((29 - x) % 37)],
                               Pos[((30 - x) % 37)], Pos[((31 - x) % 37)], Pos[((32 - x) % 37)], Pos[((33 - x) % 37)], Pos[((34 - x) % 37)],
                               Pos[((35 - x) % 37)], Pos[((36 - x) % 37)]]     
     
        if Letter_num >= 1:
            Rotor_Input_2 = Rotor_Input_2.merge(Rotor_Output, how = 'left', on = 'Pos') 
            
            Convert = Cypher_text_2[Letter_num - 1]
                   
            Decoded_letter_index = int(Rotor_Input_2.index[Rotor_Input_2[Rotor_X] == Convert].tolist()[0])
            
            Decoded_Letter = Rotor_Input_2.loc[Decoded_letter_index,'Output']   
    
            Decoded_text = Decoded_text + Decoded_Letter
            
            Rotor_Input_2 = Rotor_Input_2.drop(columns = ['Output'])   
        else:
            pass
        
        if Rotor_num == 0:
            x = x + 1
        elif int(Letter_num) % int(26 * Rotor_num) == 0:
                x = x + 1
        else:
            pass           
        
        Letter_num = Letter_num + 1
            
#%% Encode Text
def Encode_text():
    global Input_text
    global Input_text_2
    global Initial_Pos
    global ROIP
    global Rotor_num
        
    Input_text = str(IT) + "1"
    
    Input_text = Input_text.upper()
    
    Convert_text()
    Define_rotors()
    
    Input_text_2 = Input_text

    Encode_start = time.time()
    
    a = 0
    b = int(len(ROIP)) - 2
    Rotor_num = 0

    while a <= b:
        Initial_Pos = int(ROIP[a + 1])
        globals()['Rotor_X'] = 'Rotor_' + ROIP[a]
        Encode()
        Input_text_2 = Cypher_text
        Rotor_num = Rotor_num + 1
        a = a + 2
        
    Encode_end = time.time()
    
    OT = Cypher_text
    OUT.replace("1.0", tk.END, OUT.get("1.0", tk.END).replace(OUT.get("1.0", tk.END),str(OT)))
    
    print("------------------------------")
    print("Input text = " + IT)
    print("Cypher text = " + OT)
    print("Text length = %s characters" % (len(Cypher_text)))
    print("Encode time = %s sec" % (Encode_end - Encode_start))

#%% Decode Text
def Decode_text():
    global Cypher_text
    global Cypher_text_2
    global Initial_Pos
    global ROIP
    global Rotor_num

    Cypher_text = str(IT) + "1"
    
    Cypher_text = Cypher_text.upper()
    
    Convert_text()
    Define_rotors()
    
    Cypher_text_2 = Cypher_text
    
    Decode_start = time.time()
    
    a = int(len(ROIP))
    b = 2
    Rotor_num = (a / 2) - 1

    while a >= b:
        Initial_Pos = int(ROIP[a - 1])
        globals()['Rotor_X'] = 'Rotor_' + ROIP[a - 2]
        Decode()
        Cypher_text_2 = Decoded_text

        a = a - 2
        
        Rotor_num = Rotor_num - 1
    
    Decode_end = time.time()
    
    OT = Decoded_text
    OUT.replace("1.0", tk.END, OUT.get("1.0", tk.END).replace(OUT.get("1.0", tk.END),str(OT)))
    
    print("------------------------------")
    print("Cypher text = " + IT)
    print("Decyphered text = " + OT)
    print("Text length = %s characters" % (len(Decoded_text)))
    print("Decypher time = %s sec" % (Decode_end - Decode_start))

#%% The big red button
   
# The function called by a button click
def GO():
    global RP
    global IT
    global var1
    global ROT
    global ROIP
    global IN
    
    IT = IN.get(1.0, "end-1c")
    RP = ROT.get(1.0, "end-1c")
    ROIP = list(RP.split(','))
    
    if var1.get() == 0:
        Encode_text()
    elif var1.get() == 1:
        Decode_text()
                
# Describes the button and what function it runs    
button1 = tk.Button(root, text = 'Encode/Decypher' ,command = GO, bg='brown',fg='white')
button1.pack()

root.mainloop()
