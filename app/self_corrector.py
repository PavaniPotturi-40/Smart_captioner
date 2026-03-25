from PIL import Image
from .captioner import processor, model

def refine_caption(image_path):
    image = Image.open(image_path).convert('RGB')

    # Prompt helps improve caption quality
    prompt = "a detailed and accurate description of"
    inputs = processor(image, text=prompt, return_tensors="pt")

    output = model.generate(**inputs)
    refined_caption = processor.decode(output[0], skip_special_tokens=True)

    return refined_caption