from playsound import playsound
import cv2
import tkinter as tk
import pdfplumber
from tkinter import filedialog
from PIL import Image

def load_media() :
    file_path = filedialog.askopenfilename(title="Select a file")
    
    if not file_path :
        return
    
    print(f"Here is your file: {file_path}.")
    mediaplayer(file_path)
    
def mediaplayer(file_path):
    # open these type of text files 
    if file_path.endswith(".txt"):
        try:
            with open(file_path, 'r') as f:
                text_content = f.read()
                print("Text content(s):")
                print(text_content)
                
            feedback_option(file_path)
        except Exception as e:
            print(f"Error reading text file: {e}")
    
    elif file_path.endswith(".pdf"):
        try:
            # Using pdfplumber to read the PDF content
            with pdfplumber.open(file_path) as pdf:
                print("PDF content(s):")
                for page in pdf.pages:
                    print(page.extract_text())
            feedback_option(file_path)   
        except Exception as e:
            print(f"Error for PDF file: {e}")
    
    # play an audio file
    elif file_path.endswith('.mp3') or file_path.endswith('.wav'):
        
        try:
            playsound(file_path)
            print("Audio file(s) played. ")
            
        except Exception as e:
            print(f"Error playing audio: {e}")
    
    # show an image
    elif file_path.endswith('.jpg') or file_path.endswith('.png') or file_path.endswith('.gif') or file_path.endswith('.jpeg'):
        
        try:
            img = Image.open(file_path)
            img.show()
            print("Image(s) displayed. ")
            feedback_option(file_path)
            
        except Exception as e:
            print(f"Problem loading image: {e}")
    
    # this will play a video
    elif file_path.endswith('.mp4') or file_path.endswith('.avi'):
        try:
            
            #open the video with opencv
            cap = cv2.VideoCapture(file_path)
            if not cap.isOpened():
                print("Error: Couldn't open video file.")
                return
            
            while cap.isOpened():
                ret, frame = cap.read()
                
                if not ret:
                    break
                
                cv2.imshow('video', frame)
                
                # quit the video with 'q' key after 1 mills
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break
                
            cap.release()  
            cv2.destroyAllWindows()
            print("Video has played.")
            feedback_option(file_path)
            
        except Exception as e:
            print(f"Problem playing video: {e}")
            
    else:
        print("This file format is not supported! Please try ampther.")
        
def feedback_option(file_path):
    feedback_screen = tk.Toplevel(file_path)
    feedback_screen.title("Feedback Mechanism")
    
    prompt = tk.Label(feedback_screen, text="Do you want to keep this? ")
    prompt.pack()

    def store_feedback(yes):
        with open("Feedbakc.txt", "a") as f:
            f.write(f"{file_path}: {'Yes' if yes else 'No'} \n")
        feedback_screen.destroy()
        
        yes_button = tk.Button(feedback_screen, text= "Yes", command=lambda: store_feedback(True))
        yes_button.pack(side= tk.LEFT, padx= 1)
        
        no_button =tk.Button(feedback_screen, text= "No", command= lambda: store_feedback(False))
        no_button.pack(side=tk.RIGHT, padx= 1)
        
root = tk.Tk()
root.title("Drag and Drop Input Loader")

load_button = tk.Button(root, text="Drag and Drop Media File", command=load_media)
load_button.pack(pady=20)

root.mainloop()