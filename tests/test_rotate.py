import unittest
import os
from PIL import Image
from image_rotator.rotate import rotate_image

class TestImageRotate(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.input_dir = "input"
        cls.output_dir = "output"
        cls.test_input = os.path.join(cls.input_dir, "sample.jpg")
        cls.test_output = os.path.join(cls.output_dir, "rotated.jpg")

        # Create input and output directories
        os.makedirs(cls.input_dir, exist_ok=True)
        os.makedirs(cls.output_dir, exist_ok=True)

        # Create a sample test image if not already present
        if not os.path.exists(cls.test_input):
            image = Image.new("RGB", (100, 100), color="blue")
            image.save(cls.test_input)
            print(f"✅ Created test image at: {cls.test_input}")
        else:
            print(f"ℹ️ Test image already exists at: {cls.test_input}")

    def test_rotate(self):
        print(f"🔄 Running test_rotate with {self.test_input}")

        # Ensure output directory exists
        os.makedirs(self.output_dir, exist_ok=True)

        # Rotate the image
        rotate_image(self.test_input, self.test_output, 90)

        # Check if rotated image exists
        self.assertTrue(os.path.exists(self.test_output), "❌ Rotated image was not saved!")

        # Verify rotated image properties
        with Image.open(self.test_input) as original_image, Image.open(self.test_output) as rotated_image:
            self.assertEqual(original_image.mode, rotated_image.mode, "❌ Image mode mismatch!")
            self.assertGreater(rotated_image.width, original_image.width, "❌ Rotated image width is incorrect!")
            self.assertGreater(rotated_image.height, original_image.height, "❌ Rotated image height is incorrect!")
            print(f"✅ Verified rotated image dimensions: {rotated_image.size}")

    # @classmethod
    # def tearDownClass(cls):
    #     """Remove test images after tests."""
    #     try:
    #         os.remove(cls.test_output)
    #         print(f"🗑️ Deleted rotated image: {cls.test_output}")
    #     except FileNotFoundError:
    #         print("⚠️ Rotated image not found for cleanup.")

if __name__ == "__main__":
    unittest.main()
