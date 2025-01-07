import cv2

TITLE = "docker on WSL2"
cv2.namedWindow(TITLE, cv2.WINDOW_AUTOSIZE)

# display image
img = cv2.imread("bird.jpg")
cv2.imshow(TITLE, img)

print("Finish to press ESC...")
while True:
    if cv2.waitKey(1) == 0x1B:
        break

cv2.destroyAllWindows()