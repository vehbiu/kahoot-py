# kahoot-py
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Open Source](https://img.shields.io/badge/Open_Source-green?style=for-the-badge&logo=opensource&logoColor=white)
![MIT License](https://img.shields.io/badge/License-GNU-yellow.svg?style=for-the-badge)

KahootPy is a Python client for interacting with the Kahoot API, allowing you to join games, send responses, and handle events in real-time.

## 🌟 Features
- **Join Games**: Quickly join Kahoot games using game PINs.
- **Event Handling**: Register handlers for various game events such as questions and game status updates.
- **Real-Time Communication**: Utilize WebSocket connections for real-time interaction with the Kahoot server.
- **User-Friendly**: Simple interface for sending packets and handling game events.

## 🚀 Quick Start
1. Install the package via pip:
   ```bash
   pip install kahoot
   ```

2. Import and use KahootPy in your Python script:
   ```python
   from kahoot import KahootClient
   ```

## 🛠️ Example Usage
Here's a basic example of how to use the KahootClient:

```python
import asyncio
from kahoot import KahootClient

async def main():
    client = KahootClient()
    # add handlers before joining the game
    client.on('question_start', lambda question: print(f"qsPacket: {question}"))
    await client.join_game(game_pin=123456, username='your_username')

# Run the main function
asyncio.run(main())
```

### 🎉 Event Handlers
- **Joining a Game**: Use the `join_game` method to join a game with a specific PIN and username.
- **Listening for Events**: Register handlers for various events (e.g., questions, game status) using the `on` method.

## 📁 Project Structure
```
kahoot/
├── __init__.py       # Package initialization
├── packets/          # Packet definitions and implementations
├── util/             # Utility functions (e.g., challenge solver, logger)
├── exceptions.py      # Custom exceptions
├── constants.py      # Constant values (e.g., USER_AGENT)
└── README.md         # Documentation
```

## ⚙️ Technical Details
- Built using `httpx` for HTTP requests and `aiocometd` for WebSocket communication.
- Utilizes asynchronous programming with Python's `asyncio` for efficient real-time interaction.
- Modular design with separate packet handling and utility functions for easy maintenance.

## 📝 License
This project is licensed under the GNU GPLv3 License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing
Contributions are welcome! Feel free to:
- Open issues
- Submit pull requests
- Suggest new features or improvements

## 👤 Author
**Vehbi**
- GitHub: [@vehbiu](https://github.com/vehbiu)

## 🔒 Responsible Use
This tool is intended for educational and personal use only. Users must ensure compliance with Kahoot's terms of service and applicable laws.

## 🙏 Acknowledgments
- Inspired by the need for real-time interaction with Kahoot's educational games.

## 📊 Stats
![GitHub stars](https://img.shields.io/github/stars/vehbiu/kahoot-py?style=social)
![GitHub forks](https://img.shields.io/github/forks/vehbiu/kahoot-py?style=social)

---
Made with ❤️ by [@vehbiu](https://github.com/vehbiu)