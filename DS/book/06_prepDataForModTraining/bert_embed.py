from transformers import DistilBertTokenizer


# balance between capturing majority of data, and not too much padding for most
MAX_SEQ_LEN = 64  
sample = (
    'I needed an antivirus application and know the quality of Norton '
    'products. This was a no brainer for me and I am glad it was so simple to '
    'get.')
tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')
tokens = tokenizer.tokenize(sample)
print(tokens)  # [i, needed, an, anti, ##virus, ...to, get, .]

encode_plus_tokens = tokenizer.encode_plus(
    text_input.text, pad_to_max_length=True, max_lenght=MAX_SEQ_LEN)
# Convert tokens to IDs from pre-trained BERT vocab
input_ids = encode_plus_tokens['input_ids']
print(input_ids)  # [101, 1045, 2734, ...0, 0, 0, 0] (end 0-padded)

input_mask = encode_plus_tokens['attention_mask']
print(input_mask)  # [1, 1, 1, ...0, 0, 0, 0] (mask actual content vs. padding)

segment_ids = [0] * MAX_SEQ_LEN
