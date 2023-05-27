import os


class Filemanager:

    def __init__(self, video_dir=None,):

        if (video_dir == None):
            raise ValueError()

        self.video_dir = video_dir

        # Accepted video extensions
        self.accepted_ext = ['mp4', 'mkv', 'webm', 'wmv', 'mov', 'flv', 'avi']

        # Get all videos from the directory and all its future subdirectories using recursion
        self.parsed_videos = []

    def get_videos(self):
        # Walk through the directory and get all the videos
        for root, dirs, files in os.walk(self.video_dir):
            for file in files:
                if file.endswith(tuple(self.accepted_ext)):
                    self.parsed_videos.append(os.path.join(root, file))

    def get_audio_dirs(self) -> list:
        # Get all the audio directories from temp-storage/audio-chunks
        audio_dirs = []
        audio_chunks_dir = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'temp-storage', 'audio-chunks')

        for root, dirs, files in os.walk(audio_chunks_dir):
            for dir in dirs:
                audio_dirs.append(os.path.join(root, dir))

        return audio_dirs

    def get_audio_files(self, dir) -> list:
        # Get all the audio files from the given directory
        audio_files = []

        for root, dirs, files in os.walk(dir):
            for file in files:
                audio_files.append(os.path.join(root, file))

        return audio_files
