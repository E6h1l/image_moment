from PIL import Image
import numpy as np

def open_image(path : str) -> np.ndarray:
    img = Image.open(path).convert('L')
    img_array = np.array(img)

    return img_array


def log_image(img_array : np.ndarray, c : int) -> np.ndarray:
    log_img = c*np.log(1+img_array)

    x_min = np.min(log_img)
    x_max = np.max(log_img)

    norm_log_img = (log_img - x_min) / (x_max - x_min) * 255

    return norm_log_img
    

def prep_image(img_array : np.ndarray) -> np.ndarray:
    shape = img_array.shape
    prep_img = np.zeros(shape)

    for row in range(shape[0]):
        for column in range(shape[1]):
            if img_array[row][column] < 100:
                prep_img[row][column] = 0
            elif img_array[row][column] > 180:
                prep_img[row][column] = 255
            else:
                prep_img[row][column] = img_array[row][column]

    return prep_img


def invert(img_array : np.ndarray) -> np.ndarray:
    return 255 - img_array


def find_invariate(img_array : np.ndarray) -> tuple:
    x = np.arange(img_array.shape[1])
    y = np.arange(img_array.shape[0])[:, np.newaxis]

    m00 = np.sum(img_array)
    m01 = np.sum(img_array * y)
    m10 = np.sum(img_array * x)

    x_dash = x - m10 / m00
    y_dash = y - m01 / m00

    mu11 = np.sum(x_dash * y_dash * img_array)
    mu12 = np.sum(x_dash * (y_dash ** 2) * img_array)
    mu21 = np.sum((x_dash ** 2) * y_dash * img_array)
    mu02 = np.sum((y_dash ** 2) * img_array)
    mu20 = np.sum((x_dash ** 2) * img_array)
    mu30 = np.sum((x_dash ** 3) * img_array)
    mu03 = np.sum((y_dash ** 3) * img_array)

    eta11 = mu11 / m00 ** 2
    eta12 = mu12 / m00 ** 2.5
    eta21 = mu21 / m00 ** 2.5
    eta20 = mu20 / m00 ** 2
    eta02 = mu02 / m00 ** 2
    eta30 = mu30 / m00 ** 2.5
    eta03 = mu03 / m00 ** 2.5

    phi1 = eta20 + eta02
    phi2 = (eta20 - eta02) ** 2 + 4 * eta11 ** 2
    phi3 = (eta30 - 3 * eta12) ** 2 + (3 * eta21 - eta03) ** 2
    phi4 = (eta30 + eta12) ** 2 + (eta21 + eta03) ** 2

    return (phi1, phi2, phi3, phi4)


def save_image(img_array : np.ndarray, image_name : str) -> None:
    pil_img = Image.fromarray(img_array.astype(np.uint8))
    pil_img.save(image_name)