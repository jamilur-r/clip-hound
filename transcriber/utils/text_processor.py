import os
import whisper


class TextProcessor:

    def __init__(self, folder_name: str) -> None:
        self.out_dir = os.path.join(os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))), 'temp-storage', 'text-chunks')

        self.project_dir = os.path.dirname(
            os.path.dirname(os.path.abspath(__file__)))

        self.folder_name = os.path.splitext(os.path.basename(folder_name))[0]

        self.model = whisper.load_model('small')

        if (not self.out_dir):
            os.makedirs(self.out_dir)

    def process(self, audio_file: str) -> None:
        # get file name without extension
        file_name = os.path.splitext(os.path.basename(audio_file))[0]

        text_chunk_path = os.path.join(self.out_dir, self.folder_name)
        if (not os.path.exists(text_chunk_path)):
            os.makedirs(text_chunk_path)

        text_file_path = os.path.join(
            text_chunk_path, file_name + '.txt')

        result = self.model.transcribe(
            audio_file, verbose=True, temperature=0.8,)

        with open(text_file_path, 'w') as text_file:
            text_file.write(f'{result}')
