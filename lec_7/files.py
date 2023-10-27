while True:
    file_name = input("Enter the name of the text file you want to open: ")

    try:
        with open(file_name, 'r') as txt_file:
            content = txt_file.read()
            print("File content:")
            print(content)

        option = input(" Please enter 'w' to write to the current file, 'n' to write to a new file, or 'q' to quit. ").lower()

        if option == 'w':
            with open(file_name, 'a') as txt_file:
                new_content = input("Enter the content you want to write: ")
                txt_file.write(new_content)
                print("Content has been successfully written to the file.")
                txt_file.close()
        elif option == 'n':
            new_txt_file_name = input("Enter the name of the new file: ")
            new_content = input("Enter the content you want to write to the new file: ")
            try:
                with open(new_txt_file_name, 'w') as new_txt_file:
                    new_txt_file.write(new_content)
                    print("Content has been successfully written to the new file.")
                    new_txt_file.close()
            except FileNotFoundError:
                print("Error: The new file could not be created. Please enter a valid filename.")

        elif option == 'q':
            print("Quitting the program.")
            break
        else:
            print("Invalid option. Please enter 'w' to write to the current file, 'n' to write to a new file, or 'q' to quit.")

    except FileNotFoundError:
        print("Error: The file does not exist. Please enter a valid filename.")
    except ValueError:
        print("Error: Invalid input. Please enter a valid filename.")
    finally:
        print("File has been closed.")

