# A.D.A V2 - Advanced Design Assistant

![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.11-blue?logo=python)
![React](https://img.shields.io/badge/React-18.2-61DAFB?logo=react)
![Electron](https://img.shields.io/badge/Electron-28-47848F?logo=electron)
![Gemini](https://img.shields.io/badge/Google%20Gemini-Native%20Audio-4285F4?logo=google)
![License](https://img.shields.io/badge/License-MIT-green)

> **A.D.A** = **A**dvanced **D**esign **A**ssistant

ADA V2 is a sophisticated AI assistant with voice conversation, computer vision,
gesture control, and browser automation — all in a desktop app.

---

## 🚀 Super Simple Setup Guide (Anyone Can Do This!)

### What You Need First

Think of these as the "ingredients" before cooking:

| Tool            | What It Does       | Download Link                                                        |
| --------------- | ------------------ | -------------------------------------------------------------------- |
| **Python 3.11** | Runs the AI brain  | [Download Miniconda](https://docs.conda.io/en/latest/miniconda.html) |
| **Node.js 18+** | Runs the interface | [Download Node.js](https://nodejs.org/) (Choose LTS)                 |
| **Git**         | Downloads the code | [Download Git](https://git-scm.com/download/win)                     |
| **VS Code**     | Where you work     | [Download VS Code](https://code.visualstudio.com/)                   |

---

### Step 1: Install the Tools

1. **Miniconda** – Download, run installer, ✅ **check "Add Anaconda to my
   PATH"**
2. **Node.js** – Download the LTS version, run installer, click Next → Next →
   Finish
3. **Git** – Download, run installer, keep clicking Next → Finish
4. **VS Code** – Download, install, done!

> ⚠️ **Important**: Restart your computer after installing these tools!

---

### Step 2: Get the Code

1. Open **Command Prompt** (Press `Win + R`, type `cmd`, hit Enter)
2. Type this and press Enter:
   ```bash
   git clone https://github.com/nazirlouis/ada_v2.git
   ```
3. A folder called `ada_v2` is now on your computer!

---

### Step 3: Open in VS Code

1. Open VS Code
2. Click **File → Open Folder**
3. Find and select the `ada_v2` folder
4. Press **Ctrl + `** (the key below Escape) to open the built-in terminal

---

### Step 4: Set Up Python Environment

Run these commands **ONE BY ONE** in the VS Code terminal:

```bash
# Create a safe space for the project
conda create -n ada_v2 python=3.11 -y
```

```bash
# Enter that safe space
conda activate ada_v2
```

```bash
# Install all the Python tools needed
pip install -r requirements.txt
```

```bash
# Install the web browser for automation
playwright install chromium
```

---

### Step 5: Set Up the Frontend

```bash
npm install
```

_(This downloads all the interface parts — may take a few minutes)_

---

### Step 6: Create Your Secret Key File

1. In VS Code, **right-click** on the file explorer panel → **New File**
2. Name it exactly: `.env` (yes, starting with a dot)
3. Paste this inside:
   ```
   GEMINI_API_KEY=your_key_here
   ```
4. **Get your free key:**
   - Go to [Google AI Studio](https://aistudio.google.com/app/apikey)
   - Sign in with Google
   - Click **"Create API Key"**
   - Copy the key and replace `your_key_here` with it
5. Save the file (**Ctrl + S**)

---

### Step 7: RUN IT! 🎉

```bash
conda activate ada_v2
npm run dev
```

**The app will open!** Say "Hello Ada" to test if voice works.

---

## 📋 Quick Reference Card

| What              | Command                                    |
| ----------------- | ------------------------------------------ |
| **Start the app** | `conda activate ada_v2` then `npm run dev` |
| **Stop the app**  | Press `Ctrl + C` in the terminal           |

---

## ❓ Common Problems & Fixes

| Problem                      | Solution                                                                    |
| ---------------------------- | --------------------------------------------------------------------------- |
| `conda is not recognized`    | Restart your computer after installing Miniconda                            |
| `npm is not recognized`      | Restart your computer after installing Node.js                              |
| App says "API key not found" | Make sure `.env` file is in the main `ada_v2` folder, not inside `backend/` |
| Camera not working           | Allow camera access when asked                                              |
| WebSocket connection errors  | Just reconnect — say "Hello Ada" again                                      |

---

## 🌟 What ADA Can Do

| Feature                | Description                             |
| ---------------------- | --------------------------------------- |
| 🗣️ **Voice Chat**      | Talk naturally with real-time responses |
| 👁️ **Face Auth**       | Secure login with your face             |
| 🖐️ **Gesture Control** | Control windows with hand movements     |
| 🌐 **Web Automation**  | Let ADA browse the web for you          |
| 📁 **Project Memory**  | Remembers your conversations            |

### Gesture Controls

| Gesture          | Action        |
| ---------------- | ------------- |
| 🤏 **Pinch**     | Click/confirm |
| ✋ **Open Palm** | Release       |
| ✊ **Fist**      | Grab and drag |

---

## 📂 Project Structure

```
ada_v2/
├── backend/           # Python AI brain
│   ├── ada.py         # Gemini AI integration
│   ├── server.py      # Main server
│   └── ...
├── src/               # React interface
├── electron/          # Desktop app wrapper
├── .env               # Your secret API key (create this!)
├── requirements.txt   # Python dependencies
└── package.json       # Node.js dependencies
```

---

## ⚙️ For Developers

<details>
<summary>Click for advanced setup options</summary>

### Two-Terminal Setup (See Python Logs)

**Terminal 1 (Backend):**

```bash
conda activate ada_v2
python backend/server.py
```

**Terminal 2 (Frontend):**

```bash
npm run dev
```

### Face Authentication Setup

1. Take a clear photo of your face
2. Rename it to `reference.jpg`
3. Put it in the `backend/` folder

### Configuration (`settings.json`)

| Key                              | Description                          |
| -------------------------------- | ------------------------------------ |
| `face_auth_enabled`              | Enable/disable face login            |
| `tool_permissions.generate_cad`  | Require confirmation for CAD         |
| `tool_permissions.run_web_agent` | Require confirmation for browser     |
| `tool_permissions.write_file`    | Require confirmation for file writes |

</details>

---

## 🔒 Security

- API keys are stored locally in `.env` — never commit this file!
- Face data is processed locally — never uploaded
- All project data stays on your machine

> ⚠️ **Never share your `.env` file or `reference.jpg`**

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

---

<p align="center">
  <strong>Built with 🤖 by Nazir Louis</strong><br>
  <em>Bridging AI, Vision, and Voice in a Single Interface</em>
</p>
