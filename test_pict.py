import cv2 as cv
pict = "/home/ramonpr/Github/vision-cad/nbs/FLOW_Annual_Meeting_2024.png"
img = cv.imread(pict)

cv.imshow("Image", img)

print(img.shape)
print(img.size)
print(img.dtype)

cv.waitKey(0)
cv.destroyAllWindows()

exit(0)
