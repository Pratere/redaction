import cv2
import os,argparse
import pytesseract
import pandas
import re


# parser allows for command line argument to be passed like any bash command
parser = argparse.ArgumentParser()

parser.add_argument("-i", "--image", required=True) # path to image
# parser.add_argument("-b", "--boundings", required=True)
parser.add_argument("-o", "--output", required=True) # output filename

args = vars(parser.parse_args())

image = cv2.imread(args["image"]) # load image

# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# preform OCR, return as a pandas dataframe and drop rows with NaN values
# all NaNs are in the text field and of no use
data = pytesseract.image_to_data(image, output_type=pytesseract.Output.DATAFRAME).dropna()

for idx, row in data.iterrows():
	if re.search("\$", row.text): # replace with regex for SSN
		start = (row.left, row.top) # (x, y) in pixel space
		end = (row.left + row.width, row.top+row.height) 
		
		# draw rectangle on image, -1 line thickness fills in the rectangle
		image = cv2.rectangle(image, start, end, color=(0,0,0), thickness=-1)

cv2.imwrite(args['output'], image)