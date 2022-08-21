import cv2
# cv2 is directory & mediapipe is our framework
import mediapipe as mp
import time

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose() # here we created an object

cap = cv2.VideoCapture('PoseVideos/5.mp4')
pTime = 0

while True:
    success, img = cap.read()   # Here img is in BGR and our framework uses RGB so we write a code to convert BGR to RGB
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # so now our image is converted and sent to module
    results = pose.process(imgRGB)  # this give dection of our pose
    print(results.pose_landmarks) # this gives landmark co-ordinate i.e x,y,z, along with visibility

    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)  # if results have landmark then show landmark along with there connectionss
        # 14.18 in video check detail info about landmark of human body
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = img.shape
            print(id, lm)  # so we have now printed all landmarks with there co-ordinates

            cx, cy = int(lm.x*w), int(lm.y*h)             # check all landmark co-ordinates value are in decimal i.e they are decimal so we are getting there corresponding pixel valuse
            cv2.circle(img, (cx,cy), 1, (128,0,0), cv2.FILLED) # This is used to give pixel postion for x & y along with size of dot here is (2) & color is (0,128,0) i.e green you can hcnage size and color of dots by changing here values


    cTime = time.time()
    # cTime is current time pTime is previous time
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3,
                (0, 0, 0), 3)
    # This whole thing is written to get the frame rate of image
    cv2.imshow("Image", img)
    cv2.waitKey(1)

