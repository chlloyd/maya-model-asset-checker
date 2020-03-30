import os


def get_all_images(sourceimages_path):
    """

    Args:
        sourceimages_path: Path to sourceimages folder.

    Returns: List of all images paths within sourceimages.

    """
    all_images_list = []
    for subdir, dirs, files in os.walk(sourceimages_path):
        for file in files:
            image_path = os.path.join(subdir, file)
            all_images_list.append(image_path)
    return all_images_list


"""def image_naming_check(all_images):  # Naming convention for images textures
    broken_image_naming_list = []
    for file_image in all_images:
        base_name = os.path.splitext(os.path.basename(file_image))[0].split("_")
        if (base_name[-1] == "baseColor") or (base_name[-1] == "metalness") or (base_name[-1] == "roughness") or (
                base_name[-1] == "normal"):
            pass
        else:
            broken_image_naming_list.append(file_image)
    return broken_image_naming_list"""
