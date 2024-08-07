import pandas as pd
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Configure Gemini API
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

# Load the dataset
df = pd.read_csv("sentences.csv")['Sentence'].iloc[0:]
df = pd.DataFrame(df)

def get_sentiment(tweet):
    try:
        response = model.generate_content(
            f"Categorize the following sentence: example as The sky is blue. :Weather, This movie was fantastic! : Sentiment like this categorized only in one word  don't give stars in output give only in one word:\n\n{tweet}"
        )
        sentiment = response.text.strip().lower()
        return sentiment
    except Exception as e:
        print(f"Error: {e}")
        return None

# Apply sentiment analysis
df['Categorized'] = df['Sentence'].apply(get_sentiment)

# Display the dataframe
# df.to_csv("Genai.csv")
print(df)
