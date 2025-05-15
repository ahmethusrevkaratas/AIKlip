from PIL import Image, ImageDraw, ImageFont

def generate_image(text="Gizli Tarih Teması", filename="output.png"):
    # 640x480 beyaz arka planlı basit görsel oluşturuyor
    img = Image.new('RGB', (640, 480), color='white')
    d = ImageDraw.Draw(img)
    d.text((10, 200), text, fill=(0, 0, 0))
    img.save(filename)
    return filename

