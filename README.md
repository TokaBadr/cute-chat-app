# cute-chat-app
🌸 **Cute Python Asynchronous Chat App**

### **Overview**
This project is a custom-built, WhatsApp-style live chat application. It uses Python's Socket programming and Threading to allow multiple devices to communicate over the internet, and has been fully upgraded to support rich multimedia sharing, including images, files, and live voice notes!

### **✨ Key Features**
* **Asynchronous Messaging:** By utilizing Python's threading module, users can send and receive messages at the exact same time without the program freezing.
* **Rich Multimedia Sharing:** Users can send general files, videos, record 5-second live voice notes directly from their microphone, and send images with a toggleable "HD" button to choose between high-quality originals or compressed sizes.
* **Custom File Transfer Protocol:** Built entirely from scratch using a custom "End of File" (EOF) Delimiter Protocol to handle binary data transfers, bypassing the need to pre-calculate file sizes over the network.
* **Cloud-Hosted Relay Server:** The server acts as a "group chat" or relay. Instead of writing its own messages, it listens for incoming connections and instantly forwards any received message to all other connected clients. It is configured to be deployed on Railway using a TCP Proxy.
* **Beautiful Custom UI:** The client-side application features a cute, custom-themed Graphical User Interface built with `tkinter`, featuring interactive inline media playback buttons, auto-scrolling, message timestamps, and an animated progress bar for file uploads.

### **🛠️ Technologies & Concepts**
* **Python 3**
* **Socket Programming (Raw TCP):** For handling the network connections between devices.
* **Threading:** For running background tasks (like listening for incoming messages or uploading heavy files) while keeping the main user interface active and responsive.
* **Tkinter & TTK:** For building the interactive client-side GUI and styling the progress bars.
* **PIL (Pillow):** For image compression, resizing, and rendering UI thumbnails.
* **Sounddevice & Scipy:** For capturing and processing live microphone audio into `.wav` files.
* **OS Pathing:** Utilizing absolute pathing (`SCRIPT_DIR`) to securely save downloaded media directly to the local project environment.
* **Railway & TCP Proxy:** Used to host the server in the cloud, providing a public IP and port so users can connect from completely different networks, rather than just on a local localhost.

### **🚀 How It Works**
This repository specifically contains the `server.py` file, which is designed to be hosted continuously in the cloud 24/7. The `client.py` script remains on the users' local computers. Once the server is deployed and listening, multiple clients can connect to the server's public Railway address and chat with each other in real-time. All shared media files and voice notes are automatically downloaded and saved directly to the user's local machine.
