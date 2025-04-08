# The vocabulary includes:
# - Special tokens: PAD (padding) and UNK (unknown)
# - Lowercase letters (a-z)
# - Uppercase letters (A-Z) 
# - Digits (0-9)
# - Common punctuation and special characters

vocab_chars = [
    '<PAD>', '<UNK>',
    *list("abcdefghijklmnopqrstuvwxyz"),
    *list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
    *list("0123456789"),
    ' ', '.', ',', '!', '?', ':', ';', '"', "'", '-', '_',
    '(', ')', '[', ']', '{', '}', '/', '\\', '@', '#', '$',
    '%', '^', '&', '*', '+', '=', '<', '>', '`', '~'
]


token_to_id = {char: idx for idx, char in enumerate(vocab_chars)}
id_to_token = {idx: char for idx, char in enumerate(vocab_chars)}