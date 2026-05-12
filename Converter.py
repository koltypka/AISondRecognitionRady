import ffmpeg

def convert(file_path, output_filename="audio//audio.wav"):
    "Конвертация"
    try:
        stream = (
            ffmpeg
            .input(file_path)
            .output(
                output_filename,
                acodec='pcm_s16le',
                ac=1,
                ar='16000'
            )
            .overwrite_output()
        )

        stream.run()
        return output_filename

    except ffmpeg.Error as e:
        print(e.stderr.decode('utf8'))