import json
import os
import numpy as np
import pandas as pd
import requests

from src.etl import flatten_data, load_data
from src.model import trace_model
from src.triton import generate_payload, parse_inference
from transformers import AutoTokenizer

# compile model
trace_model(model_path="/deploy/model")

# get and process data
data = load_data("/deploy/dataset/squadv2.json")
df = flatten_data(data)
df_sample = df.sample(n=10, random_state=2024)

# load tokenizer
tokenizer = AutoTokenizer.from_pretrained(
    "/deploy/model", clean_up_tokenization_spaces=True
)