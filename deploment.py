from kokoro import KPipeline
import soundfile as sf
import sys




pipeline = KPipeline(lang_code='a') 
text = "The installation is now complete. I can speak your image captions perfectly."
generator = pipeline(text, voice='af_heart', speed=1)
for i, (gs, ps, audio) in enumerate(generator):
    # Save the output to a .wav file
    sf.write(f"caption_{i}.wav", audio, 24000)
    print(f"Success! Created: caption_{i}.wav")