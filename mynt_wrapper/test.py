import opencvsample
from scipy import misc
from PIL import Image
import time
import psutil

# im_np = misc.imread('test.jpg')
# opencvsample.openImage(im_np)
# opencvsample.test()
opencvsample.init_camera()
for i in range(100):
    img = Image.fromarray(opencvsample.get_depth_image())
    img.show('test')
    time.sleep(1)
    for proc in psutil.process_iter():
        if proc.name() == "display":
            proc.kill()