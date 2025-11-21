from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException

from dotenv import load_dotenv
load_dotenv()

llm = ChatGroq(model_name="llama-3.3-70b-versatile")


# Mock function to extract financial data (replace with actual function)
def extract(article_text):
    prompt = '''
    From the below news article, extract revenue and eps in JSON format containing the
    following keys: 'revenue_actual', 'revenue_expected', 'eps_actual', 'eps_expected'. 

    Each value should have a unit such as million or billion.

    Only return the valid JSON. No preamble.

    Article
    =======
    {article}
    '''

    pt = PromptTemplate.from_template(prompt)

    global llm

    chain = pt | llm
    response = chain.invoke({'article': article_text})
    parser = JsonOutputParser()

    try:
        res = parser.parse(response.content)
    except OutputParserException:
        raise OutputParserException("Context too big. Unable to parse jobs.")

    return res