import zipfile
import os


def zip_images(image_paths: list, zip_filename: str):
    print("INFO: zipping images...")
    with zipfile.ZipFile(zip_filename, "w") as zipf:
        for image_path in image_paths:
            _, filename = os.path.split(image_path)
            zipf.write(image_path, arcname=filename)
            print(f"Added {filename} to the zip file.")
    print(f"...done!  images have been zipped into {zip_filename}")
