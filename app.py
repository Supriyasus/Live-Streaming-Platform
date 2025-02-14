from flask import Flask, render_template, Response, redirect, url_for
import cv2

app = Flask(__name__)
camera=cv2.VideoCapture(0)

def video_frames():
    while True:
        success,frames=camera.read()
        if not success:
            break
        else:
            ret,buffer=cv2.imencode('.jpg',frames)
            frame=buffer.tobytes()
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(video_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)