import time
#import winsound                                        # LINUX LIMITATION (WINDOWS ONLY)




dot_len = 100
dash_len = dot_len * 3
elm_len = dot_len
word_pause = dot_len * 7




#note = 800                                             #Frequency (WINDOWS ONLY)




def dot():
    print('.')
    #winsound.beep(note,dot_len)                        # LINUX LIMITATION (WINDOWS ONLY)
    time.sleep(1)




def dash():
    print('-')
    #winsound.beep(note,dash_len)                       # LINUX LIMITATION (WINDOWS ONLY)
    time.sleep(1)




def el_pause():
    print(""" 
    *ELEMENT PAUSE*
    """)
    time.sleep(2)




def word_pause():
    print("""

    
    ***WORD PAUSE***
    

    """)




def text_pause():
    time.sleep(0.5)




def text_to_morse(message):
    for i in message:
        if i == 'a' or i == 'A': # A
            dot()
            dash()
            el_pause()




        elif i == 'b' or i == 'B': # B
            dash()
            dot()
            dot()
            dot()
            el_pause()



        
        elif i == 'c' or i == 'C': # C
            dash()
            dot()
            dash()
            dot()
            el_pause()




        elif i == 'd' or i == 'D': # D
            dash()
            dash()
            dot()
            el_pause()




        elif i == 'e' or i == 'E': # E
            dot()
            el_pause()




        elif i == 'f' or i == 'F': # F
            dot()
            dot()
            dash()
            dot()
            el_pause()




        elif i == 'g' or i == 'G': # G 
            dash()
            dash()
            dot()
            el_pause()




        elif i == 'h' or i == 'H': # H
            dot()
            dot()
            dot()
            dot()
            el_pause()




        elif i == 'i' or i == 'I': # I
            dot()
            dot()
            el_pause()




        elif i == 'j' or i == 'J': # J
            dot()
            dash()
            dash()
            dash()
            el_pause()




        elif i == 'k' or i == 'K': # K 
            dash()
            dot()
            dash()
            el_pause()




        elif i == 'l' or i == 'L': # L
            dot()
            dash()
            dot()
            dot()
            el_pause()




        elif i == 'm' or i == 'M': # M
            dash()
            dash()
            el_pause()




        elif i == 'n' or i == 'N': # N
            dash()
            dot()
            el_pause()




        elif i == 'o' or i == 'O': # O
            dash()
            dash()
            dash()
            el_pause()




        elif i == 'p' or i == 'P': # P
            dot()
            dash()
            dash()
            dot()
            el_pause()




        elif i == 'q' or i == 'Q': # Q
            dash()
            dash()
            dot()
            dash()
            el_pause()




        elif i == 'r' or i == 'R': # R
            dot()
            dash()
            dot()
            el_pause()




        elif i == 's' or i == 'S': # S
            dot()
            dot()
            dot()
            el_pause()




        elif i == 't' or i == 'T': # T
            dash()
            el_pause()




        elif i == 'u' or i == 'U': # U
            dot()
            dot()
            dash()
            el_pause()




        elif i == 'v' or i == 'V': # V
            dot()
            dot()
            dot()
            dash()
            el_pause()




        elif i == 'w' or i == 'W': # W
            dot()
            dash()
            dash()
            el_pause()




        elif i == 'x' or i == 'X': # X
            dash()
            dot()
            dot()
            dash()
            el_pause()




        elif i == 'y' or i == 'Y': # Y
            dash()
            dot()
            dash()
            dash()
            el_pause()




        elif i == 'z' or i == 'Z': # Z
            dash()
            dash()
            dot()
            dot()
            el_pause()




        elif i == '1':
            dot()
            dash()
            dash()
            dash()
            dash()
            el_pause()




        elif i == '2':
            dot()
            dot()
            dash()
            dash()
            dash()
            el_pause()




        elif i == '3':
            dot()
            dot()
            dot()
            dash()
            dash()
            el_pause()




        elif i == '4':
            dot()
            dot()
            dot()
            dot()
            dash()
            el_pause()




        elif i == '5':
            dot()
            dot()
            dot()
            dot()
            dot()
            el_pause()




        elif i == '6':
            dash()
            dot()
            dot()
            dot()
            dot()
            el_pause()




        elif i == '7':
            dash()
            dash()
            dot()
            dot()
            dot()
            el_pause()




        elif i == '8':
            dash()
            dash()
            dash()
            dot()
            dot()
            el_pause()




        elif i == '9':
            dash()
            dash()
            dash()
            dash()
            dot()
            el_pause()




        elif i == '0':
            dash()
            dash()
            dash()
            dash()
            dash()
            el_pause()




        elif i == ' ':
            word_pause()



        
        elif i == '|':
            break




        else:
            print("""


            |=============================================|
            |WARNING: INVALID CHARATER DETECTED! SKIPPING!|
            |=============================================|


            """)



            time.sleep(1)
            continue



def morse_to_text(morse):
    

    
    
    for i in morse:




        if i == '.-':
            print('a')
            text_pause()            

        


        elif i == '-...':
            print('b')
            text_pause()            

        


        elif i == '-.-.':
            print('c')
            text_pause()            




        elif i == '-..':
            print('d')
            text_pause()            




        elif i == '.':
            print('e')
            text_pause()            




        elif i == '..-.':
            print('f')
            text_pause()            




        elif i == '--.':
            print('g')
            text_pause()            




        elif i == '....':
            print('h')
            text_pause()            




        elif i == '..':
            print('i')
            text_pause()            




        elif i == '.---':
            print('j')
            text_pause()            




        elif i == '-.-':
            print('k')
            text_pause()            




        elif i == '.-..':
            print('l')
            text_pause()            




        elif i == '--':
            print('m')
            text_pause()            




        elif i == '-.':
            print('n')
            text_pause()            




        elif i == '---':
            print('o')
            text_pause()            




        elif i == '.--.':
            print('p')
            text_pause()            




        elif i == '--.-':
            print('q')
            text_pause()            




        elif i == '.-.':
            print('r')
            text_pause()            




        elif i == '...':
            print('s')
            text_pause()            




        elif i == '-':
            print('t')
            text_pause()            




        elif i == '..-':
            print('u')
            text_pause()            




        elif i == '...-':
            print('v')
            text_pause()            




        elif i == '.--':
            print('w')
            text_pause()            




        elif i == '-..-':
            print('x')
            text_pause()            




        elif i == '-.--':
            print('y')
            text_pause()            




        elif i == '--..':
            print('z')
            word_pause()




        elif i == '-----':
            print('0')
            text_pause()            




        elif i == '.----':
            print('1')
            text_pause()            




        elif i == '..---':
            print('2')
            text_pause()            




        elif i == '...--':
            print('3')
            text_pause()            




        elif i == '....-':
            print('4')
            text_pause()            




        elif i == '.....':
            print('5')
            text_pause()            




        elif i == '-....':
            print('6')
            text_pause()




        elif i == '--...':
            print('7')
            text_pause()        




        elif i == '---..':
            print('8')
            text_pause()




        elif i == '----.':
            print('9')
            text_pause()





        elif i == '|':
            word_pause()




        else:
            print("""


            |=============================================|
            |WARNING: INVALID CHARATER DETECTED! SKIPPING!|
            |=============================================|


            """)




            time.sleep(1)
            continue



def translations():
    print("""
            |=============================================|
            |*********************************************|
            |************AGENT MORSE DICTIONARY***********|
            |*********************************************|
            |=============================================|
          


            |==============================|
            |          ALPHABETS           |
            |==============================|

        A ----------------------> .-  
             
        B ----------------------> -...   
          
        C ----------------------> -.-.   
          
        D ----------------------> -..
          
        E ----------------------> .     
          
        F ----------------------> ..-.
          
        G ----------------------> --.    
          
        H ----------------------> ....
          
        I ----------------------> ..   
          
        J ----------------------> .---   
          
        K ----------------------> -.-    
          
        L ----------------------> .-..
          
        M ----------------------> --    
          
        N ----------------------> -.     
          
        O ----------------------> ---    
          
        P ----------------------> .--.
          
        Q ----------------------> --.-   
          
        R ----------------------> .-.    
          
        S ----------------------> ...    
          
        T ----------------------> -
          
        U ----------------------> ..-    
          
        V ----------------------> ...-   
          
        W ----------------------> .--    
          
        X ----------------------> -..-
          
        Y ----------------------> -.--   
          
        Z ----------------------> --..
    
          
            |==============================|
            |           NUMBERS            |
            |==============================|

        0 ----------------------> -----  
          
        1 ----------------------> .----  
          
        2 ----------------------> ..---  
          
        3 ----------------------> ...--
          
        4 ----------------------> ....-  
          
        5 ----------------------> .....  
          
        6 ----------------------> -....  
          
        7 ----------------------> --...
          
        8 ----------------------> ---..  
          
        9 ----------------------> ----.
          
            |=============================================|
            |******************PAGE ENDS******************|
            |=============================================|
        """)



print("""
            =======================================================
            |       |\      /|                  ------------      |
            |  M    | \    / |         TO            |            |
            |  O    |  \  /  | <---------------->    |         T  |
            |  R    |   \/   |         TO            |         E  |
            |  S    |        |                       |         X  |
            |  E    |        |                       |         T  |
            |       |        |     BY 8rupees        |            |
            =======================================================
        """)
 



while True:




    try:           
                
        


        print("""
                1) Text  ------> Morse
                2) Morse ------> Text
                3) Show Translations
                4) Close the script
                """)




        choice = int(input("Make a selection: "))




        if choice > 0 and choice < 4:
            pass




        else:
            print("MAKE A VALID CHOICE BETWEEN 1 AND 3!")




    except:
        print("MAKE A VALID SELECTION FROM 1-3!")
    



    if choice == 1:
        
        
        

        text = input('Enter your secret message: ')
        
        

        
        print("""
        =============================
        |        CONVERTING         |
        =============================
        """)
    
    
    

        text_to_morse(text)
    
    
    

        print("""
        =============================
        |         CONVERTED         |
        =============================
        """)




    elif choice == 2:




        print("""
        ============================================
        |                 TIPS                     |
        |                                          |
        |***YOU CAN USE " | " TO SEPERATE WORDS!***|
        ============================================
        """)




        code = input("Enter the Morse Code: ")
        code_split = code.split()




        print("""
        =============================
        |        CONVERTING         |
        =============================
        """)
        
        

        
        morse_to_text(code_split)
        
        
        

        print("""
        =============================
        |         CONVERTED         |
        =============================
        """)




    elif choice == 3:
        translations()


    elif choice == 4:
        break

print("""
        =================
        |STAY SAFE AGENT|
        =================
        """)
