import pickle
import cv2
import matplotlib.pyplot as plt


test_image = cv2.imread("artifacts/cats_vs_dogs/test_set/cats/cat.5000.jpg")
print(test_image.shape)

# cv2.imshow("image",test_image)
# cv2.waitKey(0)
# test_image = cv2.resize(test_image, (256, 256))
# cv2.imshow("image",test_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# plt.imshow(test_image)

import tensorflow.keras as keras

with open("artifacts/prepare_base_model/cats_vs_dogs_trained_model",'rb') as file:
    model = pickle.load(file)

model.summary()

test_image = cv2.resize(test_image, (256, 256))
test_input = test_image.reshape((1, 256, 256, 3))

print(f"\nthe prediction is {model.predict(test_input)}. 0 stands for cat and 1 stands for dog.")