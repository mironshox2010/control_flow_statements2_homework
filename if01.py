def main(a,b,c):
    """
    Find the largest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    dgf = a
    if a > b:
        if a > c:
            dgf = a
        else:
            dgf = c
    else:
        if b > c:
            dgf = b
        else:
            dgf = c
    return dgf
print(main(-5,-3,-1))
