from parameterized import parameterized

from ..vocab import Vocab

from copy import deepcopy

empty = []
letters = list('abcdefghijklmnopqrstuvwxyz')

all_combos = [(init_words, oov, bos, eos)
              for init_words in [None, empty, letters]
              for oov in [None, '_OOV_']
              for bos in [None, '_BOS_']
              for eos in [None, '_EOS_']]


def test_get_index():
    in_vocab = letters[:6]
    out_of_vocab = letters[6:]
    oov = '_OOV_'
    vocab = Vocab(in_vocab, oov=oov)
    for term in in_vocab:
        assert vocab.get_index(term) == 1 + in_vocab.index(term)
    oov_id = vocab.get_index(oov)
    for term in out_of_vocab:
        assert vocab.get_index(term, grow_if_missing=False) == oov_id
    for term in out_of_vocab:
        term_id = vocab.get_index(term, grow_if_missing=True)
        assert term_id == len(vocab) - 1


@parameterized(all_combos)
def test_vocab_extra_indices(init_words, oov, bos, eos):

    vocab = Vocab(init_words, oov, bos, eos)
    extra_indices = 0
    if oov:
        extra_indices += 1
    if bos:
        extra_indices += 1
    if eos:
        extra_indices += 1
    assert len(vocab) == extra_indices + vocab.init_size

    if oov:
        assert vocab.get_index(oov) is not None
    assert vocab.oov == oov

    if bos:
        assert vocab.get_index(bos) is not None
    assert vocab.bos == bos

    if eos:
        assert vocab.get_index(eos) is not None
    assert vocab.eos == eos


@parameterized(all_combos)
def test_vocab_growth(init_words, oov, bos, eos):

    vocab = Vocab(init_words, oov, bos, eos)

    # do not grow
    prev_len = len(vocab)
    unk_index = vocab.get_index('@', grow_if_missing=False)
    assert unk_index == vocab.oov_idx
    assert len(vocab) == prev_len

    # do grow
    prev_len = len(vocab)
    unk_index = vocab.get_index('@', grow_if_missing=True)
    assert unk_index != vocab.oov_idx
    assert len(vocab) == prev_len + 1
    assert unk_index == prev_len


@parameterized(all_combos)
def test_vocab_clone(init_words, oov, bos, eos):
    """This is to show that is possible to easily clone vocabularies"""
    old_vocab = Vocab(init_words, oov, bos, eos)
    new_vocab = deepcopy(old_vocab)

    assert len(old_vocab) == len(new_vocab)
    assert old_vocab.oov == new_vocab.oov
    assert old_vocab.bos == new_vocab.bos
    assert old_vocab.eos == new_vocab.eos

    new_vocab.get_index('@', grow_if_missing=True)
    assert len(old_vocab) == len(new_vocab) - 1
