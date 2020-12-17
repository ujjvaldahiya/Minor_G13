from keras.models import load_model
from keras.preprocessing import image
import os
import numpy as np
import matplotlib.pyplot as plt

def no_warn():
    import warnings

    def fxn():
        warnings.warn("deprecated", DeprecationWarning)

    with warnings.catch_warnings(record=True) as w:
        # Cause all warnings to always be triggered.
        warnings.simplefilter("always")
        # Trigger a warning.
        fxn()
        # Verify some things
        assert len(w) == 1
        assert issubclass(w[-1].category, DeprecationWarning)
        assert "deprecated" in str(w[-1].message)


no_warn()


# Loading the Weight into the model (Weight is a h5 file)
model = load_model('ingridients.h5')
no_warn()


# The Layout of the model.
model.summary()


# Class to predict the images, you only need to call the function read_images to read the iamges, and then the predict funciton.
class Fruit:
    
    def __init__(self, img_dir = ''):
        self.img_dir = img_dir
        self.cnt = 0
        self.batch_holder = None
        self.model = load_model('ingridients.h5')
        self.Label_dict = labels = {
            'apple':0,
            'banana':1,
            'cucumber':2,
            'kidneybean':3,
            'kiwi':4,
            'lemon':5,
            'onion':6,
            'orange':7,
            'paneer':8,
            'pineapple':9,
            'pomegranate':10,
            'potato':11,
            'strawberry':12,
            'tomato':13,
            'watermelon':14
             
        }
        self.label = list(self.Label_dict.keys())
    
    def read_images(self):
        self.cnt = len(os.listdir(self.img_dir))
        self.batch_holder = np.zeros((self.cnt, 100, 100, 3))
        for i,img in enumerate(os.listdir(self.img_dir)):
            img = image.load_img(os.path.join(self.img_dir,img), target_size=(100, 100))
            self.batch_holder[i, :] = img
        return self.batch_holder
    
    def predict(self):
        fig = plt.figure(figsize=(20, 20))
        for i,img in enumerate(self.batch_holder):
            fig.add_subplot(5, 5, i+1)
            result=self.model.predict(self.batch_holder)
            result_classes = result.argmax(axis=-1)
            plt.title(self.label[result_classes[i]])
            plt.tick_params(
                axis='both',        
                which='both',      
                bottom=False,      
                top=False,         
                labelbottom=False,
                labelleft=False)
            plt.imshow(img/256.)
        plt.show()

    def name(self):
        for i,img in enumerate(self.batch_holder):
            result=self.model.predict(self.batch_holder)
            if result.max(axis=-1)<0.4:
                return ""
            result_classes = result.argmax(axis=-1)
            return self.label[result_classes[i]]

# Class takes a parameter -> location of  images that needs to be predicted.
def pred():
    obj = Fruit('C:\\Users\\Ujjval Dahiya\\Desktop\\minor\\media\\temp_pics')
    obj.read_images()
    name = obj.name()
    return name
