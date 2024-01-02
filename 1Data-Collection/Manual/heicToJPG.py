import pyheif
from PIL import Image
import os
from tqdm import tqdm


def convert_heic_to_jpeg(heic_path, output_path):
    # Read the HEIC file
    heif_file = pyheif.read(heic_path)

    # Convert to other file format like jpeg
    image = Image.frombytes(
        heif_file.mode,
        heif_file.size,
        heif_file.data,
        "raw",
        heif_file.mode,
        heif_file.stride,
    )

    # Save the image as jpeg file
    image.save(output_path, "JPEG")


PATH = "1Data-Collection/Manual/Socks_Organized/HEIC"
SAVE_PATH = "1Data-Collection/Manual/Socks_Organized/JPG"

fileInPath = os.listdir(PATH)
fileInSavePath = os.listdir(SAVE_PATH)

for file in tqdm(fileInPath):
    saveName = file[:-5] + ".jpg"
    if saveName not in fileInSavePath:
        convert_heic_to_jpeg(PATH + "/" + file, SAVE_PATH + "/" + saveName)
