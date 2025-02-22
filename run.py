import json
import os

import numpy as np
import pandas as pd
import requests
from transformers import AutoTokenizer

from src.etl import flatten_data, load_data
from src.model import trace_model
from src.triton import generate_payload, parse_inference

# compile model
trace_model(model_path="/deploy/model")

# get and process data
data = load_data("/deploy/dataset/squadv2.json")
df = flatten_data(data)
df_sample = df.sample(n=10, random_state=2024)

# load tokenizer
tokenizer = AutoTokenizer.from_pretrained("/deploy/model", clean_up_tokenization_spaces=True)

# start triton
os.system("./triton/commands/start.sh &> server.out && sleep 10")  # noqa: S605

# Send Requests
URL = "http://localhost:8000/v2/models/tinyroberta/infer"

tracking = {
    "context": [],
    "question": [],
    "answer": [],
    "decoded": [],
    "start_idx": [],
    "pred_start_idx": [],
    "pred_end_idx": [],
}
for _i, row in df_sample.iterrows():
    # preprocess
    tokenized = tokenizer(row.question, row.context, return_tensors="np")
    input_ids = np.asarray(tokenized.input_ids, dtype=np.int32)
    attention_mask = np.asarray(tokenized.attention_mask, dtype=np.int32)
    payload = generate_payload(tokenized)
    # inference
    response = requests.post(URL, json=payload)  # noqa: S113
    # parse and track
    if response.status_code == 200:
        inference = json.loads(response.text)
        parsed = parse_inference(inference)
        start_idx, end_idx = parsed["start_idx"], parsed["end_idx"]
        decode_tokens = input_ids[0, start_idx : end_idx + 1]
        decoded = tokenizer.decode(decode_tokens)
        tracking["context"].append(row.context)
        tracking["question"].append(row.question)
        tracking["answer"].append(row.answer)
        tracking["decoded"].append(decoded)
        tracking["start_idx"].append(row.answer_start)
        tracking["pred_start_idx"].append(start_idx)
        tracking["pred_end_idx"].append(end_idx)
    else:
        raise Exception(f"Status code {response.status_code}")

results_df = pd.DataFrame.from_dict(tracking)

results_df.to_json("results/results.json", orient="records", indent=4)
