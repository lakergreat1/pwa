import os
from groq import Groq

class GroqClient:
    def __init__(self):
        api_key = os.environ.get("GROQ_API_KEY")
        if not api_key:
            raise ValueError("GROQ_API_KEY environment variable is not set")
        self.client = Groq(api_key=api_key)

    def transcribe_audio(self, audio_file, language=None):
        try:
            transcription = self.client.audio.transcriptions.create(
                file=audio_file,
                model="whisper-large-v3",
                language=language,
                response_format="text"
            )
            return transcription.text
        except Exception as e:
            print(f"Error during transcription: {str(e)}")
            return None
