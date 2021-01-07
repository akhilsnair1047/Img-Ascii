#import the pywhatkit module as kt
import pywhatkit as kt

#capture source and target path
source_path = 'python_image.png'
target_path = 'output_image.text'

#call the method
kt.image_to_ascii_art(source_path, target_path)

#to show the content of the file in terminal
f = open('output_image.text', 'r')
file_contents = f.read()
print (file_contents)
f.close()



#display
print("Images to ASCII art Saved to PC as : "+ target_path)
