file_path = 'numbers.txt'

try:
    with open(file_path, 'r') as file:
        numbers = [float(line.strip()) for line in file.readlines()]

        if numbers:
            max_number = max(numbers)
            print("The largest number in the file is:", max_number)
        else:
            print("The file is empty.")

except FileNotFoundError:
    print("File not found:", file_path)
except ValueError:
    print("Invalid number format in the file.")
except Exception as e:
    print("An error occurred:", str(e))