# Food Recommendation App
In my experience, deciding what to eat can be the hardest and most time consuming part of eating. This python appliucation 
application  utilizes the Streamlit framework to create a Food Recommendation App. The app combines random string generation and a language model (LM) chatbox to suggest food dishes.

## Getting Started

To run the app, you need to have Python installed on your system. Additionally, you should replace the placeholder "ENTER API KEY" in the code with your actual OpenAI API key.

## Dependencies

Make sure to install the necessary dependencies by running:

```bash
pip install streamlit openai pandas matplotlib
```

## How to Use

1. Run the script.
2. Enter a list of food strings separated by commas in the provided text area.
3. Click the "Randomize" button to get a random food string from your list.
4. The app displays the selected random string and updates recommendation statistics.
5. Use the LM Chatbox to request a food recommendation by entering your query and clicking "Get Recommendation."

## OpenAI Language Model

The app uses OpenAI's text-davinci-003 language model to generate food recommendations based on user queries.

## Recommendation Statistics

The app maintains a Pandas DataFrame to store and display recommendation statistics. It tracks the count of each recommended food string.

## Chart Display

A bar chart visualizes the recommendation statistics, showing the popularity of different food suggestions.


## Note

Ensure that you handle your OpenAI API key securely and responsibly. Do not share it publicly.

Feel free to customize and enhance the app according to your preferences and requirements. Enjoy exploring diverse food recommendations!
