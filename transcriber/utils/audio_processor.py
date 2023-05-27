from moviepy.editor import VideoFileClip
from pydub import AudioSegment
import os


class AudioPorcessor:

    def __init__(self, v_path: str = None, chunk_min_duration: int = 1,) -> None:
        if (v_path == None):
            raise ValueError()

        self.v_path = v_path
        self.chunk_min_duration = chunk_min_duration

        # get project directory
        self.project_dir = os.path.dirname(
            os.path.dirname(os.path.abspath(__file__)))

        # get video filename
        self.video_filename = os.path.basename(self.v_path)
        self.video_filename = os.path.splitext(self.video_filename)[0]

    def extract_audio(self):
        try:
            # extract audio from video
            video = VideoFileClip(self.v_path)
            total_duration = video.duration
            print(f'Total duration: {total_duration}')

            for i in range(0, int(total_duration), self.chunk_min_duration * 60):
                start_time = i
                end_time = min(i + self.chunk_min_duration *
                               60, total_duration)

                audio_segment = video.subclip(start_time, end_time).audio

                audio_chunks_dir = os.path.join(
                    self.project_dir, 'temp-storage', 'audio-chunks', self.video_filename)

                if (not os.path.exists(audio_chunks_dir)):
                    os.makedirs(audio_chunks_dir)

                chunk_path = os.path.join(
                    audio_chunks_dir, f'{self.video_filename}-{start_time}-{end_time}-min.wav',)

                audio_segment.write_audiofile(chunk_path)
                print(f'Audio chunk saved at {chunk_path}')
            video.close()

        except Exception as e:
            print(e)
            print('Error extracting audio from video!')
            pass
