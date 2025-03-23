from image_rotator import rotate_image

input_image = "input.jpg"  # Place an image here
output_image = "output.jpg"
angle = 45

print(f"Rotating {input_image} by {angle} degrees...")
rotate_image(input_image, output_image, angle)
print(f"Rotated image saved as {output_image}")