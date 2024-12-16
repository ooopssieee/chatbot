import random
generated_numbers = set()

def generate_unique_random_number(start, end):
    if len(generated_numbers) >= (end - start + 1):
        raise ValueError("All unique numbers within the range have been generated.")
    
    while True:
        num = random.randint(start, end)
        if num not in generated_numbers:
            generated_numbers.add(num)
            return num
