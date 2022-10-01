const roomName = JSON.parse(document.getElementById('room-name').textContent);
const chatLog = document.getElementById('chat-log')


const chatSocket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/chat/'
    + roomName
    + '/'
);

chatSocket.onmessage = (e) => {
    const data = JSON.parse(e.data);
    const messageElement = document.createElement("div")
    const userId = data['user_id']
    const loggedInUserId = JSON.parse(document.getElementById('user_id').textContent)

    if (userId == loggedInUserId) {
        messageElement.innerHTML = `
        <div class="flex justify-end mb-4">
          <div
            class="mr-2 py-3 px-4 bg-blue-400 rounded-bl-3xl rounded-tl-3xl rounded-tr-xl text-white"
          >
          ${data.message}
          </div>
        </div>
        `
    } else {
        messageElement.innerHTML = `
        <div class="flex justify-start mb-4">
          <div
            class="ml-2 py-3 px-4 bg-gray-400 rounded-br-3xl rounded-tr-3xl rounded-tl-xl text-white"
          >
            ${data.message}
          </div>
        </div>
        `
    }

    chatLog.appendChild(messageElement)

    // document.querySelector('#chat-log').value += (data.message);
};

chatSocket.onclose = (e) => {
    console.error('Chat socket closed unexpectedly');
};

document.querySelector('#chat-message-input').focus();
document.querySelector('#chat-message-input').onkeyup = (e) => {
    if (e.keyCode === 13) {  // enter, return
        document.querySelector('#chat-message-submit').click();
    }
};

document.querySelector('#chat-message-submit').onclick = (e) => {
    const messageInputDom = document.querySelector('#chat-message-input');
    const message = messageInputDom.value;
    chatSocket.send(JSON.stringify({
        'message': message
    }));
    messageInputDom.value = '';
};