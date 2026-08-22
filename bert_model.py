import torch

from transformers import BertTokenizer
from transformers import BertForSequenceClassification

from config import BERT_MODEL

tokenizer = BertTokenizer.from_pretrained(
    BERT_MODEL
)

model = BertForSequenceClassification.from_pretrained(
    BERT_MODEL,
    num_labels=2
)

def bert_predict(text):

    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=128
    )

    outputs = model(**inputs)

    probs = torch.softmax(
        outputs.logits,
        dim=1
    )

    pred = torch.argmax(probs).item()

    confidence = probs.max().item()

    return pred, confidence