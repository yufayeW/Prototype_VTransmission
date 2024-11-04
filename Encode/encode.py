import cv2

def encode_video(input_file, output_file):
    # Open the input video file
    video = cv2.VideoCapture(input_file)

    # Get the video codec and create a VideoWriter object
    codec = cv2.VideoWriter_fourcc(*'XVID')
    fps = video.get(cv2.CAP_PROP_FPS)
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    writer = cv2.VideoWriter(output_file, codec, fps, (width, height))

    # Read and encode each frame of the video
    while True:
        ret, frame = video.read()
        if not ret:
            break
        encoded_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        writer.write(encoded_frame)

    # Release the video objects
    video.release()
    writer.release()

def decode_video(input_file, output_file):
    # Open the input video file
    video = cv2.VideoCapture(input_file)

    # Get the video codec and create a VideoWriter object
    codec = cv2.VideoWriter_fourcc(*'XVID')
    fps = video.get(cv2.CAP_PROP_FPS)
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    writer = cv2.VideoWriter(output_file, codec, fps, (width, height))

    # Read and decode each frame of the video
    while True:
        ret, frame = video.read()
        if not ret:
            break
        decoded_frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
        writer.write(decoded_frame)

    # Release the video objects
    video.release()
    writer.release()

# Example usage
input_file = 'D:\Semester9\毕业设计\Prototype1\1.mp4'
encoded_file = 'encoded_video.mp4'
decoded_file = 'decoded_video.mp4'

encode_video(input_file, encoded_file)
decode_video(encoded_file, decoded_file)