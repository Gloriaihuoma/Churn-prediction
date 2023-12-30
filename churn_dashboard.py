import streamlit as st
import pandas as pd
import pickle

# Function to load the model
def load_model():
    with open('.\Best_model.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

# Function to make predictions (probabilities)
def make_predictions(model, df):
    # Get probability estimates for churn
    probabilities = model.predict_proba(df)
    
    # Assuming the second column (index 1) corresponds to the probability of churn
    churn_probabilities = probabilities[:, 1]

    return churn_probabilities

def main():
    st.title('Churn Prediction Dashboard')

    # Load the model
    model = load_model()

    # File uploader
    uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

    if uploaded_file is not None:
        # Read CSV file
        df = pd.read_csv(uploaded_file)

        # Make predictions (probabilities) and add as a new column
        df['Churn Probability'] = make_predictions(model, df)

        # Convert probabilities to percentages and format the column
        df['Churn Probability'] = df['Churn Probability'].apply(lambda x: f"{x*100:.2f}%")

        # Show modified data
        st.write("Data with Churn Probabilities:")
        st.write(df)

if __name__ == "__main__":
    main()
