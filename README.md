# Elementarz

This is a prototype for a learn-to-read application.

The idea is to present increasingly harder words for the pupil to read, and use speech recognition to verify if the pupil can read the word.

This is designed as a throw-away prototype, as python-based applications are hard to move around.

The Google-Cloud based speech recognition works pretty well for adult speech. It doesn't work that great with a child speaking.

```
python -m venv env
.\env\Scripts\activate

pip install google-api-python-client
pip install google-cloud-speech
pip install pyaudio
```

For Windows-based development you will need Visual C++ to install pyaudio. See https://stackoverflow.com/questions/52283840/i-cant-install-pyaudio-on-windows-how-to-solve-error-microsoft-visual-c-14