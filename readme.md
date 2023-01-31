# Checkbox Music

This project is a beat maker that allows users to create their own beats and export it as MP3. It is built using Python, PyQt5 and Pydub.
Features

- Create beat by selecting checkboxes
- Save beat pattern to a file
- Load beat pattern from a file
- Play beat
- Export beat as MP3

## Requirements

- Python 3.x
- PyQt5
- Pydub
- pickle

## Usage

1. Clone the repository

`git clone https://github.com/<username>/checkbox-music.git`

2. Navigate to the project folder

`cd checkbox-music`

3. Run the program

`python beatmaker.py`

## File Description

- beatmaker.py - main script to run the program
- kick.wav, snare.wav, clap.wav, hihat.wav - audio samples used in the beat

## Limitations

- Only 4 sounds are available for creating the beat
- Beat pattern can only be saved as a pickle file and loaded as a pickle file
- MP3 export is currently not implemented, only the function is available.s