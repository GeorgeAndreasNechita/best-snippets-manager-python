import os


class Snippet:
    def __init__(self, title, content):
        self.title = title
        self.content = content


# Create an array of Person objects
snippets = []

# Specify the path to the snippets folder


def read_snippets_folder():
    snippets_folder = "./snippets"

    # Check if the snippets folder exists
    if os.path.exists(snippets_folder):
        # Iterate over the files in the snippets folder
        for filename in os.listdir(snippets_folder):
            # Check if the file has a .txt extension
            if filename.endswith(".txt"):
                # Construct the full file path
                file_path = os.path.join(snippets_folder, filename)

                # Read the contents of the file
                with open(file_path, "r") as file:
                    content = file.read()
                    snippets.append(Snippet(filename, content))
        return snippets

    else:
        print(f"The snippets folder '{snippets_folder}' does not exist.")


# read_snippets_folder()
print(read_snippets_folder())
