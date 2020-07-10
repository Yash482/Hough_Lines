import numpy as np
import cv2
import matplotlib.pyplot as plt
# matplotlib qt

img = cv2.imread("mobile.jpeg")
img_copy= np.copy(img)
img_copy = cv2.cvtColor(img_copy, cv2.COLOR_BGR2RGB)
#plt.imshow(img_copy)
gray = cv2.cvtColor(img_copy, cv2.COLOR_RGB2GRAY)
#plt.imshow(gray)

edged = cv2.Canny(gray, 120, 240)
#plt.imshow(edged)

rho =1
theta = np.pi/180
threshold = 60
min_line_length =70
max_line_gap =5
lines = cv2.HoughLinesP(edged, rho, theta, threshold, np.array([]), min_line_length , max_line_gap )
line_img = np.copy(img_copy)
for line in lines:
    for a, b, c, d in line:
        cv2.line(line_img, (a,b), (c,d), (25, 250, 200), 2)
        
plt.imshow(line_img)
