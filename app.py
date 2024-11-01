import streamlit as st
from openai import OpenAI
# Retrieve OpenAI API key from Streamlit secrets
api_key = st.secrets["OPENAI_API_KEY"]
# Initialize the OpenAI client
client = OpenAI(api_key=api_key)
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
            model="gpt-3.5-turbo",
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
