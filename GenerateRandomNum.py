import random

num_numbers = 100000

min_value = 1
max_value = 10**63

random_numbers = [random.randint(min_value, max_value) for _ in range(num_numbers)]

print("Numbers Finished Generating")

output_file_path = 'numbers.txt'
with open(output_file_path, 'w') as output_file:
    for number in random_numbers:
        output_file.write(str(number) + '\n')

print("Random numbers saved to", output_file_path)
