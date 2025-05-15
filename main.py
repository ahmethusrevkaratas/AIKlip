import argparse
from utils.text_gen import generate_story
from utils.tts import text_to_speech
from utils.image_gen import generate_image
from utils.video_maker import make_video

def main():
    parser = argparse.ArgumentParser(description="AIKlip video oluşturucu")
    parser.add_argument("--topic", type=str, default="gizli tarih", help="Hikaye konusu")
    parser.add_argument("--length", type=int, default=500, help="Hikaye uzunluğu kelime olarak")
    parser.add_argument("--lang", type=str, default="tr", help="Ses dili (ör: tr, en)")
    args = parser.parse_args()

    print("AIKlip başladı...")

    story = generate_story(args.topic, args.length)
    print("Hikaye oluşturuldu.")

    audio_path = text_to_speech(story, lang=args.lang)
    print(f"Ses dosyası oluşturuldu: {audio_path}")

    image_path = generate_image(f"{args.topic} temalı görsel")
    print(f"Görsel oluşturuldu: {image_path}")

    video_path = make_video(audio_path, image_path)
    print(f"Video oluşturuldu: {video_path}")

if __name__ == "__main__":
    main()
