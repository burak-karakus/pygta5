import numpy as np
from PIL import ImageGrab
import cv2
import time
from directkeys_mac import KeyPress,KeyDown,KeyUp

def draw_lines(img, lines):
    try:
        for line in lines:
        	coords = line[0]
        	cv2.line(img, (coords[0],coords[1]), (coords[2],coords[3]), [255,255,255], 3)
    except:
        pass

def roi(img, vertices):
	mask = np.zeros_like(img)
	cv2.fillPoly(mask, vertices, 255)
	masked = cv2.bitwise_and(img, mask)
	return masked



def process_img(org_img):
	p_img = cv2.cvtColor(org_img, cv2.COLOR_BGR2GRAY)
	p_img = cv2.Canny(p_img, threshold1=200, threshold2=300)
	p_img = cv2.GaussianBlur(p_img, (3,3), 0)
	vertices = np.array([[10,500],[10,300],[300,200],[500,200],[800, 300],[800,500]], np.int32)
	p_img = roi(p_img, [vertices])

	lines = cv2.HoughLinesP(p_img, 1, np.pi/180, 180, 50, 15)
	draw_lines(p_img,lines)

	return p_img

def main():
	last_time = time.time()
	while(True):
		screen = np.array(ImageGrab.grab(bbox=(0,40,800,640)))
		new_screen = process_img(screen)
	
		print('loop took {} seconds'.format(time.time()-last_time))
		last_time=time.time()
		cv2.imshow('window', new_screen)
		#cv2.imshow('window', cv2.cvtColor(np.array(screen), cv2.COLOR_BGR2RGB))
		if cv2.waitKey(25) & 0xFF == ord('q'):
			cv2.destroyAllWindows()
			break


if __name__ == "__main__":
	main()