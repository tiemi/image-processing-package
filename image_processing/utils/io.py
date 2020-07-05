from skimage.io import imread

def read_image(path, is_gray = False):
    image = imread(path, as_gray = is_gray)
    return image