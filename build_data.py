from model.config import Config
from model.data_utils import Dataset, get_vocabs, PAD, UNK, NUM, EOS, BOS, \
    get_wordvec_vocab, write_vocab, load_vocab, get_char_vocab, \
    export_trimmed_wordvec_vectors, export_trimmed_wordvec_vectors_bin, \
    get_processing_word
import argparse

parser = argparse.ArgumentParser()


def main():
    """Procedure to build data

    You MUST RUN this procedure. It iterates over the whole dataset (train,
    dev and test) and extract the vocabularies in terms of words, tags, and
    characters. Having built the vocabularies it writes them in a file. The
    writing of vocabulary in a file assigns an id (the line #) to each word.
    It then extract the relevant GloVe vectors and stores them in a np array
    such that the i-th entry corresponds to the i-th word in the vocabulary.


    Args:
        config: (instance of Config) has attributes like hyper-params...

    """
    # get config and processing of words
    config = Config(parser, load=False)
    processing_word = get_processing_word(lowercase=True)

    # Generators
    dev   = Dataset(config.filename_dev, processing_word)
    test  = Dataset(config.filename_test, processing_word)
    train = Dataset(config.filename_train, processing_word)

    # Build Word and Tag vocab
    vocab_words, vocab_tags = get_vocabs([train, dev, test])
    vocab = list(vocab_words)
    vocab = [PAD, UNK, BOS, EOS] + vocab + [NUM]

    # Save vocab
    write_vocab(vocab, config.filename_words)
    write_vocab(vocab_tags, config.filename_tags)

    # Trim Embedding Vectors
    vocab = load_vocab(config.filename_words)
    export_trimmed_wordvec_vectors(vocab, config.filename_wordvec,
                                config.filename_wordvec_trimmed)

    # Build and save char vocab
    train = Dataset(config.filename_train)
    vocab_chars = get_char_vocab(train)
    write_vocab(vocab_chars, config.filename_chars)


if __name__ == "__main__":
    main()
