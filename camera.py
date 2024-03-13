import cv2
import datetime

class Camera:

    @staticmethod
    def capture_image():
        """
        Captures an image using the camera.

        Returns:
            str: The file path of the captured image.
        """
        now = datetime.datetime.now()
        timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
        file_name = f"static/capture_{timestamp}.jpg"
        camera = cv2.VideoCapture(0)
        success, frame = camera.read()
        camera.release()
        cv2.imwrite(file_name, frame)
        return file_name

    def get_frames(self):
        """
        Generates frames from the camera for video streaming.

        Yields:
            bytes: The encoded frame as bytes.
        """
        camera = cv2.VideoCapture(0)
        while True:
            success, frame = camera.read()
            if not success:
                break
            else:
                ret, buffer = cv2.imencode('.jpg', frame)
                frame = buffer.tobytes()
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        camera.release()
