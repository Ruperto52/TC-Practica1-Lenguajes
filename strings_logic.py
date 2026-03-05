def get_prefixes(string):
    """Calcula todos los prefijos de una cadena."""
    # Un prefijo va desde el inicio hasta cada posición i
    return [string[:i] for i in range(len(string) + 1)]

def get_suffixes(string):
    """Calcula todos los sufijos de una cadena."""
    # Un sufijo va desde cada posición i hasta el final
    return [string[i:] for i in range(len(string) + 1)]

def get_substrings(string):
    """Calcula todas las subcadenas posibles."""
    substrings = {""} # Iniciamos con la cadena vacía
    n = len(string)
    for i in range(n):
        for j in range(i + 1, n + 1):
            substrings.add(string[i:j])
    return sorted(list(substrings), key=len)
