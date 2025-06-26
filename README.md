# AI-Powered Sentiment Analysis

A Python application that leverages AI21's Maestro API to perform intelligent sentiment analysis on product reviews.

## Overview

a tool designed to analyze product reviews and classify their sentiment as Positive, Neutral, Negative, Mixed, or Irrelevant. The application focuses specifically on product-related sentiment, filtering out comments about shipping, customer service, or other non-product aspects.

## Features

- Automated sentiment analysis of product reviews
- Classification into five sentiment categories (Positive, Neutral, Negative, Mixed, Irrelevant)
- Focus on product-specific sentiment only
- Explanations provided for each sentiment classification
- Batch processing of multiple reviews
- Results saved to a structured output file

## Requirements

- Python 3.6+
- AI21 API key

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/maestro.git
   cd maestro
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv myenv
   source myenv/bin/activate  # On Windows: myenv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root and add your AI21 API key:
   ```
   AI21_API_KEY=your_api_key_here
   ```

## Usage

### Analyzing Reviews

1. Place your reviews in the `reviews.txt` file, with one review per line.

2. Run the analyzer:
   ```
   python analyzer.py
   ```

3. View the results in `sentiment_analysis_results.txt`

### Example

Input (`reviews.txt`):
```
This product exceeded my expectations. The quality is outstanding!
The delivery was late, but the product works fine.
I'm disappointed with the durability. It broke after just two weeks.
```

Output (`sentiment_analysis_results.txt`):
```
Review: This product exceeded my expectations. The quality is outstanding!
Analysis: Positive - The review expresses high satisfaction with the product quality and indicates it exceeded expectations.

Review: The delivery was late, but the product works fine.
Analysis: Neutral - While there was an issue with delivery (non-product aspect), the product itself works as expected without exceptional praise or criticism.

Review: I'm disappointed with the durability. It broke after just two weeks.
Analysis: Negative - The review specifically mentions poor durability, which is a product attribute, and indicates product failure.
```

## Project Structure

- `analyzer.py`: Main script for processing reviews and generating sentiment analysis
- `maestro.py`: Example implementation of AI21's Maestro API
- `reviews.txt`: Input file containing reviews to analyze
- `sentiment_analysis_results.txt`: Output file with analysis results
- `requirements.txt`: Python dependencies
- `.env`: Environment variables (API key)

## License

[Your License Here]

## Acknowledgments

- This project uses the [AI21 Maestro API](https://www.ai21.com/blog/introducing-maestro) for sentiment analysis
