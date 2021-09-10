from PIL import Image

# Read image
img = Image.open("cat.png").convert("RGBA")

# Create black background
color = (0, 0, 0, 255)  # the last value is alpha
bg = Image.new("RGBA", img.size, color)

# Composite
composited = Image.alpha_composite(bg, img)
composited = composited.convert("RGB")

# Save image
composited.save("cat_new.png")