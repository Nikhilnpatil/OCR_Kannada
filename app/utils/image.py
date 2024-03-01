from PIL import Image 
import io, base64, os, cv2
import numpy as np

IMAGEDIRECTORY= 'app/images/'

def save_image(string64: str)->str:
    '''save_image(string64) is a function that takes in a base64 encoded string of the image and returns the path at which the image is saved'''
    if string64:
        image = Image.open(io.BytesIO(base64.b64decode(string64.split(',')[1])))
        pixel_data = image.load()
        if image.mode == "RGBA":
            for y in range(image.size[1]):
                for x in range(image.size[0]): 
                    # Check if it's opaque
                    if pixel_data[x, y][3] < 255:
                        pixel_data[x, y] = (255, 255, 255, 255)
        image.thumbnail([128,128], Image.ANTIALIAS)
        image_name = str(len(os.listdir(IMAGEDIRECTORY))+1)+'.png'
        image_path = os.path.join(IMAGEDIRECTORY,image_name)
        image.save(image_path)
        return image_path
    else:
        return None
    
def read_image(path:str)->np.array:
    '''read_image(path) is a function that takes the path of the image and returns the data in the required format'''
    return (cv2.cvtColor(cv2.imread(path),cv2.COLOR_BGR2GRAY).reshape(-1,128,128)/255) #model requires the reshaping
