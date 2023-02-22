import cv2
import time

camera = cv2.VideoCapture(-1)

current_frame_count = 0
total_time = 30
start_time = time.time()

while int(time.time()-start_time < total_time):
    ret,frame = camera.read()
    cv2.imshow("LiveVideo", frame)
    if ret:
        name = 'collected_images' + str(current_frame_count) + '.jpg'
        cv2.imwrite(name, frame)
        current_frame_count += 1
    else:
        break
    key = cv2.waitKey(1)
    if key == 27:
        break

camera.release()
cv2.destroyAllWindows()