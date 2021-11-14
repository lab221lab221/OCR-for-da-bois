import cv2
import pytesseract
import numpy as np
import pyautogui

codec = cv2.VideoWriter_fourcc(*"XVID")

out = cv2.VideoWriter("Recorded.avi", codec , 60, (1000, 550))

cv2.namedWindow("Recording", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Recording", 480, 270)

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
i = 0
while True:
    img = pyautogui.screenshot(region=(0, 150, 1000, 700)) #capturing screenshot
    frame = np.array(img) #converting the image into numpy array representation
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) #converting the BGR image into RGB image

    if i % 10 == 0 and not i == 0:
        i = 0
        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        gray, img_bin = cv2.threshold(gray,128,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        gray = cv2.bitwise_not(img_bin)

        kernel = np.ones((2, 1), np.uint8)
        img = cv2.erode(gray, kernel, iterations=1)
        img = cv2.dilate(img, kernel, iterations=1)
        out_below = pytesseract.image_to_string(img)
        print("OUTPUT:", out_below)
    
    #out.write(frame) #writing the RBG image to file
    cv2.imshow('Recording', frame) #display screen/frame being recorded
    if cv2.waitKey(1) == ord('q'): #Wait for the user to press 'q' key to stop the recording
        break
    i += 1

out.release() #closing the video file
cv2.destroyAllWindows()
"""
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

directory = input("Directory of screenshot (ex. C://Users/me/downloads/happieness.png):")
img = cv2.imread(directory)

gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
gray, img_bin = cv2.threshold(gray,128,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
gray = cv2.bitwise_not(img_bin)

kernel = np.ones((2, 1), np.uint8)
img = cv2.erode(gray, kernel, iterations=1)
img = cv2.dilate(img, kernel, iterations=1)
out_below = pytesseract.image_to_string(img)
print("OUTPUT:", out_below)
"""
"""
answer = input("Example sentence:")
scramble = input("Scrambled sentence:")

letters = {}
for i in range(len(scramble)):
    if scramble[i-1] in list(letters.keys()):
        continue
    else:
        letters[scramble[i-1]] = answer[i-1]

decrypt = input("What sentence to decrypt:")
final = ""
for i in decrypt:
    if i not in list(letters.keys()):
        help_inp = input(f"Help - What is the answer to the letter of \"{i}\" after decryption:")
        letters[i] = help_inp
    final += letters[i]

print(final)
"""
