import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import os
from PIL import Image

# Load the trained model
model = tf.keras.models.load_model(r"C:\Users\Reham\OneDrive\Desktop\techableM\tm")



# Define the class labels (same as what you used in Teachable Machine)
class_names = ['Brian Moser', 'Professor X']

# Function to preprocess and predict the image
def predict_image(img_path):
    # Load and resize the image to the required size (Teachable Machine default is 224x224)
    img = image.load_img(img_path, target_size=(224, 224))
    
    # Convert the image to a numpy array
    img_array = image.img_to_array(img)
    
    # Expand dimensions to match the model input
    img_array = np.expand_dims(img_array, axis=0)
    
    # Normalize the image array (if required by your model)
    img_array = img_array / 255.0
    
    # Make the prediction
    prediction = model.predict(img_array)
    
    # Get the predicted class index
    predicted_class_index = np.argmax(prediction, axis=1)[0]
    
    # Get the predicted class name
    predicted_class_name = class_names[predicted_class_index]
    
    return predicted_class_name, prediction[0][predicted_class_index]

# Test the model with an input image
img_path = 'C:\Users\Reham\OneDrive\Desktop\techableM\imagetest\1.jpg'  # Replace with the image path you want to predict
predicted_class, confidence = predict_image(img_path)

print(f'Predicted Class: {predicted_class}')
print(f'Confidence: {confidence:.2f}')



