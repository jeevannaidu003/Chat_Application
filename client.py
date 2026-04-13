import socket
import threading
import sys
import time

server_host = "127.0.0.1"
server_port = 5555

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect((server_host, server_port))

username = input("Enter your username: ").strip()

lock = threading.Lock()
running = True

def clear_line():
    sys.stdout.write("\r" + " " * 100 + "\r")
    sys.stdout.flush()

def print_message(message):
    with lock:
        clear_line()
        print(message)
        print(f"{username}> ", end="", flush=True)

def receive_handler():
    global running
    while running:
        try:
            message = connection.recv(1024).decode()
            if not message:
                break
            if message == "USERNAME":
                connection.send(username.encode())
            else:
                print_message(message)
        except:
            running = False
            break

def send_handler():
    global running
    print(f"{username}> ", end="", flush=True)
    while running:
        try:
            message = sys.stdin.readline().strip()
            if message.lower() == "/exit":
                running = False
                connection.close()
                print("\nDisconnected from chat")
                break
            if message:
                timestamp = time.strftime("%H:%M:%S")
                formatted_message = f"[{timestamp}] {username}: {message}"
                connection.send(formatted_message.encode())
                print(f"{username}> ", end="", flush=True)
        except:
            running = False
            break

def start_chat():
    receiver_thread = threading.Thread(target=receive_handler, daemon=True)
    sender_thread = threading.Thread(target=send_handler)

    receiver_thread.start()
    sender_thread.start()

    sender_thread.join()

start_chat()