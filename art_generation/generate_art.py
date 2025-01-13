from PIL import Image, ImageDraw
import random
import os

# Create a folder to store the generated images if it doesn't exist
output_folder = "generated_art"
os.makedirs(output_folder, exist_ok=True)

# Function to generate a random color
def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Function to generate a random block-based artwork
def generate_block_image(block_size=500, num_blocks=10):
    # Create a blank canvas (white background)
    img = Image.new('RGB', (block_size, block_size), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)

    # Size of each individual block
    block_width = block_size // num_blocks

    # Draw random blocks
    for i in range(num_blocks):
        for j in range(num_blocks):
            x1 = i * block_width
            y1 = j * block_width
            x2 = (i + 1) * block_width
            y2 = (j + 1) * block_width
            draw.rectangle([x1, y1, x2, y2], fill=random_color())

    # Generate a unique file name for each image
    file_name = f"block_image_{random.randint(1000, 9999)}.png"
    file_path = os.path.join(output_folder, file_name)

    # Save the generated image
    img.save(file_path)

    # Return the file path for later use (for IPFS or other purposes)
    return file_path

# Function to generate multiple images
def generate_nft_artworks(num_images=999):
    print(f"Generating {num_images} NFT artworks...")
    for i in range(num_images):
        generate_block_image()

    print(f"Generated {num_images} images and saved them in '{output_folder}'.")

if __name__ == "__main__":
    # Generate 999 random artworks for the NFT collection
    generate_nft_artworks(999)
