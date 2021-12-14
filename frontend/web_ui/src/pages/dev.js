import React, { useState, useRef} from "react";
import WebCam from "react-webcam";

const container= {
    margin: 'auto',
    width: '50%'
};


const vid_constraints = {
    width: {ideal: 4096},
    height: {ideal: 2160},
    facingMode: "user"
}

function Dev() {
    var client = new WebSocket("ws://localhost:8080");
    console.log("Create Connection to WebSocket");
    
    const [key, setKey] = useState(null);
    const [msg, setMsg] = useState(null);
    const [file, setFile] = useState(null);

    const webRef = useRef(null);

    const key_handler = (event) => {
        setKey(event.key);
        client.send(event.key);
    };

    client.onmessage = (e) => {
        setMsg(e.data)
    }

    const file_handler = (event) => {
        setFile(event.target.files[0]);
        console.log("Successfully set file");
    }

    const file_submission = (event) => {
        event.preventDefault();
        var reader = new FileReader();
        reader.readAsDataURL(file);
        reader.onload = () => {
            const img = reader.result;
            client.send(img);
        };
    }

    const sendImage = () => {
        const FPS = 25;
    
        const img = webRef.current.getScreenshot();
        const msg = JSON.stringify(
            {message: "image",
            content: img}
        );
        client.send(msg);
        console.log("Image sent, check server");
        setTimeout(sendImage, (1000/FPS))

    }

    return (
        <>
            <div style={container}>
                {key ? <h1>You Pressed: {key}</h1> : null}
                <h3>Please start collecting keyboard input as it will send to server socket if available</h3>
                <input
                    type="text"
                    placeholder="Input Key"
                    onKeyPress={(e) => key_handler(e)}
                />
                <br />
                {msg ? <big>{msg}</big> : null}
                <br />
                <form
                    onSubmit={file ? (e) => file_submission(e) : console.log("No file to submit")}
                >

                    <input
                        type="file"
                        onChange={(e) => file_handler(e)}
                    />
                    <button
                        type="submit"
                    >Submit</button>
                </form>
                <br />
                <WebCam 
                ref={webRef}
                screenshotFormat="image/jpeg"
                videoConstraints={vid_constraints}
                />
                <button onClick={() => {
                    sendImage()
                }}>Send Image to socket</button>

                
            </div>
        </>

    );
}

export default Dev;