def sum(seq):
    if not seq:
        return 0
    else:
        return seq[0] + sum(seq[1:])
