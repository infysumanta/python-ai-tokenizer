from tokenizer import Tokenizer

def main():
    tokenizer = Tokenizer()
    text = "AI is the future of technology. It is a powerful tool that can help us solve complex problems and improve our lives."
    print(f"Original: {text}")

    encoded = tokenizer.encode(text)
    print("Encoded:", encoded)

    decoded = tokenizer.decode(encoded)
    print("Decoded:", decoded)

    print("Vocab Size:", tokenizer.vocab_size())
    tokenizer.print_vocab(limit=15)

if __name__ == '__main__':
    main()