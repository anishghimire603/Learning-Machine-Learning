import cv2qq

#THISIS MY WEB CAMERE
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, back = cap.read()   #HERE I AM SIMPLY READING FROM MY WEBCAM
    if ret:
        #back is what the camera is reading
        cv2.imshow("image", back)
        if cv2.waitKey(5) == ord('q'):
            #save the image
            cv2.imwrite('image.jpg', back)
            break

cap.release()
cv2.destroyAllWindows()
