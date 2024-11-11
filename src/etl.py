import json
from typing import List
import pandas as pd


def load_data(path: str) -> List[dict]:
    """Load data from squadv2.json"""
    with open(path) as f:
        data = json.load(f)["data"]
    return data


def flatten_data(data: List[dict]) -> pd.DataFrame:
    """Flatten nested json data and convert to dataframe.

    Input
    -----
    data loaded from load_data()

    Output
    ------
    df columns:
        title: object
        context: object
        question: object
        answer: object
        answer_start: int64
        is_impossible: bool
    
    Note: all is_impossible values should be False!

    Example Output
    --------------
    >>> df.iloc[1000]
    title                                              Frédéric_Chopin
    context          Two Polish friends in Paris were also to play ...
    question         What nationality were the two friends who serv...
    answer                                                      Polish
    answer_start                                                     4
    is_impossible                                                False
    Name: 1000, dtype: object
    """

    # After Initial Examination, the Data Appears to be Well-Defined
    # Hence, no need to use a Recursive Function for this Transformation

    df = pd.json_normalize(
        data,
        record_path=['paragraphs', 'qas', 'answers'],  # Expands 'answers'
        meta=[
            ['title'],  # Article title
            ['paragraphs', 'context'],  # Context of the paragraph
            ['paragraphs', 'qas', 'question'],  # Question text
            ['paragraphs', 'qas', 'is_impossible']  # Is the question unanswerable?
        ]
    )

    # Rename columns to Match Documentation Docstring
    df.rename(columns={'text': 'answer', 'paragraphs.context': 'context', 'paragraphs.qas.question': 'question',
                       'paragraphs.qas.is_impossible': 'is_impossible'}, inplace=True)

    # Select Required Columns into DataFrame
    df = df[['title', 'context', 'question', 'answer', 'answer_start', 'is_impossible']]

    # Specify Correct Datatypes in Dataframe Columns
    df['title'] = df['title'].astype('object')
    df['context'] = df['context'].astype('object')
    df['question'] = df['question'].astype('object')
    df['answer'] = df['answer'].astype('object')
    df['answer_start'] = df['answer_start'].astype('int64')
    df['is_impossible'] = df['is_impossible'].astype('bool')


    return df