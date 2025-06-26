import os
from ai21 import AI21Client

client = AI21Client(api_key=os.environ.get("AI21_API_KEY"))
client.beta.maestro.runs.create_and_poll(
		requirements=[
				{
						"name": "Label Format",
						"description": "Each review must be labeled as Positive, Neutral, Negative, Mixed, or Irrelevant.",
						"is_mandatory": False,
				},
				{
						"name": "Product-Focused Sentiment Only",
						"description": "Only analyze sentiment if it refers to the product itself.",
						"is_mandatory": False,
				},
				{
						"name": "Explanation Requirement",
						"description": "Include a short explanation for each sentiment label.",
						"is_mandatory": False,
				},
		],
		models=[
				"jamba-1-6-mini-planning"
		],
		output_type={
				"type": "string"
		},
		budget="medium",
)
