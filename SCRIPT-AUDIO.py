import os
from pydub import AudioSegment
import speech_recognition as sr
# Asegurarse de que Pydub y SpeechRecognition están instalados
# Puedes instalarlo con pip si no lo tienes:

# Setear variables de entorno ANTES de usar Pydub
os.environ["PATH"] += os.pathsep + r"C:\Users\GAMER\Downloads\ffmpeg-7.1.1\bin"


# También forzamos las rutas directamente por seguridad
AudioSegment.converter = r"C:\Users\GAMER\Downloads\ffmpeg-7.1.1\bin\ffmpeg.exe"
AudioSegment.ffprobe = r"C:\Users\GAMER\Downloads\ffmpeg-7.1.1\bin\ffprobe.exe"

print("✅ FFMPEG y FFPROBE están listos.")

# Ruta del archivo MP3 original
audio_mp3 = "ARCHIVO ORIGINAL.mp3"
# Convertir MP3 a WAV mono 16kHz
audio = AudioSegment.from_mp3(audio_mp3)
audio = audio.set_channels(1).set_frame_rate(16000)

# Dividir en fragmentos de 60 segundos
chunk_length_ms = 60 * 1000
chunks = [audio[i:i + chunk_length_ms] for i in range(0, len(audio), chunk_length_ms)]

recognizer = sr.Recognizer()
transcripcion_total = ""

for i, chunk in enumerate(chunks):
    chunk_filename = f"chunk_{i}.wav"
    chunk.export(chunk_filename, format="wav")
    
    with sr.AudioFile(chunk_filename) as source:
        print(f"🎧 Transcribiendo fragmento {i + 1}/{len(chunks)}...")
        audio_data = recognizer.record(source)
        try:
            texto = recognizer.recognize_google(audio_data, language="es-ES")
            transcripcion_total += texto + "\n"
        except sr.UnknownValueError:
            transcripcion_total += "[Incomprensible]\n"
        except sr.RequestError as e:
            print(f"❌ Error del servicio: {e}")
            break

# Guardar la transcripción completa
with open("transcripcion.txt", "w", encoding="utf-8") as f:
    f.write(transcripcion_total)

print("✅ Transcripción final guardada en 'transcripcion.txt'")


