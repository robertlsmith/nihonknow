from pathlib import Path
from gtts import gTTS

from data import word_bank, phrase_bank

def generate_audio(items):
    for item in items:

        filename = Path(item["audio"])

        filename.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        if filename.exists():
            continue

        print(f"Generating {filename}")

        tts = gTTS(
            text=item["japanese"],
            lang="ja"
        )

        tts.save(filename)


generate_audio(word_bank)
print("Words complete.")

generate_audio(phrase_bank)
print("Phrases complete.")