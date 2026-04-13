# 💬 Real-Time Terminal Chat Application (Python)

A multi-user, real-time chat application built using Python sockets and threading. This project demonstrates client-server architecture, concurrent communication, and clean terminal-based interaction.

---

## 🚀 Features

- Real-time messaging between multiple users  
- Client-server architecture using sockets  
- Multi-threaded communication handling  
- Clean terminal interface with user prompts  
- Timestamped messages  
- Graceful exit functionality (`/exit`)  
- Lightweight and easy to run  

---

## 🧠 Concepts Used

- Socket Programming  
- TCP/IP Communication  
- Multi-threading  
- Synchronization (thread-safe printing)  
- Client-Server Model  

---

## 🛠️ Tech Stack

- Language: Python 3  
- Libraries:  
  - socket  
  - threading  
  - sys  
  - time  

---

## 📂 Project Structure

```
chat-application/
│
├── server.py       # Handles connections and message broadcasting
├── client.py       # Terminal-based chat client
└── README.md       # Project documentation
```

---

## ⚙️ Setup & Installation

1. Clone the repository:
```
git clone https://github.com/your-username/chat-application.git
cd chat-application
```

2. Make sure Python is installed:
```
python --version
```

---

## ▶️ How to Run

### Step 1: Start Server
```
python server.py
```

### Step 2: Run Clients (in separate terminals)
```
python client.py
```

Run multiple clients in different terminals to simulate multiple users.

---

## 💬 Usage

- Enter your username when prompted  
- Start sending messages  
- Messages are broadcast to all connected users  
- Type `/exit` to leave the chat  

---

## 🧪 Example

```
[14:32:10] Jeevan: Hello
[14:32:15] Rahul: Hi!
```

---

## 🔥 Future Enhancements

- Private messaging  
- User authentication  
- GUI version (Tkinter / Web-based)  
- Message persistence (database)  
- File sharing  
- Emoji support  

---

## 📌 Learning Outcome

This project helps in understanding how real-time systems like messaging apps work internally, including handling multiple users and maintaining communication between them.

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repository and submit a pull request.

---

## 📄 License

This project is open-source and available under the MIT License.

---

## 👨‍💻 Author

**V. Jeevan Naidu**  
Python Developer | Student | Tech Enthusiast  

---

⭐ If you found this project useful, consider giving it a star!
