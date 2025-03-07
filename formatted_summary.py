from langchain_core.messages import HumanMessage, SystemMessage
from main import article
from langchain_openai import ChatOpenAI

# we get the article data from the scraping part
article_title = article.title
article_text = article.text

# prepare template for prompt
template = """You are a very good assistant that summarizes online articles.

Here's the article you want to summarize.

==================
Title: {article_title}

{article_text}
==================

Now, provide a summarized version of the article in a bulleted list format and in Indonesian
"""

prompt = template.format(article_title=article.title, article_text=article.text)

messages = [HumanMessage(content=prompt)]

chat = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.7)

# generates summary
summary = chat.invoke(messages) 
print(summary.content)