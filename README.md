# NihonKnow :jp:
A tool for practicing Japanese pronunciation using the SpeechRecognition and pygame Python libraries.

NihonKnow uses speech recognition to compare a learner's spoken Japanese against expected answers, allowing multiple valid Japanese representations (hiragana, katakana, and kanji).

## Why?
I've been learning Japanese since 2024. I felt it would be good to have a practice tool that is free and open.

## Features

### Current:
* Japanese speech recognition and audio playback
* Answer checking with multiple accepted responses
* Supports hirigana, katakana, and kanji
* Word and phrase practice banks

<!-- ### Planned:
* Lesson-based practice
* Progress tracking
* Pop culture (namely anime and manga) references for immersion learning
* Spaced repeition
* More advanced speech analysis -->

# Requirements
* Python 3.13
* A working microphone
* Internet connection

Python 3.14 not currently supported due to issues with libraries.

# Installation
## 1. Clone the repo
`git clone <repository-url>`
`cd nihonknow`

## 2. Create a virtual environment
Make sure Python 3.13 is installed.

Windows:
`py -3.13 -m venv .venv`

Activate the environment:
`.\.venv\Scripts\activate`

## 3. Install dependencies
`pip install -r requirements.txt`

# Generate Audio Files

For the moment, NihonKnow stores generated Japanese audio locally instead of creating new audio every time the program runs. Remember that this is just a small project for now.

Run:

python generate_audio.py

This will create:

audio/
├── words/
│   ├── cat.mp3
│   ├── dog.mp3
│
└── phrases/
    ├── hello.mp3

# Adding New Words

Add entries to data.py.

Example:

{
    "id": "mountain",
    "japanese": "山",
    "english": "Mountain",
    "audio": "audio/words/mountain.mp3",
    "accepted": [
        "山",
        "やま",
        "ヤマ"
    ]
}

Then regenerate audio:

python generate_audio.py