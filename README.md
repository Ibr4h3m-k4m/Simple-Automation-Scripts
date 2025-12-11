# 🤖 Simple Automation Scripts

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/Ibr4h3m-k4m/Simple-Automation-Scripts/graphs/commit-activity)

> A collection of practical Python automation scripts to streamline everyday tasks and boost productivity

## 📋 Table of Contents

- [Overview](#overview)
- [Scripts](#scripts)
- [Installation](#installation)
- [Usage](#usage)
- [Requirements](#requirements)
- [Contributing](#contributing)

## 🎯 Overview

This repository contains a curated collection of simple yet powerful Python automation scripts designed to automate repetitive tasks and improve workflow efficiency. Each script is self-contained, well-documented, and easy to use.

**Perfect for:**
- Developers looking to automate daily tasks
- Python learners exploring practical applications
- Anyone wanting to save time on repetitive operations

## 📜 Scripts

### 1. 📋 Multi-Clipboard Manager (`multiclipboard.py`)

A powerful clipboard manager that allows you to save, retrieve, and manage multiple clipboard entries with ease.

**Features:**
- Save unlimited clipboard entries with custom keys
- Quick retrieval of saved clips
- List all saved entries
- Delete unwanted clips
- Persistent storage using JSON

**Usage:**
```bash
# Save current clipboard with a key
python multiclipboard.py save <key>

# Load a saved clip to clipboard
python multiclipboard.py load <key>

# List all saved clips
python multiclipboard.py list

# Delete a saved clip
python multiclipboard.py delete <key>
```

**Example Workflow:**
```bash
# Copy some text, then save it
python multiclipboard.py save email_signature

# Later, load it back
python multiclipboard.py load email_signature

# View all saved clips
python multiclipboard.py list
```

**Use Cases:**
- Save frequently used code snippets
- Store email templates
- Keep command-line commands handy
- Manage multiple passwords temporarily
- Quick access to formatted text

---

### 2. 🌤️ Weather Fetcher (`weather.py`)

Get real-time weather information for any city directly from your command line.

**Features:**
- Current weather conditions
- Temperature (with Celsius/Fahrenheit options)
- Humidity levels
- Weather descriptions
- Simple and fast API integration

**Usage:**
```bash
# Get weather for a specific city
python weather.py "London"

# Get weather for your current location
python weather.py "New York"

# Try different cities
python weather.py "Tokyo"
python weather.py "Paris"
```

**Example Output:**
```
Weather in London:
Temperature: 15°C
Condition: Partly cloudy
Humidity: 72%
```

**Use Cases:**
- Quick weather checks before commuting
- Travel planning
- Integration into morning routine scripts
- Weather-based automation triggers

---

## 🚀 Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Quick Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Ibr4h3m-k4m/Simple-Automation-Scripts.git
   cd Simple-Automation-Scripts
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

   If `requirements.txt` doesn't exist, install manually:
   ```bash
   pip install pyperclip requests
   ```

3. **Verify installation**
   ```bash
   python multiclipboard.py list
   python weather.py "London"
   ```

### Platform-Specific Notes

**Linux:**
```bash
# May need to install xclip or xsel for clipboard access
sudo apt-get install xclip  # Ubuntu/Debian
```

**Windows:**
- No additional dependencies needed for clipboard operations

## 💻 Usage

### General Command Format

Each script follows a simple command-line interface:

```bash
python <script_name>.py <command> [arguments]
```

### Multi-Clipboard Manager

```bash
# Basic operations
python multiclipboard.py save meeting_notes
python multiclipboard.py load meeting_notes
python multiclipboard.py list
python multiclipboard.py delete old_note

# Pro tip: Create aliases for faster access
alias mcs='python /path/to/multiclipboard.py save'
alias mcl='python /path/to/multiclipboard.py load'
```

### Weather Fetcher

```bash
# Single city
python weather.py "Berlin"

# With error handling
python weather.py "NonExistentCity"  # Graceful error message

# Integration example: Check weather every morning
python weather.py "$(curl -s ipinfo.io/city)"
```

## 📦 Requirements

### Core Dependencies

```
pyperclip>=1.8.2    # Clipboard operations
requests>=2.28.0    # HTTP requests for weather API
```

### Optional Dependencies

```
colorama>=0.4.6     # Colored terminal output (optional enhancement)
python-dotenv>=0.19.0  # Environment variable management (if API keys needed)
```

### Creating requirements.txt

```bash
pip freeze > requirements.txt
```

## 🛠️ Configuration

### Weather Script Configuration

For the weather script, you may need an API key from OpenWeatherMap:

1. Sign up at [OpenWeatherMap](https://openweathermap.org/api)
2. Get your free API key
3. Create a `.env` file:
   ```
   WEATHER_API_KEY=your_api_key_here
   ```

### Clipboard Data Storage

The multi-clipboard manager stores data in `clipboard.json` in the same directory. You can:

- **Backup:** Copy `clipboard.json` to backup your clips
- **Sync:** Use cloud storage to sync across devices
- **Reset:** Delete `clipboard.json` to start fresh

## 🔧 Advanced Usage

### Creating System-Wide Commands

**Linux:**

Add to your `~/.bashrc` or `~/.zshrc`:

```bash
# Multi-clipboard aliases
alias mcs='python ~/Simple-Automation-Scripts/multiclipboard.py save'
alias mcl='python ~/Simple-Automation-Scripts/multiclipboard.py load'
alias mclist='python ~/Simple-Automation-Scripts/multiclipboard.py list'

# Weather alias
alias weather='python ~/Simple-Automation-Scripts/weather.py'
```

**Windows:**

Create batch files in a directory in your PATH:

```batch
@echo off
python C:\path\to\multiclipboard.py %*
```

### Integration with Other Tools

**Task Scheduler (Windows):**
- Schedule weather checks at specific times
- Automate clipboard backups

**Cron Jobs (Linux):**
```bash
# Add to crontab
0 8 * * * python /path/to/weather.py "$(curl -s ipinfo.io/city)" | mail -s "Morning Weather" user@example.com
```

## 📊 Script Details

### Multi-Clipboard Manager

**File Structure:**
```
multiclipboard.py       # Main script
clipboard.json          # Storage file (auto-generated)
```

**Storage Format:**
```json
{
  "email_signature": "Best regards,\nJohn Doe",
  "api_key": "abc123xyz789",
  "code_snippet": "def hello():\n    print('Hello')"
}
```

### Weather Fetcher

**Supported Information:**
- Current temperature
- Weather condition
- Humidity
- Wind speed (can be added)
- Forecast (extendable)


### Script Guidelines

When contributing new scripts:

- ✅ Keep it simple and focused
- ✅ Add proper error handling
- ✅ Include usage examples
- ✅ Document dependencies
- ✅ Use command-line arguments
- ✅ Add comments for complex logic

### Ideas for New Scripts

Looking for inspiration? Here are some ideas:

- 📧 Email automation script
- 📁 File organizer by type/date
- 🔄 Batch file renamer
- 📸 Screenshot organizer
- 🗜️ Bulk file compressor
- 📝 Text file merger
- 🌐 Website availability checker
- 📊 CSV data processor
- 🔐 Password generator
- ⏰ Reminder system

## 🐛 Troubleshooting

### Common Issues

**Clipboard not working:**
```bash
# Linux
sudo apt-get install xclip xsel


**Module not found:**
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

**Permission denied:**
```bash
chmod +x multiclipboard.py weather.py
```

**Weather API errors:**
- Check your API key
- Verify internet connection
- Confirm city name spelling

## 📝 To-Do

- [ ] Add more automation scripts
- [ ] Create GUI versions
- [ ] Web interface option
- [ ] Documentation website


## 👤 Author

**Ibrahim Kamraoui**

- GitHub: [@Ibr4h3m-k4m](https://github.com/Ibr4h3m-k4m)
- Project: [Simple-Automation-Scripts](https://github.com/Ibr4h3m-k4m/Simple-Automation-Scripts)

## 🌟 Show Your Support

If these scripts helped you, please consider:

- ⭐ Starring this repository
- 🐛 Reporting bugs
- 💡 Suggesting new features
- 🔀 Contributing your own scripts

## 📚 Resources

- [Python Official Documentation](https://docs.python.org/3/)
- [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/)
- [Python Automation Cookbook](https://www.packtpub.com/product/python-automation-cookbook)

## 🎓 Learning Path

**Beginner:**
1. Start with `weather.py` - understand API calls
2. Try `multiclipboard.py` - learn file I/O and JSON
3. Modify scripts for your needs

**Intermediate:**
4. Add new features to existing scripts
5. Create your own automation script
6. Combine multiple scripts into workflows

**Advanced:**
7. Build a script orchestrator
8. Create a CLI tool with argparse
9. Package scripts for distribution

---

## 🏆 Changelog

### v1.0.0 (Initial Release)
- ✨ Multi-clipboard manager
- ✨ Weather fetcher
- 📝 Initial documentation

---

*Automating the boring stuff, one script at a time!*


