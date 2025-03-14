from PIL import Image, ImageDraw, ImageFont

# Define text and properties
text = "Good artists copy, great artists steal 🥂"
font_path = "arial.ttf"  # Ensure this file exists in your script directory
font_size = 40
text_color = ["red", "green", "blue"]  # RGB colors for blinking effect
frame_count = len(text_color)

# Create frames for GIF
frames = []
for i in range(frame_count):
    img = Image.new("RGB", (600, 100), "black")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font_path, font_size)
    
    text_width, text_height = draw.textsize(text, font=font)
    draw.text(((600 - text_width) // 2, (100 - text_height) // 2), text, font=font, fill=text_color[i])
    
    frames.append(img)

# Save as GIF
gif_path = "blinking_text.gif"
frames[0].save(gif_path, save_all=True, append_images=frames[1:], duration=500, loop=0)

print(f"✅ GIF saved as {gif_path}")
