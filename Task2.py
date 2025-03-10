output_file = "output.txt"

# Step 1:
text_to_write = input("Enter text to write to the file: ")
with open(output_file, 'w') as file:
    file.write(text_to_write + '\n')
print(f"Data successfully written to {output_file}.")

# Step 2:
additional_text = input("Enter additional text to append: ")
with open(output_file, 'a') as file:
    file.write(additional_text + '\n')
print("Data successfully appended.")

# Step 3:
print(f"\nFinal content of {output_file}:")
with open(output_file, 'r') as file:
    content = file.read()
    print(content)