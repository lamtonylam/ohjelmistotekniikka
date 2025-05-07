# Generoitu koodi alkaa

from pdf2image import convert_from_path
import os

from PIL import Image

pdf_path = os.path.join(os.path.dirname(__file__), "kuvat", "coverage_report.pdf")

output_dir = os.path.join(os.path.dirname(__file__), "kuvat")
os.makedirs(output_dir, exist_ok=True)

images = convert_from_path(pdf_path)

for i, image in enumerate(images):
    image.thumbnail((600, 600), Image.LANCZOS)
    resized_image = image
    image_path = os.path.join(output_dir, f"page_{i + 1}.png")
    resized_image.save(image_path, "PNG")

print(f"Converted {len(images)} to {output_dir}")

# Generoitu koodi loppuu