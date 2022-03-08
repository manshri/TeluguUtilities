from TeluguTokenizer.tokenizer import *
import sys
import codecs


### Testing the tokenizer with command line arguments.
no_tokens = 0
if(len(sys.argv)==3):

    file_fp = sys.argv[1] ### File pointer or text
    f_type = sys.argv[2] ### mode of input (file/text)
    
    data = ""
    if(f_type=="file"):
        ### Reading the text from file pointer.
        try:
            with codecs.open(file_fp,"r",encoding="utf-8") as fp:
                data = fp.read()
        except Exception as e:
            with codecs.open(file_fp,"r",encoding="utf-16") as fp:
                data = fp.read()
    else:
        ### Assigning the text to variable
        data = file_fp
    
    processed_data = preprocess_data(data)        ### Preprocessing data
    sentences = sentence_tokenize(processed_data) ### Sentencification
    tokens = word_tokenize(sentences)   ### Tokenization
    clened_tokens = remove_punctuation(tokens)   ### Remove punctuations from tokens

    ### Printing sentences and tokens
    print("Original Text: \n", data)
    print("\nPreprocessed Text: \n", processed_data)
    print("\nList of sentences:")
    for sent in sentences:
        print(sent)
    print("\nList of tokens: \n", tokens)
    print("\nList of Processed tokens: \n", clened_tokens)

else:
    print("Hint:")
    print(">>>python3 tokenize.py <file_pointer> 'file'")
    print("Or")
    print(">>> python3 tokenize.py <string> 'text'")