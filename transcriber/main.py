from utils import Filemanager
from utils import AudioPorcessor, TextProcessor


# default run function
def run(dir: str) -> None:
    # Get the videos from the directory
    file_manager = Filemanager(video_dir=dir)
    file_manager.get_videos()

    videos = file_manager.parsed_videos
    total_videos = len(videos)

    print(f'Total videos found: {total_videos}')
    print('Processing videos...')
    processed_count = 0
    processing_progress = 0

    # Process the videos
    for index, video in enumerate(videos):
        processed_count += 1
        processing_progress = (processed_count / total_videos) * 100

        audio = AudioPorcessor(v_path=video, chunk_min_duration=2,)
        audio.extract_audio()

        if (index % 5 == 0):
            print(
                f'Processing video {processed_count} of {total_videos} ({processing_progress:.2f}%)')

    audio_dirs = file_manager.get_audio_dirs()
    print(f'Total audio chunks found: {len(audio_dirs)}')
    print('Processing audio chunks...')
    for index, audio in enumerate(audio_dirs):

        audio_files = file_manager.get_audio_files(audio)

        for file in audio_files:
            text_processor = TextProcessor(audio)
            text_processor.process(file)


# run the program
if __name__ == '__main__':
    try:

        # input = input('Directory to parse video from: ')
        run(dir=r'D:\series\Fawlty Tower\S01')

    except KeyboardInterrupt:
        print('Program terminated!')
        exit(0)
