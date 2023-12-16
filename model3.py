import os
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from keras.optimizers import Adam
from sklearn.utils import class_weight
import numpy as np


# Define the number of classes (replace 3 with the actual number of classes in your dataset)
num_classes = 13

# Image dimensions and other parameters
img_width, img_height = 150, 150
batch_size = 32
epochs = 10

# Organize Your Dataset
datagen = ImageDataGenerator(rescale=1./255,
                             shear_range=0.2,
                             zoom_range=0.2,
                             horizontal_flip=True,
                             rotation_range=45)


# Specify Image Paths
train_path = 'D:\\Personal Projects\\Nutrition Web-App\\Fruits-360\\test'
validation_path = 'D:\\Personal Projects\\Nutrition Web-App\\Fruits-360\\validation'

# Generate Image Batches
train_generator = datagen.flow_from_directory(train_path,
                                              target_size=(img_width, img_height),
                                              batch_size=batch_size,
                                              class_mode='categorical')

validation_generator = datagen.flow_from_directory(validation_path,
                                                   target_size=(img_width, img_height),
                                                   batch_size=batch_size,
                                                   class_mode='categorical')


# Calculate class weights
# class_labels = np.unique(train_generator.classes)
# class_counts = []
# for label in class_labels:
#     class_counts.append(np.sum(train_generator.classes == label))

# class_weights = class_weight.compute_class_weight(np.unique(train_generator.classes), train_generator.classes)
# class_weights = dict(enumerate(class_weights))


def compute_class_weight(class_weight, classes, y):
  """Computes class weights for unbalanced datasets.

  Args:
    class_weight: A dictionary of class weights, where the keys are the class labels
      and the values are the weights.
    classes: A list of the class labels.
    y: A list of the target labels.

  Returns:
    A list of the class weights, in the same order as the classes list.
  """

  if class_weight is None:
    class_weight = {class_label: 1 for class_label in classes}

  if not isinstance(class_weight, dict):
    raise TypeError("class_weight must be a dictionary")

  if not isinstance(classes, list):
    raise TypeError("classes must be a list")

  if not isinstance(y, list):
    raise TypeError("y must be a list")

  class_weights = []
  for class_label in classes:
    class_weight = class_weight.get(class_label, 1)
    class_weights.append(class_weight)
    class_weights_dict = dict(zip(class_labels, class_weights))
  return class_weights_dict


class_labels = np.unique(train_generator.classes)
class_weights = class_weight.compute_class_weight('balanced', class_labels)

# Convert to dictionary



# This will raise the error
# compute_class_weight({"balanced": 1}, [1, 2], [3, 4])

# # This will fix the error
# class_weights = compute_class_weight({"balanced": 1}, [1, 2], [3, 4])
# class_weights = dict(enumerate(class_weights))




# Build the Model
model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape=(img_width, img_height, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(num_classes, activation='softmax'))

# Compile the model
model.compile(optimizer=Adam(learning_rate=0.001), loss='categorical_crossentropy', metrics=['accuracy'])


# Train the Model
model.fit(train_generator, steps_per_epoch=train_generator.samples // batch_size, epochs=epochs, 
          validation_data=validation_generator, validation_steps=validation_generator.samples // batch_size,
          class_weight=class_weights)

# Evaluate and Save the Model
score = model.evaluate(validation_generator, steps=validation_generator.samples // batch_size)
print(f"Validation Accuracy: {score[1] * 100:.2f}%")

model.save('fruit_classifier_model.h5')
