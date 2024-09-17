from PIL import Image
from playsound import playsound
import cv2

#require pillow, pygame, and moviepy Libraries
def mediaplayer(file_path) : 
    
    
    #this will open these type of text files and its content(s)
    if filename.endswith (".txt") or filename.endswith(".pdf"):
        with open(file_path, 'r') as f:
            textContent = print(f.read())
            print("Text content: ")
            print(textContent)
            
    #this will show an image
    elif filename.endswith('.mp3') or filename.endswith('.wav'):
      playsound(filename)
      print("Audio file played.")
      
    elif filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.gif'):
        img = cv2.imread(filename)
        cv2.imshow('Image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print("Image is displayed.")
    #this will show show a video playing. ret will verify if it reads. 
    # cap to caputre video and frame to hold the frames    
    elif filename.endswith('.mp4') or filename.endswith('.avi'):
        cap = cv2.VideoCapture(filename)
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            cv2.imshow('Video', frame)
            #quit the video with q key after 1 millisecond
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            cap.release()
            cv2.destroyAllWindows()
            print("Video has played.")
    else:
        print("This file type is not supported!")

#User inputs the filename
filename = input("Please enter your filename: ")

# Play the media file
mediaplayer(filename)