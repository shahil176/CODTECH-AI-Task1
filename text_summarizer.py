from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

text = """
Artificial Intelligence (AI) is transforming industries worldwide.
It helps automate repetitive tasks, improve decision-making,
and increase efficiency. AI technologies such as machine learning,
natural language processing, and computer vision are widely used
in healthcare, finance, education, and cybersecurity.
AI continues to evolve rapidly and is becoming an essential part
of modern technology.
"""

parser = PlaintextParser.from_string(text, Tokenizer("english"))
summarizer = LsaSummarizer()

summary = summarizer(parser.document, 2)

print("Original Text:\n")
print(text)

print("\nSummary:\n")
for sentence in summary:
    print(sentence)