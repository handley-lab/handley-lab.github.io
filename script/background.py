from google import genai
import requests
import os
import feedparser
from pandas import to_datetime
from io import BytesIO
import tarfile
import sys
import yaml
from PIL import Image

# Algorithm parameters
basic_model = "gemini-2.5-flash-preview-04-17"
text_model = "gemini-2.5-pro-preview-05-06"
image_model = "imagen-3.0-generate-002"
url_model = "https://deepmind.google/technologies/gemini/"
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

postname='background'
imagename = f'/assets/images/{postname}.png'
image_prompt_save = f'/prompts/images/{postname}.txt'

# Read group homepage
with open('index.md', 'r') as f:
    homepage = f.read()
print ("Generating image prompt")

pre_image_prompt = f"""
Generate a detailed creative prompt for an AI image generator. The goal is to design a subtle background image for a Github Jekyll homepage. The image should meet the following criteria:

1. It must be abstract and minimalistic to ensure that it does not distract from the homepage content.
2. It should evoke themes from the web content, drawing inspiration from the ideas and tone present in the text below.
3. The design must be harmonious and subtle, enhancing the overall user experience without overwhelming the content.
4. It will be 9:16 in aspect ratio, with website content over the center, so most of the interest should be at the margins of the background, since the center will be obscured by solid text boxes.

Here is the homepage text for reference:
```markdown
{homepage}
```

Please provide a comprehensive description that balances creativity with the need for a calm, background aesthetic.

Please only give the prompt, which I will feed directly into an image generating model. Do not give any pre- or post- amble, and don't give me options.
"""

response = client.models.generate_content(model=text_model, contents=pre_image_prompt)
image_prompt = response.text
print(image_prompt)

print("Generating image")
response = client.models.generate_images(model=image_model, prompt=image_prompt, config=genai.types.GenerateImagesConfig(aspectRatio="9:16", numberOfImages=1))

image = Image.open(BytesIO(
    response.generated_images[0].image.image_bytes
    ))

image.show()

# Save image
image.save(f'.{imagename}')
print(f"Image saved to .{imagename}")

with open(f'.{image_prompt_save}', 'w') as f:
    f.write("{% raw %}\n" + image_prompt + "\n{% endraw %}")
print(f"Image prompt saved to .{image_prompt_save}")
