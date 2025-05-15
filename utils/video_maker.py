from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips

def make_video(audio_path, image_path, output="output_video.mp4"):
    audio = AudioFileClip(audio_path)
    image = ImageClip(image_path).set_duration(audio.duration)
    video = image.set_audio(audio)
    video.write_videofile(output, fps=24)
    return output

