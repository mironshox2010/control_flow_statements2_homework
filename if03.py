def main(a,b,c):
    """
    Determine the number between large and small.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    dgf = a
    if a < b:
        if a > c:
            dgf = a
    if a > b:
        if b > c:
            dgf = b
    if a > c:
        if b < c:
            dgf = c

    return dgf

print(main(1,4,2))

    