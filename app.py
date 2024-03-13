from flask import Flask, render_template, Response, request
from image_processor import ImageProcessor
from camera import Camera
import constants

import os

app = Flask(__name__)

if not os.path.exists(constants.UPLOAD_FOLDER):
    os.makedirs(constants.UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = constants.UPLOAD_FOLDER

@app.route('/')
def index():
    """Render the index.html template."""
    return render_template('index.html')

@app.route('/upload_image', methods=['POST'])
def upload_image():
    """
    Handle image upload and text extraction.

    Returns:
        Rendered HTML template with the extracted text or error message.
    """
    if 'file' not in request.files:
        return render_template('index.html', error='No file part')
    
    file = request.files['file']

    if file.filename == '':
        return render_template('index.html', error='No selected file')
    
    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        extracted_text = ImageProcessor.extract_text_from_image(file_path)
        extracted_text_ingredients = ImageProcessor.extract_ingredients(extracted_text)

        if extracted_text_ingredients is None:
            if len(extracted_text) == 0:
                extracted_text_ingredients = constants.NOT_FOUND_MESSAGE
            else:
                extracted_text_ingredients =  constants.INGREDIENTS_NOT_FOUND_MESSAGE + extracted_text

        os.remove(file_path)
        return render_template('index.html', extracted_text=extracted_text_ingredients)
    
    return render_template('index.html', error='Invalid file format')

@app.route('/video_feed')
def video_feed():
    """
    Stream the video feed from the camera.

    Returns:
        Response object containing the video feed frames.
    """
    def generate_frames():
        camera = Camera()
        for frame in camera.get_frames():
            yield frame
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/capture')
def capture():
    """
    Capture and save an image from the camera.

    Returns:
        Rendered HTML template indicating that the image has been saved.
    """
    file_path = Camera.capture_image()
    return render_template('image_saved.html', file_path=file_path)

if __name__ == '__main__':
    app.run(debug=True)
