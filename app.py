import streamlit as st  # For creating the web interface
import os
import asyncio
from together import AsyncTogether, Together  # For interacting with Together AI

# Title of the Streamlit app
st.title("Mixture of LLMs App")

# Input field for the Together API key
together_api_key = st.text_input("Enter the Together API key", type="password")

# Initialize the Together API clients
if together_api_key:
    os.environ["TOGETHER_API_KEY"] = together_api_key
    client = Together(api_key=together_api_key)
    async_client = AsyncTogether(api_key=together_api_key)

# Reference models for generating individual responses
reference_models = {
    "Qwen/Qwen2-72B-Instruct",
    "mistralai/Mixtral-8x22B-Instruct-v0.1",
    "databricks/dbrx-instruct",
}

# Aggregator model for synthesizing responses
aggregator_model = "mistralai/Mixtral-8x22B-Instruct-v0.1"

# Prompt for the aggregator model
aggregator_system_prompt = """You have been provided with a set of responses from various open-source models to the latest user query. Your task is to synthesize these responses into a single, high-quality response. It is crucial to critically evaluate the information provided in these responses, recognizing that some of it may be biased or incorrect. Your response should not simply replicate the given answers but should offer a refined, accurate, and comprehensive reply to the instruction. Ensure your response is well-structured, coherent, and adheres to the highest standards of accuracy and reliability. Responses from models:"""


# Function to query individual LLMs asynchronously
async def run_llm(model):
    await asyncio.sleep(1)  # Respect API rate limits
    response = await async_client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": user_prompt}],
        temperature=0.7,
        max_tokens=512,
    )
    return model, response.choices[0].message.content


# Main function to orchestrate the app's logic
async def main():
    results = []

    # Query all reference models in parallel
    for model in reference_models:
        results.append(await run_llm(model))

    # Display individual model responses
    st.subheader("Individual Responses")
    for model, response in results:
        with st.expander(f"Response from {model}"):
            st.write(response)

    # Aggregate responses using the aggregator model
    st.subheader("Aggregated Response")
    finalStream = client.chat.completions.create(
        model=aggregator_model,
        messages=[
            {"role": "system", "content": aggregator_system_prompt},
            {"role": "user", "content": ",".join(response for _, response in results)},
        ],
        stream=True,
    )

    # Display aggregated response as a live stream
    response_container = st.empty()
    full_response = ""
    for chunk in finalStream:
        content = chunk.choices[0].delta.content or ""
        full_response += content
        response_container.markdown(full_response + " ")

    # Final aggregated response display
    response_container.markdown(full_response)


# Input field for user prompt
user_prompt = st.text_input("Enter your prompt:")

# Button to trigger the processing
if st.button("Get Answer"):
    if user_prompt:
        asyncio.run(main())
    else:
        st.warning("Please enter a prompt.")
