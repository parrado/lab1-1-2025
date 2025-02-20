# pip install opencv-python
import cv2

# Open the default camera
cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)

# Get the default frame width and height
frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))


while True:
    # Read frame from camera
    ret, frame = cam.read()

    #print(len(frame))

    # Display the captured frame after flipping
    cv2.imshow('Parking Lot Camera', cv2.flip(frame,1))  

    # Wait for 10ms and exit if any key is pressed
    if cv2.waitKey(10) != -1:
        break
    

# Release the capture object
cam.release()
cv2.destroyAllWindows()