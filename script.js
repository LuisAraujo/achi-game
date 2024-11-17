var ws = new WebSocket("ws://localhost:8888/achi-game/");

ws.onopen = function (event) {
    var msg = {
        type: "message"
    };

    ws.send(JSON.stringify(msg));
};

ws.onmessage = function (event) {
    console.log(event.data);
};