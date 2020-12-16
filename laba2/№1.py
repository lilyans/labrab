import numpy as np
import matplotlib as mpl
from PIL import Image

img = Image.open('lunar01_raw.jpg')
data = np.array(img)
maxdata = data.max()
mindata = data.min()

updated_data = np.around((data - mindata * np.ones(data.shape)) * 255 / (maxdata - mindata))

res_image = Image.fromarray(updated_data.astype('uint8'), 'L')
res_image.show()