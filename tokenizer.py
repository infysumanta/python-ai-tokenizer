from vocab import token_to_id, id_to_token

class Tokenizer:
    def __init__(self):
        self.token_to_id = token_to_id
        self.id_to_token = id_to_token
        self.vocab_size_value = len(self.token_to_id)
	
    def tokenize(self, text):
        return list(text) 

    def encode(self, text):
        return [self.token_to_id.get(char, self.token_to_id['<UNK>']) for char in self.tokenize(text)]

    def decode(self, token_ids):
        return ''.join([self.id_to_token.get(id_, '<UNK>') for id_ in token_ids])

    def vocab_size(self):
        return self.vocab_size_value

    def tokens_to_string(self, tokens):
        return ''.join(tokens)

    def string_to_tokens(self, string):
        return self.tokenize(string)

    def print_vocab(self, limit=None):
        for i, (char, idx) in enumerate(self.token_to_id.items()):
            if limit and i >= limit:
                break
            print(f"{repr(char)}: {idx}")
