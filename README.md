# Jarvis AI Powered by OpenAI

## Overview

**Jarvis AI** is an intelligent assistant powered by OpenAI, designed to execute various tasks through voice commands. It integrates Python, Streamlit, and several other Python modules to provide a robust platform for automating tasks, opening applications, accessing websites, playing music, fetching weather updates, and more. The system leverages speech recognition to interact with the user and carry out commands efficiently.

## Features

- **Voice Command Execution**: Jarvis AI listens to user commands via speech recognition and performs actions accordingly.
- **Application Control**: Open and control various Windows applications such as Google Chrome, Visual Studio Code, Notepad, Paint, Microsoft Word, Excel, and more.
- **Web Browsing**: Open and navigate websites like YouTube, Wikipedia, and Google using voice commands.
- **Music Playback**: Play music from your local system by simply asking Jarvis to do so.
- **Weather Updates**: Fetch and read out the latest weather updates.
- **File Management**: Perform actions like writing, deleting, and managing text within applications like VS Code.
- **Custom AI Responses**: Interact with Jarvis through custom queries using OpenAI's GPT models.
- **Streamlit Integration**: A user-friendly web interface to interact with Jarvis AI.

## Tech Stack

- **Python**: Core language used for building the assistant.
- **OpenAI API**: Utilized for generating responses and interacting with the AI model.
- **Streamlit**: Provides a web-based interface for user interaction.
- **SpeechRecognition**: For capturing and processing voice commands.
- **PyAutoGUI & PyGetWindow**: For automating interactions with applications and windows.
- **Win32ComClient**: For voice output using the SAPI.SpVoice.
- **Subprocess**: To manage and open various applications in Windows.
- **WebBrowser**: For handling web-related commands like opening websites.
- **Requests**: For making API calls (e.g., fetching weather data).

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/jarvis-ai.git
   cd jarvis-ai
   ```

2. **Install the Required Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up OpenAI API Key**:
   - Replace `apikey` in the `config.py` file with your actual OpenAI API key.

4. **Run the Application**:
   - Run the main script:
     ```bash
     python jarvis.py
     ```
   - Alternatively, if using the Streamlit interface:
     ```bash
     streamlit run jarvis_streamlit.py
     ```

## Usage

- **Voice Commands**: Simply speak commands like "Open Chrome," "Play music," "What's the weather today?" and Jarvis will perform the action.
- **Application Interaction**: After opening an application, you can instruct Jarvis to write or delete text.
- **Web Interface**: Use the Streamlit web interface to interact with Jarvis in a more structured way.

## Customization

- **Adding New Commands**: You can extend Jarvis by adding new voice commands in the main Python script (`jarvis.py`). Simply define new functions and map them to voice commands.
- **Enhancing AI Responses**: Customize how Jarvis interacts with the OpenAI API by tweaking the parameters in the `chat()` function.

## Future Enhancements

- **Natural Language Processing (NLP)**: Improve understanding of more complex commands and conversations.
- **Integration with More APIs**: Expand functionality by integrating additional services (e.g., news updates, financial data).
- **Multi-Platform Support**: Extend compatibility to other operating systems like macOS and Linux.

## Contributing

Contributions are welcome! Feel free to submit issues, fork the repository, and create pull requests. Make sure to follow the contribution guidelines.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **OpenAI**: For providing the GPT models that power Jarvis AI.
- **Streamlit**: For the easy-to-use web interface.
- **Python Community**: For the open-source libraries that made this project possible.

---

With **Jarvis AI**, automation and interaction have never been this accessible and powerful. Get started today and let Jarvis make your life easier!
