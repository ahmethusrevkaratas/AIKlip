from utils.text_gen import generate_story
from utils.tts import text_to_speech
from utils.image_gen import generate_image
from utils.video_maker import make_video

def main():
    print("AIKlip projesi başladı!")
    
    # Hikaye oluştur
    story = generate_story("gizli tarih", length=500)
    print("Hikaye oluşturuldu.")
    
    # Metni seslendir
    audio_path = text_to_speech(story)
    print("Ses dosyası oluşturuldu:", audio_path)
    
    # Görsel üret
    image_path = generate_image("tarih temalı gizemli manzara")
    print("Görsel oluşturuldu:", image_path)
    
    # Videoyu oluştur
    video_path = make_video(audio_path, image_path)
    print("Video oluşturuldu:", video_path)
    
if __name__ == "__main__":
    main()

