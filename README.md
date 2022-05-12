# Telugu Utilities
This repository aims to provide a basic and efficient utility module for Telugu language.

## 1. Telugu Tokenizer
This module modifies an exisiting tokenizer for better efficiency, by adding hand-crafted rules.

#### Test Tokenizer

To test the telugu tokenizer, use the code file test_tokenizer.py with the following commands.

	
```
	$ python3 test_tokenizer.py test_samples/example_2.txt <file-name>
```
OR
	
```
	$ python3 test_tokenizer.py <telugu-text> 'text'
```
#### Usage

To make use of this repository, git-clone it inside your project repository.
After that you can simply import desired methods. 

For example:
```
	>>> from TeluguUtilities.TeluguTokenizer import tokenizer as t
```
## 2. Indic Transliterator

```
	>>> from TeluguUtilities.utils import transliterator
	>>> demo(lang='te_IN')
```
