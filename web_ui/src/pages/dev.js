import React, { useState } from "react";

const container= {
    margin: 'auto',
    width: '50%'
};


var client = new WebSocket("ws://localhost:8080");
console.log("Create Connection to WebSocket");




function Dev() {
    const [key, setKey] = useState(null);
    const [msg, setMsg] = useState(null);
    const [file, setFile] = useState(null);

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
        console.log("Here");
        var reader = new FileReader();
        reader.readAsDataURL(file);
        reader.onload = () => {
            const img = reader.result;
            console.log(img);
            client.send(img);
        };
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
                
            </div>
        </>

    );
}

export default Dev;