import sys

sys.path.append("../")

from mtai.transcribes import Transcribe

secret_key = "your_secret_key_here"

# Initialize Transcribe with secret key
transcribe = Transcribe(secret_key=secret_key)

# Example for listing all transcribes
print("List of transcribes:")
print(transcribe.list())
print(Transcribe.list())

# Example for getting a transcribe by ID
transcribe_id = "12345"  # Replace with your transcribe ID
print(f"\nTranscribe details for ID {transcribe_id}:")
print(transcribe.get_transcribe_by_id(transcribe_id))
print(Transcribe.get_transcribe_by_id(transcribe_id))

# Example for creating a transcribe from an audio URL
audio_url = "http://example.com/audio.mp3"  # Replace with your audio URL
services = ["service1", "service2"]  # Replace with your services
print("\nCreating transcribe from audio URL:")
print(transcribe.create_transcribe_from_audio_url(audio_url, services))
print(Transcribe.create_transcribe_from_audio_url(audio_url, services))

# Example for creating a transcribe from a media file
media_file = "/path/to/media/file.mp4"  # Replace with your media file path
print("\nCreating transcribe from media file:")
print(transcribe.create_transcribe_from_media_file(media_file, services))
print(Transcribe.create_transcribe_from_media_file(media_file, services))

# Example for creating a transcribe from a YouTube video
youtube_url = "http://youtube.com/video"  # Replace with your YouTube video URL
print("\nCreating transcribe from YouTube video:")
print(transcribe.create_transcribe_from_youtube_video(youtube_url, services))
print(Transcribe.create_transcribe_from_youtube_video(youtube_url, services))

# Example for deleting a transcribe by ID
delete_transcribe_id = "67890"  # Replace with your transcribe ID
print(f"\nDeleting transcribe with ID {delete_transcribe_id}:")
print(transcribe.delete_transcribe_by_id(delete_transcribe_id))
print(Transcribe.delete_transcribe_by_id(delete_transcribe_id))
