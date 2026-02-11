import whisper

# Carga el modelo base (puedes usar "small", "medium" o "large" para más precisión)
model = whisper.load_model("small")

# Ruta del archivo de audio .ogg
audio_file = "Alvaro\Downloads\3_a.ogg"

# Transcripción
result = model.transcribe(audio_file, language="fr")

print("Transcripción en francés:")
print(result["text"])
