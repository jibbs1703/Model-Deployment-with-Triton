import numpy as np


def generate_payload(inputs):
    """Construct payload for use by inference server."""
    payload = {
        "inputs": [
            {
                "name": "input_ids",
                "shape": inputs.input_ids.shape,
                "datatype": "INT32",
                "data": inputs.input_ids[0].tolist(),
            },
            {
                "name": "attention_mask",
                "shape": inputs.attention_mask.shape,
                "datatype": "INT32",
                "data": inputs.attention_mask[0].tolist(),
            },
        ]
    }
    return payload


def parse_inference(inference: dict) -> dict:
    """Parse Triton inference response."""
    parsed = {}
    for output in inference["outputs"]:
        if output["name"] == "start_idx_logits":
            parsed["start_idx"] = np.argmax(output["data"])
        elif output["name"] == "end_idx_logits":
            parsed["end_idx"] = np.argmax(output["data"])
        else:
            raise Exception("No 'start_idx' or 'end_idx'")
    return parsed
