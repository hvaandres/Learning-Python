# Open your terminal
# Write the following code

file_builder = open("logger.txt" . "w+")

for i in range(10):
  file_builder.write(f"I'm on line {i + 1 }\n")

# file_builder.write("Hey, I'm in a file!")

file_builder.close()