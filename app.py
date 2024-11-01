import streamlit as st
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

# Initialize the OpenAI client with your API key
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# Define the Streamlit app
def main():
    st.title("Blog Title Generator")
    st.write("Generate SEO-optimized, attention-grabbing blog titles!")

    # User input for blog topic
    blog_topic = st.text_input("Enter your blog topic:", "Digital Marketing Tips")

    # Number of titles to generate
    num_titles = st.slider("Select number of titles to generate:", 1, 10, 5)

    if st.button("Generate Titles"):
        # Create prompt based on user input
        blog_title_generator_prompt = f"""I want you to act as a professional blog titles generator. 
        Think of titles that are SEO optimized and attention-grabbing at the same time, 
        and will encourage people to click and read the blog post. 
        I want to generate {num_titles} titles in a numbered list format.
        My blog post is about: {blog_topic}
        """

        # Call OpenAI API to generate titles with ChatCompletion
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Ensure this is a correct model
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": blog_title_generator_prompt},
            ],
            max_tokens=150,
            temperature=0.7
        )

        # Extract and display the generated titles
        generated_text = response.choices[0].message.content.strip()
        st.write("Generated Titles:")
        st.write(generated_text)

if __name__ == "__main__":
    main()
