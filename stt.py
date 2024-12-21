import openai
import os

def transcribe_audio(audio_file_path, output_dir):
    try:
        client = openai.OpenAI()
        with open(audio_file_path, "rb") as audio_file:
            transcript = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file
            )
        
        output_file_path = os.path.join(output_dir, "output.txt")
        with open(output_file_path, "w", encoding="utf-8") as output_file:
            output_file.write(transcript.text)
        
        print(f"Transcription saved to {output_file_path}")
    
    except openai.APIError as e:
        print(f"OpenAI API error during transcription: {e}")
    except Exception as e:
        print(f"Error during transcription: {e}")

if __name__ == "__main__":
    audio_file_path = "secand.mp3"
    output_dir = "output"
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    transcribe_audio(audio_file_path, output_dir)
