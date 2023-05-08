# In this example, we first import the LegalTokenizer class from a module called legal_tokenizer. We then define a main function that creates an instance of the LegalTokenizer class and enters a loop that prompts the user to enter text to tokenize. If the user enters 'q', the loop breaks and the program exits. Otherwise, the text is tokenized using the tokenize method of the LegalTokenizer class, and the tokenized output is printed to the console.

from legal_tokenizer import LegalTokenizer

def main():
    tokenizer = LegalTokenizer()
    while True:
        text = input("Enter text to tokenize (or type 'q' to quit): ")
        if text == 'q':
            break
        tokens = tokenizer.tokenize(text)
        print("Tokenized output:")
        for token in tokens:
            print(token)
        print()

if __name__ == '__main__':
    main()

#To run this program, we can save the code to a file called legal_tokenizer_cli.py and run it from the command line:
 
$ python legal_tokenizer_cli.py
Enter text to tokenize (or type 'q' to quit): This Agreement shall be amended to read as follows:
Tokenized output:
('Agreement', 'LEGAL_TERM')
('shall be amended', 'LEGAL_PHRASE')
('to read as follows', 'LEGAL_PHRASE')

Enter text to tokenize (or type 'q' to quit): Section 1.2(a)
Tokenized output:
('Section 1.2(a)', 'SECTION_HEADING')

Enter text to tokenize (or type 'q' to quit): q
