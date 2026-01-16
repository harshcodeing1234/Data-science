# seek () function
with open('file.txt', 'r') as f:
  # Move to the 10th byte in the file
  f.seek(10)

  # Read the next 5 bytes
  data = f.read(5)
  print(data)

# tell () function
with open('file.txt', 'r') as f:
  # Read the first 10 bytes
  data = f.read()

  # Save the current position
  current_position = f.tell()

  # Seek to the saved position
  f.seek(current_position)