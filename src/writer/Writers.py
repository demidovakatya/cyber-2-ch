from src.writer.ConsoleWriter import ConsoleWriter
from src.writer.TextFileWriter import TextFileWriter


class Writers:

    def make(self, writer, storage_path):
        if writer == 'txt':
            return TextFileWriter(storage_path)
        elif writer == 'console':
            return ConsoleWriter()
        else:
            raise Exception('Not existing writer: %s!' % writer)
