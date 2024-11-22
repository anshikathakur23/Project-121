import cv2
import numpy as np

cap = cv2.VideoCapture (0)

image = cv2.imread ('download.jpg')

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize (frame, (640, 480))
    image = cv2.resize (image, (640, 480))

    hsv_frame = cv2.cvtColor (frame, cv2.COLOR_BGR2HSV)

    l_black = np.array ([0, 0, 0])
    u_black = np.array ([180, 255, 50])

    mask = cv2.inRange (frame, l_black, u_black)
    res = cv2.bitwise_and (frame, frame, mask = mask)

    f = frame - res
    f = np.where (mask == 0 , frame, image)

    cv2.imshow ('Original Video', frame)
    cv2.imshow ('Masked Video', f)

    key = cv2.waitKey (1)
    if key == 27 or key == ord ('q'):
        break

cap.release ()
cv2.destroyAllWindows ()