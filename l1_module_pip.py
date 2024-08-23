#1. Install an external module and 
# use it to perform an operation of your interest.
import pyttsx3
engine = pyttsx3.init()
engine.say("hey dude just let me know your name ")
engine.runAndWait()

# 2.print content of directory using os module
import os
directory_path='/Intel'
content=os.listdir(directory_path)
for item in content:
    print(item)
