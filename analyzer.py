import os
from ai21 import AI21Client

# Initialize the AI21 client
client = AI21Client(api_key=os.environ.get("AI21_API_KEY"))

# Define the prompt
prompt = (
    "Please analyze the sentiment of the following product review.\n"
    "Return one of the following labels: Positive, Neutral, Negative, Mixed, or Irrelevant.\n"
    "Only evaluate the product itself (not customer service, shipping, etc.).\n"
    "Include a short explanation for each.\n\n"
)

def analyze_sentiment(response):
    if response.status == 'completed':
        if hasattr(response, 'result') and response.result:
            return response.result
        else:
            return "No result available in response"
    else:
        return f"Analysis failed with status: {response.status}"

def read_reviews(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()

def write_results(file_path, results):
    with open(file_path, 'w', encoding='utf-8') as file:
        for review, analysis in results:
            file.write(f"Review: {review.strip()}\n")
            file.write(f"Analysis: {analysis.strip()}\n\n")

def main():
    input_file = "reviews.txt"  # Change this to your input file name
    output_file = "sentiment_analysis_results.txt"  # Change this to your desired output file name

    reviews = read_reviews(input_file)

    results = []
    for review in reviews:
        try:
            response = client.beta.maestro.runs.create_and_poll(
                requirements=[
                    {
                        "name": "Label Format",
                        "description": "Each review must be labeled as Positive, Neutral, Negative, Mixed, or Irrelevant.",
                        "is_mandatory": True,
                    },
                    {
                        "name": "Product-Focused Sentiment Only",
                        "description": "Only analyze sentiment if it refers to the product itself.",
                        "is_mandatory": True,
                    },
                    {
                        "name": "Explanation Requirement",
                        "description": "Include a short explanation for each sentiment label.",
                        "is_mandatory": True,
                    },
                ],
                models=["jamba-mini-1.6"],
                output_type={"type": "string"},
                budget="medium",
                input=prompt + review
            )
            analysis = analyze_sentiment(response)
            results.append((review, analysis))
            print(f"Processed review: {review.strip()}")
            print(f"Analysis: {analysis}\n")
        except Exception as e:
            print(f"Error processing review: {review.strip()}")
            print(f"Error message: {str(e)}")

    write_results(output_file, results)
    print(f"Analysis complete. Results written to {output_file}")

if __name__ == "__main__":
    main()
