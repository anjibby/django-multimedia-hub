def generate_fibonacci(n):
    """
    Generates a list containing the Fibonacci sequence up to n terms.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]

    # Initialize the first two numbers of the sequence
    sequence = [0, 1]

    # Generate subsequent terms up to n
    for i in range(2, n):
        next_term = sequence[-1] + sequence[-2]  # Sum of the last two elements
        sequence.append(next_term)

    return sequence

# Example Usage & Testing
if __name__ == "__main__":
    num_terms = 10
    fib_series = generate_fibonacci(num_terms)
    print(f"Fibonacci sequence ({num_terms} terms): {fib_series}")

