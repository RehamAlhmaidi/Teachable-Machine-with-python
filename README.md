# 🚀 Image Recognition with Teachable Machine

## 📌 Overview
This project demonstrates how to train an image recognition model using Google's Teachable Machine, export it in TensorFlow format, and use a Python script to load the model and make predictions on new images.



## ✨ Features
- 🎯 Trains an image recognition model with at least two classes.
- 📤 Exports the trained model in TensorFlow format.
- 🖼️ Loads the model and makes predictions using a Python script.
- 🔍 Uses `tensorflow`, `numpy`, and `PIL` for image preprocessing and prediction.
- 📈 Provides high-confidence predictions for images.
- 🔄 Supports easy integration with new datasets by retraining the model in Teachable Machine.




## ⚙️ Requirements
Ensure you have the following dependencies installed before running the script:

```sh
pip install tensorflow numpy pillow
```



## 📁 Project Structure
```
/
│-- TeachableM_AI.py         # 🖥️ Python script to load and use the model
│-- keras_model.h5           # 🤖 Trained model file exported from Teachable Machine
│-- imagetest/               # 🖼️ Folder containing test images
```



## 🛠️ Usage
1. **📚 Train the Model:**
   - Go to [Teachable Machine](https://teachablemachine.withgoogle.com/) 🌐
   - Train an image classification model with at least two classes.
   - Export the trained model in TensorFlow (.h5) format.
   - Ensure that the class labels are correctly mapped.




2. **📥 Download the Model:**
   - Place the exported `keras_model.h5` file in the project directory.




3. **▶️ Run the Python Script:**
   - Ensure `TeachableM_AI.py` is updated to use `keras_model.h5` as the model file.
   - Update the `img_path` to specify an image for testing.
   - Run the script:

   ```sh
   python TeachableM_AI.py
   ```



4. **📊 Prediction Output:**
   The script will output the predicted class and confidence score, e.g.:
   
![Screenshot 2025-02-06 163631](https://github.com/user-attachments/assets/6444b11c-e903-45e0-95b9-2be4e9e08bae)


  

## 🏗️ How It Works
- 🏋️ The model is loaded using TensorFlow's `load_model` function.
- 🔄 The input image is resized to match the expected dimensions (224x224 pixels).
- 🔢 The image is converted into a NumPy array and normalized (scaled between 0 and 1).
- 🎯 The model predicts the class label and confidence score.
- 📌 The highest confidence score determines the final classification.



## 📝 Notes
- 🖼️ Ensure the image used for prediction matches the model's expected input size (224x224 pixels).
- 🛠️ If the model path is incorrect, update `model = tf.keras.models.load_model("keras_model.h5")`.
- 📊 The accuracy of the model depends on the quality and quantity of training data.
- 🔄 Additional preprocessing may improve prediction performance.



## 🚀 Future Improvements
- 🏆 Extend the model to recognize more classes by retraining in Teachable Machine.
- ⚡ Optimize the prediction pipeline for real-time classification.
- 🌐 Integrate with a web interface for easy image uploads and live predictions.





