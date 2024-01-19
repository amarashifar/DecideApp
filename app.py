import streamlit as st
import openai
import random
import matplotlib.pyplot as plt
import pandas as pd

# Set your OpenAI API key here
openai.api_key = "SET API KEY HERE"


def generate_recommendation(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",  # Use a supported engine
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()


def main():
    st.title("Food Recommendation App")

    # Get user input strings for the randomizer
    input_strings = st.text_area("Enter food dishes (separated by commas)", "Dish 1, Dish 2, Dish 3")
    strings_list = [s.strip() for s in input_strings.split(',')]

    # Randomizer button
    if st.button("Randomize"):
        random_string = random.choice(strings_list)
        st.success(f"Random String: {random_string}")

        # Update recommendation statistics
        update_recommendation_statistics(random_string)

    # Display chart of recommendation statistics
    display_chart()

    # LLM Chatbox for food recommendations
    st.subheader("Chatbox for Food Recommendations")
    user_input = st.text_input("You: ", "")
    if st.button("Get Recommendation"):
        if user_input:
            prompt = f"You: {user_input}\nRecommend a hot food dish:"
            recommendation = generate_recommendation(prompt)
            st.text(f"Chatbot: {recommendation}")
            # Update recommendation statistics
            update_recommendation_statistics(recommendation)
        else:
            st.warning("Please enter your input first.")

def update_recommendation_statistics(recommended_string):
    # Store recommendation statistics in a Pandas DataFrame
    if 'df_recommendations' not in st.session_state:
        st.session_state.df_recommendations = pd.DataFrame(columns=['String', 'Count'])

    df = st.session_state.df_recommendations

    # Update count for the recommended string
    if recommended_string in df['String'].values:
        df.loc[df['String'] == recommended_string, 'Count'] += 1
    else:
        new_row = pd.DataFrame([[recommended_string, 1]], columns=['String', 'Count'])
        df = pd.concat([df, new_row], ignore_index=True)

    # Save updated DataFrame in session state
    st.session_state.df_recommendations = df

def display_chart():
    # Display a bar chart of recommendation statistics
    if 'df_recommendations' in st.session_state and not st.session_state.df_recommendations.empty:
        st.bar_chart(st.session_state.df_recommendations.set_index('String'))

if __name__ == "__main__":
    main()
