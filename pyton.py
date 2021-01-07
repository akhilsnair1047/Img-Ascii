#import the pywhatkit module as kt
import pywhatkit as kt

#capture source and target path
source_path = 'python_image.png'
target_path = 'output_image.text'

#call the method
kt.image_to_ascii_art(source_path, target_path)

#display
print("Images to ASCII art!")