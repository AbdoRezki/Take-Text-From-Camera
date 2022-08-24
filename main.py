import cv2
import pytesseract

cam = cv2.VideoCapture(0)

cv2.namedWindow('cam-test')
while True:
    s, img = cam.read()
    if not s:
        print('fail')
        break
    cv2.imshow('cam-test', img)
    k  = cv2.waitKey(1)
    if k%256 == 27:
        print('Closing')
        break
    elif k%256  == 32:
        cv2.imwrite("images/filename.jpg",img)
        print('Saved')

cam.release()

cv2.destroyAllWindows()
img= cv2.imread("images/filename.jpg")

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
text = pytesseract.image_to_string(img)
print(text)