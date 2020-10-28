import cv2
# inputting an image in open cv 
 img = cv2.imread("File_path") # It converts the image value inside matrix 

# Writing means : Adding any file name , Matrix value : Object : Annotation
 imwrite(filename , mat) 

# Python GUI
# Showing the output image/video 
cv2.imshow()
#RGB Analyis : Classyfying a image on the basis of red , blue and green 
IMREAD_COLOR(BGR_input values)
# Change coloured image to a binary image
# Extracting negative of an image 
# Developed by using optical rays : RGB Analysis
threshold( Mat src, Mat dst , double thresh , double maxval , int type )

# If you eant to do image annotation
circle(img , center , radius , color , thickness)
rectangle(img , pt1 , pt2, color , thickness)

# Blurring of an image
# Average Blur : Smoothning 
cv2.blur(src, dst,ksize,anchor, bordertype)
# Median Blur : It gives an output pixel value , or an output image by cal median of initial pixels
cv2.medianblur(src , dst , ksize)
# Guassian Blur : Image & Filters
cv2.GuassianBlur(src , dst , ksize, sigmaX)
# Sigma X is extent of blur
