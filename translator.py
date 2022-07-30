import requests
from bs4 import BeautifulSoup
import click
from transformers import pipeline


def translate(article_text):
    translator = pipeline("translation_en_to_de")
    translation = translator(article_text)
    return translation


@click.command()
@click.option(
    "--url",
    type=str,
    default="https://en.wikipedia.org/wiki/Monarchy_of_Germany",
)
def get_and_translate(url):
    """
    It takes a URL, downloads the article text, and translates it to german
    """
    # Load model & tokenizer
#     model = model = AutoModelForSeq2SeqLM.from_pretrained("t5-base")
#     tokenizer = AutoTokenizer.from_pretrained("t5-base")
    
#     # Set desired target min and max length for translation (not strict bounds)
#     min_length = 50
#     max_length = 200
    
    # translate
    article_text = get_article_text(url)
    translation = translate(
        article_text)
    # Clean up output formatting
#     translation = translation.split("</s>")[-2].split("<s>")[-1].strip()
    print("Translation: ")
    print(translation)


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
    get_and_translate()  # pylint: disable=no-value-for-parameter
