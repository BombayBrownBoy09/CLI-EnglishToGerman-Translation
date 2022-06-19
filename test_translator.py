from wiki_summarizer import get_article_text, summarize
from click.testing import CliRunner


def test_get_article_text():
    article_txt = get_article_text(
        "https://en.wikipedia.org/wiki/Monarchy_of_Germany"
    )
    assert article_txt.__contains__(
        "This empire was a federal monarchy"
    )
    assert len(article_txt) > 100


def test_summarize():
    runner = CliRunner()
    result = runner.invoke(
        translate,
        ["https://en.wikipedia.org/wiki/Monarchy_of_Germany"],
    )
    assert len(result.output) > 20