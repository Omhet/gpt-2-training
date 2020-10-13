import sentencepiece as spm
spm.SentencePieceTrainer.train(input='input.txt', model_prefix='sp',
                               vocab_size=50257, user_defined_symbols=['<|n|>', '<|endoftext|>'],
                               input_sentence_size=10000000, max_sentence_length=32768,
                               model_type='bpe', character_coverage=1)
