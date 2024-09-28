from playsound import playsound
import cv2
from PIL import Image

def mediaplayer(file_path):
    # open these type of text files 
    if file_path.endswith(".txt") or file_path.endswith(".pdf"):
        
        try:
            with open(file_path, 'r') as f:
                text_content = f.read()
                print("Text content(s): ")
                print(text_content)
                
        except Exception as e:
            print(f"Error reading file: {e}")
    
    # play an audio file
    elif file_path.endswith('.mp3') or file_path.endswith('.wav'):
        
        try:
            playsound(file_path)
            print("Audio file(s) played. ")
            
        except Exception as e:
            print(f"Error playing audio: {e}")
    
    # show an image
    elif file_path.endswith('.jpg') or file_path.endswith('.png') or file_path.endswith('.gif'):
        
        try:
            img = Image.open(file_path)
            img.show()
            print("Image(s) displayed. ")
            
        except Exception as e:
            print(f"Problem loading image: {e}")
    
    # this will play a video
    elif file_path.endswith('.mp4') or file_path.endswith('.avi'):
        try:
            cap = cv2.VideoCapture(file_path)
            while True:
                ret, frame = cap.read()
                
                if not ret:
                    break
                
                cv2.imshow('video', frame)
                
                # quit the video with 'q' key after 1 mills
                if cv2.waitKey(1.5) & 0xFF == ord('q'):
                    break
                
            cap.release()  
            cv2.destroyAllWindows()
            print("Video has played.")
            
        except Exception as e:
            print(f"Problem playing video: {e}")
            
    else:
        print("This file format is not supported! Please try ampther.")

# inputs the file
filename = input("Hello, please enter your filename: ")

mediaplayer(filename)