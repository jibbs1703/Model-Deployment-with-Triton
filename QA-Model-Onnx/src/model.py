import torch
from transformers import AutoModelForQuestionAnswering, AutoTokenizer


def trace_model(model_path: str) -> None:
    """Compile and save PyTorch model in .onnx Format"""

    # Load the Tokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_path, clean_up_tokenization_spaces=True)
    # Tokenize the Example Input
    question = "Who jumped over the dog?"
    context = "The quick brown fox jumps over the lazy dog"
    example_input = tokenizer(question, context, return_tensors="pt")

    #  Load the Pre-Trained QA model
    qa_model = AutoModelForQuestionAnswering.from_pretrained(model_path, return_dict=False)

    # Set Model to evaluation mode
    qa_model.eval()

    # Extract the necessary inputs
    input_ids = example_input["input_ids"]
    attn_mask = example_input["attention_mask"]

    # Export the model to ONNX
    torch.onnx.export(
        qa_model,
        (input_ids, attn_mask),
        "/deploy/triton/model-repo/tinyroberta/1/model.onnx",
        input_names=["input_ids", "attention_mask"],
        output_names=["start_idx_logits", "end_idx_logits"],
        dynamic_axes={
            "input_ids": {0: "batch_size", 1: "seq_len"},
            "attention_mask": {0: "batch_size", 1: "seq_len"},
            "start_idx_logits": {0: "batch_size", 1: "seq_len"},
            "end_idx_logits": {0: "batch_size", 1: "seq_len"},
        },
        opset_version=14,
    )
