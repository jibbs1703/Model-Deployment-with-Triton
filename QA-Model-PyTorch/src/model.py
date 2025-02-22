import torch
from transformers import AutoModelForQuestionAnswering, AutoTokenizer


def trace_model(model_path: str) -> None:
    """Compile and save PyTorch model."""
    tokenizer = AutoTokenizer.from_pretrained(model_path, clean_up_tokenization_spaces=True)

    question = "Who jumped over the dog?"
    context = "The quick brown fox jumps over the lazy dog"

    example_input = tokenizer(question, context, return_tensors="pt")

    qa_model = AutoModelForQuestionAnswering.from_pretrained(model_path, return_dict=False)

    input_ids = example_input["input_ids"]
    attn_mask = example_input["attention_mask"]

    traced_model = torch.jit.trace(qa_model, [input_ids, attn_mask])

    torch.jit.save(traced_model, "/deploy/triton/model-repo/tinyroberta/1/model.pt")
