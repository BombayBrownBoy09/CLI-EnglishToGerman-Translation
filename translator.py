import requests
from bs4 import BeautifulSoup
import click
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer


def translate(input_text, min_length, max_length, model, tokenizer):
    inputs = tokenizer(
    "translate English to German: Hugging Face is a technology company based in New York and Paris",
    return_tensors="pt")
    outputs = model.generate(inputs["input_ids"], max_length=max_length, num_beams=4, early_stopping=True)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)


@click.command()
@click.option(
    "--url",
    type=str,
    default="https://en.wikipedia.org/wiki/Monarchy_of_Germany",
)
def get_and_translate(url):
    """
    It takes a URL, downloads the article text, and translates it to german
    :param url: The URL of the article you want to summarize
    """
    # Load model & tokenizer
    model = model = AutoModelForSeq2SeqLM.from_pretrained("t5-base")
    tokenizer = AutoTokenizer.from_pretrained("t5-base")
    
    # Set desired target min and max length for translation (not strict bounds)
    min_length = 50
    max_length = 200
    
    # translate
    article_text = get_article_text(url)
    translation = translate(
        article_text, min_length, max_length, model, tokenizer
    )
    # Clean up output formatting
    translation = translation.split("</s>")[-2].split("<s>")[-1].strip()
    print("Summary: ")
    print(summary)


def get_article_text(wiki_url):
    # Get article from Wiki
    page = requests.get(wiki_url)
    soup = BeautifulSoup(page.content, "html.parser")

    # Extract body text
    bodytext = soup.find_all("p")
    bodytext = [i.text for i in bodytext]
    article_text = " ".join(bodytext)
    return article_text


if __name__ == "__main__":
    summarize()  # pylint: disable=no-value-for-parameter
