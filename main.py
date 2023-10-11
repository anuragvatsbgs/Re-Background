# A software for remove background from image with same quality of image
print( '''

--------------------------------------------------------------
      
                 ooooooooo.   oooooo99
                 888   `Y88.  00        
                 888   .d88'  00        
                 888ooo88P'   00oo99   
                 88866        00        
                 888  66      00        
                 o88    66    oooooo99

                Welcome to Re-background
            https://github.com/anuragvatsbgs
      
                    Version 0.1

---------------------------------------------------------------          
              
''')
# printing RE in top of page
print(" Wait...")
from rembg import remove  
from PIL import Image
import easygui as eg
lst=0
while lst!=1:
    try:
        try:
            input_path = eg.fileopenbox(title='Select image file')  # selecting image path file
            output_path = eg.filesavebox(title='Save file to..')    # selecting output image file
            input1 = Image.open(input_path)
            output = remove(input1)                                 # For removing image background
            output.save(output_path)                                # For saving on selected output file
            print("Sucessfull save To Location ",output_path)       # Show File location for saving 
            print("Press 0 to Continue\nPress 1 to Exit")           # For further Operations performs on image
            lst=int(input("Enter Your Choice"))
        except:
            print("Complete The Task")                              # Error no recmd001 Defined in Anusav Technology sites
            lst=0
    except:
        print("Thank you For using our Application.")               # Error no recmd002 Defined in Anusav Technology sites
     
