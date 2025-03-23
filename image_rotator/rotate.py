from PIL import Image
import os

def rotate_image(input_path, output_path, angle):
    """Rotates an image by the given angle and saves it."""
    try:
        print(f"🔄 Attempting to open image: {input_path}")
        image = Image.open(input_path)

        print(f"✅ Opened image successfully: {input_path}")
        rotated_image = image.rotate(angle, expand=True)

        # Ensure the output folder exists
        output_dir = os.path.dirname(output_path)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            print(f"📁 Created missing directory: {output_dir}")

        rotated_image.save(output_path)
        print(f"✅ Saved rotated image to {output_path}")

    except Exception as e:
        print(f"❌ ERROR: {e}")
