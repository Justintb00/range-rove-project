async function test(){
    const response = await fetch('http://localhost:3005/video');
    const reader = response.body.getReader();

    while (true) {
        const { value, done } = await reader.read();
        if (done) break;
        console.log('Received', value);
    }

    console.log('Response fully received');
}
test();