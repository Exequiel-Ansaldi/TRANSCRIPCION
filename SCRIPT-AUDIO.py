import whisper
model = whisper.load_model("base")
result = model.transcribe("NOMBRE DE ARCHIVO O RUTA", language="es")
with open("transcripcion.txt", "w", encoding="utf-8") as f:
    f.write(result["text"])
