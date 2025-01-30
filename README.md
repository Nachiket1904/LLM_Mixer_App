# Mixture of LLMs App

This project is the implementation of the concepts discussed in my blog on the **Mixture of LLMs App**. It demonstrates how to use multiple open-source large language models (LLMs) collaboratively to generate high-quality responses. By leveraging intelligent aggregation, this app produces results that can rival commercial solutions like GPT-4.

In my blog, I explain the idea behind using multiple models and synthesizing their responses for better overall performance. The code here follows that approach and is designed to be easy to use through an interactive web interface.

## Features

- **Multiple Model Integration**: Generates responses using multiple open-source models, including `Qwen2-72B`, `Mixtral-8x22B`, and `DBRX`.
- **Asynchronous Processing**: Uses Python's `asyncio` for parallel processing, ensuring faster response times.
- **Smart Aggregation**: Synthesizes individual responses using `Mixtral-8x22B` as an aggregator model, creating a single, comprehensive answer.
- **Interactive Web Interface**: Built with `Streamlit` to enable easy user interaction.

## How It Works

1. **User Input**: The user provides a prompt through the app's interface.
2. **Model Responses**: The app queries multiple LLMs to generate individual responses asynchronously.
3. **Aggregation**: The app aggregates these responses using a separate model to create a refined, accurate answer.
4. **Display**: Both the individual model responses and the aggregated response are displayed in the app.

## Installation

### Prerequisites

- Python 3.7 or higher
- A Together AI API key (sign up at [Together AI](https://www.together.ai/))



### Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/mixture-of-llms-app.git
   cd mixture-of-llms-app
   ```

2.cInstall dependencies:
```bash
pip install -r requirements.txt
```
3. Run the application:
``` bash
streamlit run app.py
```
### Usage
1) Open the app in your browser (default URL: http://localhost:8501).
2) Enter your Together AI API key in the input field.
3) Provide a query or prompt and click the Get Answer button.
4) View the individual responses and the aggregated response.


This project is designed to complement the blog post and demonstrate the practical application of the concepts shared there. If you have any questions or suggestions, feel free to reach out!
