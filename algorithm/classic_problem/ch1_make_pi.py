def calculate_pi(n_terms: int) -> float:
    """Calculate pi value with 'Leibniz formula'
    
    Formula
    -------
        pi = 4/1 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 ...

    Parameters
    ----------
    n_terms: int
        n th terms for calculating pi value
    
    Returns
    -------
    float:
        pi value until n th terms from formula
    """
    
    numerator = 4.0
    denominator = 1.0
    operation = 1.0

    pi = 0
    for _ in range(n_terms):
        pi += numerator * operation / denominator
        operation *= -1
        denominator += 2
    return pi

def main():
    pi = calculate_pi(1000)
    print(pi)
main()