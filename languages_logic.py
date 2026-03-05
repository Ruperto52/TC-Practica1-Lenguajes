import itertools

def get_kleene_closure(alphabet, max_len):
    """Genera la cerradura de Kleene (Sigma*) hasta longitud n."""
    result = ["λ"] # Cadena vacía representada por lambda
    for i in range(1, max_len + 1):
        combinations = itertools.product(alphabet, repeat=i)
        result.extend([''.join(c) for c in combinations])
    return result

def get_positive_closure(alphabet, max_len):
    """Genera la cerradura positiva (Sigma+)."""
    result = []
    for i in range(1, max_len + 1):
        combinations = itertools.product(alphabet, repeat=i)
        result.extend([''.join(c) for c in combinations])
    return result
