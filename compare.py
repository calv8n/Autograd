def compare_text_files(file1_path, file2_path):
    try:
        with open(file1_path, "r", encoding="utf-8") as file1, open(
            file2_path, "r", encoding="utf-8"
        ) as file2:
            lines1 = file1.readlines()
            lines2 = file2.readlines()

            # Compare line by line
            for i, (line1, line2) in enumerate(zip(lines1, lines2), start=1):
                if line1 != line2:
                    print("Error at {i}")
                    return False

            # Check if one file is longer than the other
            if len(lines1) != len(lines2):
                print(f"Files have different number of lines.")
                return False

            print("Files are identical.")
            return True

    except FileNotFoundError as e:
        print(f"Error: {e.filename} not found.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


# Example usage
file1_path = "output_admin.txt"
file2_path = "output_student.txt"
compare_text_files(file1_path, file2_path)
