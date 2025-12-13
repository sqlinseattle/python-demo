
import random

def rand_int_1_10() -> int:
	"""Return a random integer between 1 and 10 inclusive."""
	return random.randint(1, 10)

def rand_float_0_1() -> float:
	"""Return a random float between 0.0 and 1.0."""
	return random.random()

def rand_randrange_1_9() -> int:
	"""Return a random integer from 1 to 9 (randrange semantics)."""
	return random.randrange(1, 10)

def rand_uniform_1_10() -> float:
	"""Return a random float between 1.0 and 10.0."""
	return random.uniform(1, 10)

def heads_or_tails() -> str:
    """Simulate a coin flip, returning 'Heads' or 'Tails'."""
    return "Heads" if random.choice([True, False]) else "Tails"

def heads_or_tails2() -> str:
    """Simulate a coin flip and return a concatenated string result.

    Converts the numeric flip result to a string before concatenation so the
    returned value is always a string (for example: "0 Heads" or "1 Tails").
    """
    result = random.randint(0, 1)
    result_str = str(result)
    if result == 0:
        return str(result) + " Heads"
    elif result == 1:
        return str(result) + " Tails"
    else:
        raise ValueError("Unexpected value from random.randint")
    

