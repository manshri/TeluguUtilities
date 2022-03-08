# Telugu Tokenizer
### _Modified indic tokenizer for telugu language_

The main aim of this tokenizer is to improve the sentence and word tokenization by incorporating the hand-crafted rules. This tokenizer build on the basis of [indic word tokenizer](https://indic-nlp-library.readthedocs.io/en/latest/_modules/indicnlp/tokenize/indic_tokenize.html)

### Hand-Crafted Rules

- Two or more dots cannot be considered as the end of sentence
- Question Marks will not be treated as the end of sentence
- Newline/carriage return will be treated as the end of sentence.
- All the sentence enclosed with in the brances are considered as single sentence.
- If the paragraph miss the end quote (single or double quote), sentencification will be done based on the sentence end punctuation (dot).

### Methods

#### *trivial_tokenize_indic()*

This method insert leading and trailing space for all the punctuations. Also, handle the numbers and dates as single tokens. Apart from these, we have added the code to join all the consequent similar puctuations will null to represent the combination as single token. This modification helps to improve the performance of the sentence tokenizer.

#### *preprocess_data()*

This preprocessing methods includes the following techniques:
- Replace all tab spaces with single space
- Replace the 0-width space with null character
- Seperate more than one dot(.) and '"' with single ' ' (example: ..." --> ... ")
- Seperate more than one dot(.) and "'" with single ' ' (example: ...' --> ... ')
- Seperate more than one dot(.) and '-' with ' ' (example: '...-' --> '... -')
- Multiple new lines replaced with single new line.
- Multiple carriage returns replaced with single '\r'.
- Multiple white spaces replaced with single space.
- Finally leading/trailing spaces are trimmed.

#### *sentence_tokenize()*

Sentence tokenizer takes the text as input and return the list of sentences. This sentence_tokenize methods initially apply the modified indic word tokenizer and use the above mentioned hand-crafted rules to split the given text into list of sentences

#### *word_tokenize()*

Word tokenizer takes the list of sentences as input and return the list of list of tokens as output. This word_tokenize method apply the modified indic word tokenizer to get the list of tokens as the output for each sentence.

#### *remove_punctuation()*

This method takes the list of tokens as input and return the list of cleaned tokens (punctuations will be replaced with null) as output.
