import datetime
import webbrowser
import os
import requests
import speech_recognition as sr
import win32com.client
from openai import OpenAI
from config import apikey
import streamlit as st

speaker = win32com.client.Dispatch("SAPI.SpVoice")
client = OpenAI(api_key=apikey)
Chatstr = ""

st.title("JARVIS The AI 🤖")
with st.chat_message(name="Jarvis", avatar="🤖"):
    st.write("Hello, I'm your personal assistant. How can I help you today?")
    st.write("Feel Free To Speak...")
def chat_assistant(query):
    with st.chat_message(name="User", avatar="🧑🏻‍💻"):
        st.write(query)
def chat_user(response):
    with st.chat_message(name="Jarvis", avatar="🤖"):
        st.write(response)

def open_app(query1):
    query1 = query1.lower()
    if "vs code".lower() in query1:
        os.system("start code")
        speaker.speak("Opening Visual Studio Code")
    elif "Chrome".lower() in query1:
        os.system("start chrome")
        speaker.speak("Opening Chrome")
    elif "Firefox".lower() in query1:
        os.system("start firefox")
        speaker.speak("Opening Firefox")
    elif "paint".lower() in query1:
        os.system("start mspaint")
        speaker.speak("Opening Paint")
    elif "notepad".lower() in query1:
        os.system("start notepad")
        speaker.speak("Opening Notepad")
    elif "winword".lower() in query1:
        os.system("start winword")
        speaker.speak("Opening Microsoft Word")
    elif "excel".lower() in query1:
        os.system("start excel")
        speaker.speak("Opening Microsoft Excel")
    elif "wordpad".lower() in query1:
        os.system("start wordpad")
        speaker.speak("Opening Microsoft Wordpad")
    elif "calculator".lower() in query1:
        os.system("start calc")
        speaker.speak("Opening Calculator")
    elif "control panel".lower() in query1:
        os.system("start control panel")
        speaker.speak("Opening Control Panel")
    else:
        speaker.speak("Sorry, I couldn't find an app to open.")

def get_news(api_key):
    base_url = "https://newsapi.org/v2/top-headlines"
    params = {
        "apiKey": api_key,
        "country": "in",  # Change country code as per your preference
        "pageSize": 5  # Number of articles to fetch
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    if data["status"] == "ok":
        articles = data["articles"]
        news_info = ""
        for article in articles:
            title = article["title"]
            news_info += title + ". "
        return news_info
    else:
        return "Sorry, couldn't fetch news articles."

def get_weather(city):
    api_key = "2ba7f635f8160203761324896267196c"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"
    response = requests.get(complete_url)
    data = response.json()
    if data["cod"] == 200:
        weather_description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        return f"The weather in {city} is {weather_description}. Temperature: {temperature}°C. Humidity: {humidity}%. Wind Speed: {wind_speed} m/s."
    else:
        return "Sorry, couldn't fetch weather information."
    chat_user(response.choices[0].message.content)

def chat(query1):
    global Chatstr
    print(Chatstr)
    Chatstr += f"KRRISH: {query1}\n Jarvis: "
    message = [[{"role": "user", "content": query1}]]
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=message[0],
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a  try catch block
    speaker.speak(response.choices[0].message.content)
    Chatstr += f"{response.choices[0].message.content}\n"
    if "exit".lower() in query1:
        exit()
    chat_user(response.choices[0].message.content)
    return response.choices[0].message.content

def ai(prompt):
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"
    client = OpenAI(api_key=apikey)
    message = [[{"role": "user", "content": prompt}]]
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=message[0],
        temperature=2,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a  try catch block
    print(response.choices[0].message.content)
    text += response.choices[0].message.content
    chat_user(response.choices[0].message.content)
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    with open(f"Openai/{''.join(prompt.split('ai')[1:])}.txt", "w", encoding='UTF-8') as f:
        f.write(text)

def open_website(url):
    """Function Opening Websites."""
    try:
        webbrowser.open(f"www.{url}.com")
        print(f"Opening {url}...")
        speaker.speak(f"Opening {url}...")
    except Exception as e:
        print(f"Error opening website: {e}")
        speaker.speak(f"Error opening website: {e}")

def take_command():
    # Initialize recognizer
    recognizer = sr.Recognizer()
    # Initialize microphone as audio source
    microphone = sr.Microphone()
    # Capture audio from the microphone
    with microphone as source:
        recognizer.pause_threshold = 1  # Adjust this value as per your preference
        print("listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source, timeout=5)

        try:
            print("Recognizing...")
            # Recognize speech using Google Speech Recognition
            command = recognizer.recognize_google(audio, language="en-IN")
            print(f"User said: {command}")
            return command

        except sr.UnknownValueError:
            print("Sorry, I didn't understand that.")
            command = None
            return command
        except sr.RequestError as e:
            print(f"Sorry, there was an error: {e}")
            command = None
            return command
        except Exception as e:
            print(f"Sorry From JarvisAI : error {e}")
            command = None
            return command
        except Exception as e:
            print(f"Time Out : Have A Good Day")
            command = None
            return command


def Call_Jarvis():
    print("...Hello I am JARVIS an Artificial Intelligence BOT")
    speaker.Speak("...Hello I am JARVIS an Artificial Intelligence BOT")
    while True:
        query = take_command()
        chat_assistant(query)
        # To quit from Jarvis------------------------------------------------
        if " open application".lower() in query:
            open_app(query)
        #  To open websites-----------------------------------------------------
        elif "open website".lower() in query:
            q = query.split()
            website = q[-1]
            open_website(website)
        # To open music from directory------------------------------------------
        elif "play music".lower() in query:
            MusicPath = "C:/Users/Krrish Jaiswal/Music/Faviourite/Brown Rang  Yo Yo Honey Singh.mp3"
            os.startfile(MusicPath)
        # To get the time--------------------------------------------------------
        elif "time".lower() in query:
            strftTime = datetime.datetime.now().strftime("%H:%M:%S")
            speaker.Speak(f"...sir the time is {strftTime}")
        # To get query from chatgpt---------------------------------------------
        elif "using AI".lower() in query:
            ai(prompt=query)
        # To get weather info----------------------------------------------------
        elif "weather".lower() in query:
            # Extract the city from the query
            words = query.split()
            if "in" in words:
                index = words.index("in")
                city = " ".join(words[index + 1:])
                # Get weather details for the specified City
                weather_info = get_weather(city)
                speaker.speak(weather_info)
                print(weather_info)
            else:
                speaker.speak("Please specify the city name.")
                print("Please specify the city name.")
        # To get news info------------------------------------------------------
        elif "news".lower() in query:
            # Get latest news articles
            news_info = get_news("5bb939b515e6406fbc163de159ab3b5b")
            speaker.speak("Here are the latest news headlines.")
            print("Here are the latest news headlines:")
            print(news_info)
            speaker.speak(news_info)
        # To reset chat info------------------------------------------------------
        elif "reset chat".lower() in query:
            Chatstr = ""
        else:
            chat(query)


Call_Jarvis()
