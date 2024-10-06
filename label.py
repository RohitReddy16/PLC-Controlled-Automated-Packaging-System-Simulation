import cv2

# Load the image of a product on the conveyor
product_image = cv2.imread('product_with_label.jpg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(product_image, cv2.COLOR_BGR2GRAY)

# Thresholding to detect the label region (assuming a distinct label color or pattern)
_, thresholded_image = cv2.threshold(gray_image, 120, 255, cv2.THRESH_BINARY)

# Detect contours to locate the label
contours, _ = cv2.findContours(thresholded_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Iterate through contours and check for the label (based on size or position)
for contour in contours:
    area = cv2.contourArea(contour)
    if area > 1000:  # Assuming the label area is significant
        # Draw a bounding box around the detected label
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(product_image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Display the result with the detected label
cv2.imshow('Label Detection', product_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
