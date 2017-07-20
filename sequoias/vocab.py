import itertools as it


class Vocab:
    """A mapping between TERMs and IDs

       Additionally might add special tokens for:
         - begin-of-sequence
         - end-of-sequence
         - out-of-vocabulary
    """
    def __init__(self, init_terms, oov=None, bos=None, eos=None, name=None):
        self.init_terms = init_terms if init_terms is not None else []
        self.init_size = len(self.init_terms)
        self.name = name

        # special tokens
        specials = []
        if oov is not None:
            specials.append(oov)
        if bos is not None:
            specials.append(bos)
        if eos is not None:
            specials.append(eos)

        # add init tokens
        self._index_to_term = [t for t in it.chain(specials, self.init_terms)]
        self._term_to_index = {t: i for i, t in enumerate(self._index_to_term)}
        self.oov_idx = None
        self.oov = oov
        self.oov_idx = self.get_index(oov, grow_if_missing=False) \
            if oov is not None else None

        self.bos = bos
        self.bos_idx = self.get_index(bos, grow_if_missing=False) \
            if bos is not None else None

        self.eos = eos
        self.eos_idx = self.get_index(eos, grow_if_missing=False) \
            if eos is not None else None

    def get_index(self, term, grow_if_missing=False):
        """Return the index of a given term
           `grow_if_missing` defines the behaviour for new terms
              - True:  term is added to user_vocab, new index is returned
              - False: term is NOT added to user_vocab, `oov_index` is returned
        """
        if grow_if_missing and term not in self._term_to_index:
            self._index_to_term.append(term)
            self._term_to_index[term] = len(self._index_to_term) - 1
        return self._term_to_index.get(term, self.oov_idx)

    def get_term(self, index):
        """Return the term given an index"""
        return self._index_to_term[index]

    def __eq__(self, other):
        return isinstance(other, Vocab) and \
            self._index_to_term == other._index_to_term

    def __len__(self):
        return len(self._index_to_term)

    def __repr__(self):
        return 'Vocab(%s)' % self.name

    def __iter__(self):
        return iter(self._index_to_term)

    def __contains__(self, key):
        return key in self._index_to_term

    @classmethod
    def empty(cls):
        return cls(init_terms=[])

    @classmethod
    def from_unigram_file(cls, unig_file,
                          max_len=None, oov=None, bos=None, eos=None):
        """Factory to initialise Vocab from unigram file"""
        with open(unig_file) as vf:
            init_words = [line.split()[0] for line in it.islice(vf, max_len)]
            return cls(init_words, oov=oov, bos=bos, eos=eos)
