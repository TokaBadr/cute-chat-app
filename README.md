# cute-chat-app
🌸 Cute Python Asynchronous Chat App
Overview
This project is a custom-built, WhatsApp-style live chat application. It uses Python's Socket programming and Threading to allow multiple devices to communicate over the internet.

✨ Key Features
Asynchronous Messaging: By utilizing Python's threading module, users can send and receive messages at the exact same time without the program freezing.

Cloud-Hosted Relay Server: The server acts as a "group chat" or relay. Instead of writing its own messages, it listens for incoming connections and instantly forwards any received message to all other connected clients. It is configured to be deployed on Railway using a TCP Proxy.

Beautiful Custom UI: The client-side application features a cute, custom-themed Graphical User Interface built entirely with Python's built-in tkinter library, requiring zero extra installations.

🛠️ Technologies & Concepts
Python 3

Socket Programming (Raw TCP): For handling the network connections between devices.

Threading: For running background tasks (like listening for incoming messages) while keeping the main user interface active and responsive.

Tkinter: For building the interactive client-side GUI.

Railway & TCP Proxy: Used to host the server in the cloud, providing a public IP and port so users can connect from completely different networks, rather than just on a local localhost.

🚀 How It Works
This repository specifically contains the server.py file, which is designed to be hosted continuously in the cloud 24/7. The client.py script remains on the users' local computers. Once the server is deployed and listening, multiple clients can connect to the server's public Railway address and chat with each other in real-time.
