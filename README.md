# Audio to Text Transcriber

Simple Python script that uses OpenAI's Whisper model to transcribe audio files into Spanish text.

## Description

This project converts an audio file into a `.txt` file using the Whisper base model.

## Installation

```bash
pip install openai-whisper
```

FFmpeg must be installed.

## Usage

Modify:

```python
result = model.transcribe("FILE_NAME_OR_PATH", language="es")
```

Run:

```bash
python script_name.py
```

The output will be saved as `transcripcion.txt`.
