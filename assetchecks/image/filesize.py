import os


def image_file_size(sourceimages_path, min_image_size=100000):  # File size, small being useless file
    """

    Args:
        sourceimages_path:Path for sourceimages folder
        min_image_size:Defaulting to 10000 bytes (100KB), this sets the minimum image size.

    Returns:A list of all images with paths smaller than the set minimum image size.

    """
    small_image_list = []
    for subdir, dirs, files in os.walk(sourceimages_path):
        for file in files:
            filename = os.path.join(subdir, file)
            print(filename)
            print(os.path.getsize(filename))
            if os.path.getsize(filename) <= min_image_size:
                small_image_list.append(os.path.basename(filename))
    return small_image_list
