def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n): 
        yield a
        a, b = b, a + b

# Run test
if __name__ == "__main__":
    n_terms = 10
    print(f"First {n_terms} terms of Fibonacci series:")
    print(list(fibonacci_generator(n_terms)))