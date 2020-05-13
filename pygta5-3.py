import numpy as np
from PIL import ImageGrab
import cv2
import time
from directkeys_mac import KeyPress,KeyDown,KeyUp


for i in list(range(4))[::-1]:
	print(i+1)
	time.sleep(1)


print('down')
#KeyPress('w')
KeyDown('a')
time.sleep(3)




def process_img(org_img):
	p_img = cv2.cvtColor(np.float32(org_img), cv2.COLOR_BGR2GRAY)
	p_img = cv2.Canny(np.uint8(p_img), threshold1=200, threshold2=300)
	return p_img


last_time = time.time()

#while(True):
#	screen = ImageGrab.grab(bbox=(0,40,800,640))
#	new_screen = process_img(screen)
#
#	print('loop took {} seconds'.format(time.time()-last_time))
#	last_time=time.time()
#	cv2.imshow('window', new_screen)
#	#cv2.imshow('window', cv2.cvtColor(np.array(screen), cv2.COLOR_BGR2RGB))
#	if cv2.waitKey(25) & 0xFF == ord('q'):
#		cv2.destroyAllWindows()
#		break
#