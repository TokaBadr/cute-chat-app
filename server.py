# server.py
import socket
import threading
import os

connected_clients = []

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected_clients.append(conn)

    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break
            
            # Broadcast the message to all OTHER clients
            for client in connected_clients:
                if client != conn:
                    try:
                        client.sendall(data)
                    except:
                        connected_clients.remove(client)
        except Exception as e:
            break
            
    print(f"[DISCONNECTED] {addr} left the chat.")
    if conn in connected_clients:
        connected_clients.remove(conn)
    conn.close()

def start_server():
    # Railway assigns a port dynamically. Default to 65432 for local testing.
    port = int(os.environ.get("PORT", 65432))
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # ADD THIS NEW LINE RIGHT HERE:
    # This tells Windows: "If this port is stuck, forcefully take it over!"
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    server_socket.bind(('0.0.0.0', port))
    server_socket.listen()
    
    print(f"Server is running and listening on port {port}...")

    while True:
        conn, addr = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(conn, addr))
        client_thread.daemon = True
        client_thread.start()

if __name__ == "__main__":
    start_server()
    