def choose_best(c1, c2):
    # Simple scoring: choose longer caption
    return c1 if len(c1) > len(c2) else c2