# Churn Prediction Dashboard

## Introduction
This Churn Prediction Dashboard is built using Streamlit, a popular Python library for creating simple and interactive web applications. The dashboard is designed to predict customer churn probabilities based on input data, using a pre-trained machine learning model.

## Features
- **Upload Feature**: Users can upload their own CSV files containing customer data. The file should be structured appropriately to match the format the model expects.
- **Prediction**: The dashboard applies the pre-trained model to the uploaded data to predict the likelihood of churn for each customer.
- **Results Visualization**: Displays the original data with an additional column showing churn probabilities as percentages.

## How to Use
1. **Starting the Dashboard**: Run the dashboard by executing the Python script. This will host the dashboard on a local server, which can be accessed through a web browser.
2. **Uploading Data**: Use the file uploader to upload a CSV file. The file should contain customer data that the pre-trained model can process.
3. **Viewing Predictions**: Once the file is uploaded, the dashboard processes the data and displays churn probabilities for each customer in the dataset.

## Code Structure
- **Model Loading**: The `load_model` function loads the pre-trained model (stored as a pickle file).
- **Prediction Function**: The `make_predictions` function takes the model and a dataframe as input, returning churn probabilities.
- **Streamlit Interface**: The `main` function uses Streamlit to create the web interface, including the title, file uploader, and data display.
- **Main Execution**: The script checks if it's the main module and runs the `main` function accordingly.

## Requirements
- **Python Libraries**: Streamlit, Pandas, Pickle
- **Model File**: A pre-trained model saved as `Best_model.pkl` in the same directory as the script.


This dashboard serves as a quick and user-friendly way to apply churn predictions to customer data, making it a valuable tool for businesses focusing on customer retention strategies.
