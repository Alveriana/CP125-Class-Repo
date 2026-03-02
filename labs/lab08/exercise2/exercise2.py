# Lab 08 Exercise 2: Text File Merger
# Write your code below:

def merge_lists(file1, file2, output_file):
    """
    Merge two lists of names, remove duplicates, and sort.

    Args:
        file1: path to first list file
        file2: path to second list file
        output_file: path to output file

    Returns:
        int: count of unique names
    """
    # TODO: Implement this function
    f = open(file1, "r")
    file1 = f.readlines()
    f.close()

    f = open(file2, "r")
    file2 = f.readlines()
    f.close()

    combine_names = set(file1 + file2)

    sorted_names = sorted(combine_names)

    f = open(output_file, "w")
    f.writelines(sorted_names)
    f.close()

    return len(sorted_names)


# Test your code here
result = merge_lists("labs/lab08/exercise2/data/list1.txt", "labs/lab08/exercise2/data/list2.txt", "labs/lab08/exercise2/data/merged.txt")
print(f"Unique names: {result}")
