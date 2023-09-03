import cv2

# Open the webcam (you can specify the camera index or video file path)
cap = cv2.VideoCapture(0)

# Check if the webcam opened successfully
if not cap.isOpened():
    print("Error: Could not open webcam")
    exit()

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read frame")
        break

    # Add the "Hello, World!" text to the frame
    text = "Hello, World!"
    font = cv2.FONT_HERSHEY_SIMPLEX
    position = (20, 50)
    font_scale = 1
    font_color = (0, 255, 0)  # Green color in BGR
    line_thickness = 2

    cv2.putText(frame, text, position, font, font_scale, font_color, line_thickness)

    # Display the frame with the text
    cv2.imshow('Webcam', frame)

    # Exit the loop when the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the OpenCV window
cap.release()
cv2.destroyAllWindows()
