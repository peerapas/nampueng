import cv2

capture = cv2.VideoCapture(0)

img_counter = 0

while(True):
    ret, frame = capture.read()
    if not ret:
        print('failed to grab frame')
        break
    cv2.imshow('Test', frame)
    k = cv2.waitKey(1)
    if k%256 == 32:
        
        img_name = 'opencv_img_{}.png'.format(img_counter)
        cv2.imwrite(img_name, frame)
        print('{} written'.format(img_name))
        img_counter += 1
    elif k%256 == 27:
        break;
    
capture.release()
cv2.destroyAllWindows()