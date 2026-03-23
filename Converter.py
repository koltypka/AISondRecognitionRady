import ffmpeg

def convert(file_path, output_filename="audio//audio.wav"):
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
        print(f"Конвертация завершена: {output_filename}")
        return output_filename

    except ffmpeg.Error as e:
        print("Ошибка при конвертации")
        print(e.stderr.decode('utf8'))