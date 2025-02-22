import pytest

from src.etl import flatten_data, load_data

# Get and process data
data = load_data("/deploy/dataset/squadv2.json")
# data = load_data("C:/Users/ameen/Downloads/squadv2.json")
df = flatten_data(data)


def test_flatten_data_columns():
    """
    Test to verify if the flattened DataFrame contains the expected columns.

    The test checks whether the columns in the DataFrame match the expected column
    names ['title', 'context', 'question', 'answer', 'answer_start', 'is_impossible'].
    """
    # Expected columns
    expected_columns = ["title", "context", "question", "answer", "answer_start", "is_impossible"]

    # Check if the DataFrame has the Specified columns
    if list(df.columns) != expected_columns:
        raise AssertionError("DataFrame does not have the specified columns")


def test_flatten_data_columns_count():
    """
    Test to verify if the flattened DataFrame has the correct number of columns.

    The test checks that the DataFrame contains exactly 6 columns, matching
    the expected structure after flattening.
    """

    # Check the DataFrame Column Count
    if df.shape[1] != 6:
        raise AssertionError("DataFrame does not have the correct number of columns")


def test_flatten_data_false_is_impossible():
    """
    Test to ensure all values in the 'is_impossible' column are False.

    This test checks that the 'is_impossible' column only contains False values,
    ensuring no True values exist in this column.
    """

    # Check if all 'is_impossible' values are Actually False
    if not (df["is_impossible"].unique() == False).all():  # noqa: E712
        raise AssertionError("Not all 'is_impossible' values are False")


def test_flatten_data_datatype():
    """
    Test to verify the data types of each column in the flattened DataFrame.

    This test checks that:
    - 'title', 'context', 'question', and 'answer' columns are of type 'object' (string).
    - 'answer_start' is of type 'int64'.
    - 'is_impossible' is of type 'bool'.
    """
    # Check the data types of each Dataframe Column
    if df["title"].dtype != "object":
        raise AssertionError("Title column is not of type 'object'")
    if df["context"].dtype != "object":
        raise AssertionError("Context column is not of type 'object'")
    if df["question"].dtype != "object":
        raise AssertionError("Question column is not of type 'object'")
    if df["answer"].dtype != "object":
        raise AssertionError("Answer column is not of type 'object'")
    if df["answer_start"].dtype != "int64":
        raise AssertionError("Answer start column is not of type 'int64'")
    if df["is_impossible"].dtype != "bool":
        raise AssertionError("Is_impossible column is not of type 'bool'")


if __name__ == "__main__":
    pytest.main()
