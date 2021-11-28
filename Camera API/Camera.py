import cv2
from flask import Flask, render_template, Response
from flask_cors import CORS, cross_origin

host = '0.0.0.0'; port=3005
app = Flask(__name__)
app.config["DEBUG"] = True
app.config['CORS_HEADERS'] = 'Content-Type'

cam = cv2.VideoCapture(0)

def gen_frames():
    while True:
        success, frame = cam.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.png', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/png\r\n\r\n' + frame + b'\r\n')


@app.route('/')
def index():
    return render_template('test.html')

@app.route('/video')
@cross_origin()
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host=host, port=port)
'''
vid = cv2.VideoCapture(0)

while True:
    ret, frame = vid.read()

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()

cv2.destroyAllWindows()
'''