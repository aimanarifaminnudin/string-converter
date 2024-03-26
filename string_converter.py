import os

class StringTransformer:
    def to_uppercase(self, text):
        """Converts text to uppercase."""
        return text.upper()

    def to_alternate_case(self, text):
        """Converts text to alternate case."""
        return ''.join([char.upper() if i % 2 == 0 else char.lower() for i, char in enumerate(text)])

class CSVWriter:
    def write_to_csv(self, text, filepath):
        """Writes characters of the text to a CSV file."""
        with open(filepath, 'w') as file:
            file.write(','.join(text))

class Application:
    def __init__(self, transformer, writer):
        self.transformer = transformer
        self.writer = writer

    def run(self):
        """Prompts user for input, processes it, and writes to a CSV file."""
        input_text = input("Enter a string: ")
        uppercase_text = self.transformer.to_uppercase(input_text)
        alternate_case_text = self.transformer.to_alternate_case(input_text)

        print(f"UPPERCASE: {uppercase_text}")
        print(f"Alternate Case: {alternate_case_text}")

        filename = "string_characters.csv"
        self.writer.write_to_csv(input_text, filename)
        print(f"CSV file created at: {os.path.abspath(filename)}")

if __name__ == "__main__":
    transformer = StringTransformer()
    writer = CSVWriter()
    app = Application(transformer, writer)
    app.run()