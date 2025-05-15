import openai

openai.api_key = "OPENAI_API_KEYİNİ_BURAYA_YAZ"

def generate_story(topic="gizli tarih", length=500):
    prompt = f"{topic} hakkında kurgusal ve ilgi çekici bir hikaye yaz, yaklaşık {length} kelime."
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=length*2,
        temperature=0.8,
        n=1,
        stop=None
    )
    story = response.choices[0].text.strip()
    return story
