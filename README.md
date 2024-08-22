# Jarvis AI Powered by OpenAI

## Project Overview

Jarvis AI is an intelligent voice-activated assistant powered by OpenAI's GPT-3.5. This project is built using Python and various libraries like `speech_recognition`, `pygetwindow`, `pyautogui`, and `subprocess` to provide an interactive experience. The assistant can perform a range of tasks including opening applications, browsing websites, playing music, fetching weather information, retrieving news, and interacting with users through natural language processing. Additionally, it leverages Streamlit to provide a user-friendly web interface.

## Features

- **Voice Commands**: Perform actions using voice commands, such as opening applications, writing or deleting text in applications like VS Code, and more.
- **Application Control**: Open and control applications like Chrome, Visual Studio Code, Notepad, Paint, MS Word, MS Excel, and Control Panel.
- **Web Browsing**: Open websites using voice commands.
- **Play Music**: Play your favorite songs through voice commands.
- **Weather Information**: Get the latest weather updates.
- **News Updates**: Fetch the latest news using voice commands.
- **Streamlit Interface**: A web-based interface powered by Streamlit for easy interaction.

## Technologies Used

- **Python**: The core language used to develop the assistant.
- **OpenAI GPT-3.5**: Provides the natural language processing capabilities.
- **SpeechRecognition**: Used to capture and recognize voice commands.
- **pygetwindow**: Manages application windows, allowing focus and control of different applications.
- **pyautogui**: Automates keyboard and mouse actions to perform tasks in different applications.
- **subprocess**: Used to open and manage external applications.
- **Streamlit**: Provides a web-based user interface for interacting with Jarvis AI.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/jarvis-ai.git
   cd jarvis-ai
   ```

2. **Install Dependencies**:
   Ensure you have Python installed (preferably 3.8 or above). Then install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up OpenAI API Key**:
   - Obtain an API key from [OpenAI](https://beta.openai.com/signup/).
   - Store the API key in a configuration file (`config.py`):
     ```python
     apikey = "your_openai_api_key"
     ```

4. **Run the Application**:
   Start the voice assistant with:
   ```bash
   python jarvis.py
   ```

5. **Run the Streamlit Interface**:
   If you want to use the Streamlit web interface, run:
   ```bash
   streamlit run app.py
   ```

## Usage

### Voice Commands

- **Open Applications**:
  - "Open Chrome"
  - "Open Visual Studio Code"
  - "Open Notepad"
  - "Open Paint"
  - "Open MS Word"
  - "Open MS Excel"
  - "Open Control Panel"

- **Web Browsing**:
  - "Open YouTube"
  - "Open Google"
  - "Open Wikipedia"

- **Music**:
  - "Play music"
  - "Stop music"

- **Weather**:
  - "What's the weather today?"

- **News**:
  - "Tell me the latest news"

- **Text Operations**:
  - "Write [text]"
  - "Delete"

### Streamlit Interface

- **Launch Streamlit Interface**: Use the command `streamlit run app.py` to start the web interface.
- **Interact**: Use the Streamlit interface to perform all the above actions through a web-based UI.

## Contributing

Contributions are welcome! If you'd like to contribute, please fork the repository and make changes as you'd like. Pull requests are warmly welcome.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

- [OpenAI](https://www.openai.com/) for providing the GPT-3.5 model.
- The Python community for providing the necessary libraries to make this project possible.
- [Streamlit](https://www.streamlit.io/) for offering a simple and effective way to create interactive web applications.

---

Feel free to customize this README further based on your project's specific details and requirements.
