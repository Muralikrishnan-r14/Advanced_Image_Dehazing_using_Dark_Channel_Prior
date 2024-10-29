import cv2
import numpy as np


# Function to perform advanced dehazing using dark channel prior
def dehaze(frame):
    # Convert the frame to float32
    frame = frame.astype(np.float32) / 255.0

    # Estimate the atmospheric light
    dark_channel = get_dark_channel(frame)
    atmospheric_light = estimate_atmospheric_light(frame, dark_channel)

    # Estimate the transmission map
    transmission_map = estimate_transmission(frame, atmospheric_light)

    # Apply the dehazing equation
    epsilon = 0.001
    dehazed_frame = np.zeros_like(frame)
    for i in range(3):
        dehazed_frame[:, :, i] = (frame[:, :, i] - atmospheric_light[i]) / np.maximum(transmission_map, epsilon) + \
                                 atmospheric_light[i]

    # Clip values to ensure they are in valid range
    dehazed_frame = np.clip(dehazed_frame, 0, 1)

    # Convert the frame back to uint8
    dehazed_frame = (dehazed_frame * 255).astype(np.uint8)

    return dehazed_frame


# Function to compute the dark channel prior
def get_dark_channel(frame, window_size=15):
    dark_channel = np.zeros((frame.shape[0], frame.shape[1]))
    padded_frame = np.pad(frame, ((window_size // 2, window_size // 2), (window_size // 2, window_size // 2), (0, 0)),
                          mode='edge')

    for i in range(frame.shape[0]):
        for j in range(frame.shape[1]):
            dark_channel[i, j] = np.min(padded_frame[i:i + window_size, j:j + window_size, :])

    return dark_channel


# Function to estimate the atmospheric light
def estimate_atmospheric_light(frame, dark_channel, percent=0.001):
    flat_dark_channel = dark_channel.flatten()
    num_pixels = flat_dark_channel.size
    num_brightest_pixels = int(num_pixels * percent)
    indices = np.argpartition(flat_dark_channel, -num_brightest_pixels)[-num_brightest_pixels:]
    brightest_pixels = frame.reshape(-1, 3)[indices]
    atmospheric_light = np.max(brightest_pixels, axis=0)
    return atmospheric_light


# Function to estimate the transmission map
def estimate_transmission(frame, atmospheric_light, omega=0.95, window_size=15):
    normalized_frame = frame.astype(np.float32) / np.maximum(atmospheric_light, 0.1)
    transmission_map = 1 - omega * get_dark_channel(normalized_frame, window_size)
    return transmission_map


def main():
    # Open the webcam
    cap = cv2.VideoCapture(0)

    # Check if the webcam is opened successfully
    if not cap.isOpened():
        print("Error: Could not open webcam")
        return

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture frame")
            break

        # Perform dehazing
        dehazed_frame = dehaze(frame)

        # Display the original and dehazed frame
        cv2.imshow('Original', frame)
        cv2.imshow('Dehazed', dehazed_frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close all windows
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()