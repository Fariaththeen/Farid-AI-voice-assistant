# 🎙️ Farid AI Voice Assistant

The **Farid AI Voice Assistant** is a real-time voice interaction system built using Android (Kotlin), [LiveKit](https://livekit.io), and optional backend tools in Python. It enables live audio communication, voice response generation, web search, weather reporting, and email functionality — ideal for both mobile and assistant-based projects.

---

## 🔧 Project Overview

This project contains:

- An **Android app** built with Kotlin and the **LiveKit SDK**
- Integration with **LiveKit Cloud Sandbox** for easy prototyping
- A **token retrieval mechanism** to securely connect to the server
- Optional **Python assistant tools** for extending functionality (e.g., search, email, weather)

---

## 📂 Project Structure

Farid-AI-voice-assistant/
├── android/ # Android client project
│ ├── MainActivity.kt # App entry point
│ ├── TokenExt.kt # Retrieves token using sandbox ID
│ └── ConnectionDetails.kt # Token + URL data model
│
├── farid_voice_assistant/ # Optional backend assistant tools (Python)
│ ├── agent.py # Launches assistant and starts session
│ ├── tools.py # Weather, email, search tools
│ ├── prompt.py # Agent instruction + response format
│ └── .env # Stores LiveKit credentials
│
├── README.md # Full documentation



---

## 🚀 Features

- 🎤 Real-time voice interaction via LiveKit
- 🔐 Secure token authentication using LiveKit Sandbox
- 🌐 DuckDuckGo-powered web search
- ⛅ Weather updates from wttr.in
- 📧 Email sending via Gmail (App Passwords)
- ⚙️ Easy modular extension for more tools

---

## 🛠 Technologies Used

| Layer              | Tool/Framework                     |
|--------------------|------------------------------------|
| Voice Platform     | [LiveKit](https://livekit.io) SDK |
| Mobile UI          | Kotlin + Android Studio            |
| Voice Agent Logic  | Python (optional)                  |
| Web Tools          | Requests, DuckDuckGo, SMTP         |
| Voice Interaction  | LiveKit Room Input + Assistant     |
| Token API          | LiveKit Cloud Sandbox              |

---

## ✅ Prerequisites

- Android Studio (latest version)
- Android Emulator or Physical Device
- Python 3.10+
- LiveKit Account (free) → https://cloud.livekit.io

---

## 📲 Android Setup (Client Side)

### 1. Open Android Project

```bash
cd Farid-AI-voice-assistant/android

2. Add Your Sandbox ID
Edit TokenExt.kt:

private const val sandboxID = "your-sandbox-id"
Get your sandbox ID from: https://cloud.livekit.io

3. Run the App
Connect a device or start an emulator

Click Run ▶️

The app will launch and connect using the token from LiveKit

1. Set Up Virtual Environment

cd Farid-AI-voice-assistant/farid_voice_assistant
python -m venv venv
.\venv\Scripts\activate  # or source venv/bin/activate (Linux/Mac)
pip install -r requirements.txt


2. Create a .env File

LIVEKIT_API_KEY=your_livekit_api_key
LIVEKIT_API_SECRET=your_livekit_api_secret
LIVEKIT_URL=wss://your-sandbox-id.sandbox.staging.livekit.io


3. Run the Agent Console (Optional)

python agent.py console
🌐 Web Tools Integrated
Tool	Usage
DuckDuckGo	Instant search results
wttr.in	Fetch city-based weather info
Gmail SMTP	Send emails via app passwords

🔐 Security Notes
Use App Passwords for Gmail, not your real password

Use .env to securely manage credentials

Sandbox tokens are temporary (testing only)

📷 Screenshots (Optional)

Include emulator screenshots, UI samples, or token server flow here.

🙋‍♂️ Author
Made with ❤️ by Fariaththeen (Farid)

📜 License
This project is licensed under the Apache 2.0 License
