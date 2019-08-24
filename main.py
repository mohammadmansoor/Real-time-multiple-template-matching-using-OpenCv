import cv2
from matplotlib import pyplot as plt
import numpy as np


cap = cv2.VideoCapture("video.mp4",0)
while(True):

	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	for i in range(1,10):
		
		template = cv2.imread('templates/'+str(i)+'.jpg',0)
		w, h = template.shape[::-1]

		res = cv2.matchTemplate(gray,template,cv2.TM_CCORR_NORMED)

		threshold = 0.99

		loc = np.where(res >= threshold)
		for box in zip(*loc[::-1]):

		    cv2.rectangle(frame, box, (box[0] + w, box[1] + h), (0, 0, 255), 2)
		
	cv2.imshow('frame',frame)


	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows() 
