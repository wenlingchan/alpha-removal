import numpy as np
import cv2

# Read image
img = cv2.imread("cat.png", cv2.IMREAD_UNCHANGED)

# Split alpha from image
mask = img[:,:,3]
img = img[:,:,:3]

# Normalize mask
mask = mask / 255.0

# Convert mask from 1 channel to 3 channels
mask = np.repeat(np.expand_dims(mask, axis=-1), 3, axis=-1)

# Create black background
bg = np.zeros_like(img)
# For white background: bg = np.ones_like(img) * 255

# Composite
composited = img * mask + bg * (1 - mask)
composited = np.clip(composited, 0, 255)
composited = composited.astype(np.uint8)

# Save image
cv2.imwrite("cat_new.png", composited)