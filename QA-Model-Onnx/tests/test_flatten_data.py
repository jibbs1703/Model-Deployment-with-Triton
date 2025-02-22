import pytest
from src.etl import flatten_data, load_data

# Get and process data
data = load_data("/deploy/dataset/squadv2.json")
df = flatten_data(data)


# Test for flatten_data function
def test_flatten_data_columns():
    """
    Test to verify if the flattened DataFrame contains the expected columns.

    The test checks whether the columns in the DataFrame match the expected column
    names ['title', 'context', 'question', 'answer', 'answer_start', 'is_impossible'].
    """
    # Expected columns
    expected_columns = ["title", "context", "question", "answer", "answer_start", "is_impossible"]

    # Check if the DataFrame has the Specified columns
    assert list(df.columns) == expected_columns, "DataFrame does not have the specified columns"


def test_flatten_data_columns_count():
    """
    Test to verify if the flattened DataFrame has the correct number of columns.

    The test checks that the DataFrame contains exactly 6 columns, matching
    the expected structure after flattening.
    """

    # Check the DataFrame Column Count
    assert df.shape[1] == 6, "DataFrame does not have the correct number of columns"


def test_flatten_data_false_is_impossible():
    """
    Test to ensure all values in the 'is_impossible' column are False.

    This test checks that the 'is_impossible' column only contains False values,
    ensuring no True values exist in this column.
    """

    # Check if all 'is_impossible' values are Actually False
    assert df["is_impossible"].unique() == False, "Not all 'is_impossible' values are False"


def test_flatten_data_datatype():
    """
    Test to verify the data types of each column in the flattened DataFrame.

    This test checks that:
    - 'title', 'context', 'question', and 'answer' columns are of type 'object' (string).
    - 'answer_start' is of type 'int64'.
    - 'is_impossible' is of type 'bool'.
    """
    # Check the data types of each Dataframe Column
    assert df["title"].dtype == "object", "Title column is not of type 'object'"
    assert df["context"].dtype == "object", "Context column is not of type 'object'"
    assert df["question"].dtype == "object", "Question column is not of type 'object'"
    assert df["answer"].dtype == "object", "Answer column is not of type 'object'"
    assert df["answer_start"].dtype == "int64", "Answer start column is not of type 'int64'"
    assert df["is_impossible"].dtype == "bool", "Is_impossible column is not of type 'bool'"


if __name__ == "__main__":
    pytest.main()
