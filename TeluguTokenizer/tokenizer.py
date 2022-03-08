#!/usr/bin/env python3
# coding=utf-8

import sys
import codecs
import re
import string


### Indic pattern for numbers and punctuations.
triv_tokenizer_indic_pat=re.compile(r'(['+string.punctuation+r'\u0964\u0965'+r'])')
pat_num_seq=re.compile(r'([0-9]+ [,.:/] )+[0-9]+')


### Punctuations list
puncts = list(string.punctuation)

### Telugu acronyms
acronyms = ["రు","కి","మీ","మి","సెం","రా","సా","తె","మ","గం","ని","జూ","నం","నెం","రూ","డాక్టర్","ఎ","ఏ","బి","సి","డి","ఇ","ఎఫ్","జి","హెచ్","ఐ","జె","జే","కె","కే","ఎల్","ఎం","ఎమ్","ఎన్","ఒ","ఓ","పి","ఫి","క్యు","క్యూ","ఆర్","ఎస్","టి","తి","యు","ఉ","ఊ","వి","డబ్లు","డబ్లూ","ఎక్స్","ఏక్స్","వై","జెడ్","జేడ్","శ్రీమతి","శ్రి","డాక్టర్","ప్రొఫెసర్","డా","ఛి","చి","చిరంజీవి","సౌ","ల"]
EndPunctuation = re.compile(r"("+("|".join(acronyms))+")+\s*")


def trivial_tokenize_indic(text):
    """tokenize string for Indian language scripts using Brahmi-derived scripts

    A trivial tokenizer which just tokenizes on the punctuation boundaries. 
    This also includes punctuations for the Indian language scripts (the 
    purna virama and the deergha virama). This is a language independent 
    tokenizer

    Args:
        text (str): text to tokenize

    Returns:
        list: list of tokens

    """
    tok_str = triv_tokenizer_indic_pat.sub(r' \1 ',text.replace('\t',' '))

    s = re.sub(r'[ ]+',' ',tok_str).strip(' ')
   
    # do not tokenize numbers and dates
    new_s = ''
    prev = 0
    for m in pat_num_seq.finditer(s):
        start = m.start()
        end = m.end()
        if start>prev:
            new_s = new_s + s[prev:start]
            new_s = new_s + s[start:end].replace(' ','')
            prev = end
   
    new_s = new_s + s[prev:]
    s = new_s

    '''
    The following code is to handle the case of more than two dots. 
    Usually, in such a case, each dot is considered as a sentence break. 
    Based on the hypothesis that consecutive dots do not all mark the end of sentence individually.
    This method avoids breaking the sentence at each dot, by adding a rule: "if previous word is a dot and current word is a dot then sentence split should not happen."
    Also, combined the consecuitive similar puntuations as single token
    '''
    tokens = re.split(r'[ ]',s)

    word_flag = True
    tokens_list = []
    token = ""
    for i in range(0, len(tokens)-1):
        if tokens[i]==tokens[i+1] and tokens[i] in puncts:
            token += tokens[i]
            word_flag = False
        else:
            word_flag = True
            token += tokens[i]

        if word_flag:
            tokens_list.append(token)
            token = ""

    token += tokens[-1]
    tokens_list.append(token)

    return tokens_list


def preprocess_data(data):
    """Preprocess the given text and return the processed text

    This preprocessing methods includes the following techniques:
    1) Replace all tab spaces with single space
    2) Replace the 0-width space with null character
    3) Seperate more than one dot(.) and '"' with single ' ' (example: ..." --> ... ")
    4) Seperate more than one dot(.) and "'" with single ' ' (example: ...' --> ... ')
    5) Seperate more than one dot(.) and '-' with ' ' (example: '...-' --> '... -')
    6) Multiple new lines replaced with single new line.
    7) Multiple carriage returns replaced with single '\r'
    8) Multiple white spaces replaced with single space
    9) Finally leading/trailing spaces are trimmed.

    Args:
        data (str): text to apply preprocessing techniques

    Returns:
        str: processed text

    """

    data = re.sub(r"[\t]+"," ", data) ## Tested
    data = re.sub(r'[\u200b\u200c\u200d]', r'', data) ## Tested
    data = re.sub(r'(\.+)("+)',r' \1 \2 ',data) ## Tested
    data = re.sub(r"(\.+)('+)",r" \1 \2 ",data) ## Tested
    data = re.sub(r'(\.+)(-+)',r' \1 \2 ',data) ## Tested

    
    try:
        temp = re.split("\n",data)
        for i in range(len(temp)):
            temp[i] = temp[i].strip()
            if(len(temp[i])>0):
                temp[i] += " "

    except Exception as e:
        print(e)
            
    data = "".join(temp)

    data = re.sub(r"[\n]+","\n",data)
    data = re.sub(r"[\r]+","\r",data)
    data = re.sub(r"[ ]+"," ",data)
    data = data.strip()
    return data



def sentence_tokenize(data):
    """Sentence tokenizer takes the text as input and return the list of sentences. This sentence_tokenize methods initially apply the modified indic word tokenizer and use the hand-crafted rules to split the given text into list of sentences

    Args:
        data (str): text to apply sentencification

    Returns:
        list: list of sentences

    """
    words = trivial_tokenize_indic(data) ### List of tokens seperated by space
    sentences = []
    
    ### Sentence begin, end and sentence break flag.
    begin = 0
    end = 1
    break_sen = False
    
    ### Next word, previous word and previous word index.
    prev = 0
    next_word = ""
    prev_word = ""

    i = 1
    while(i<len(words)):

        ### Finiding out the previous word index
        if words[i-1]!="." and words[i-1]!=" " and words[i-1]!=",":
            prev = i-1
        else:
            prev = i-2

        ### Previous word and Present word from list of tokens.
        curr_word = words[i]
        if(prev>=0):
            prev_word = words[prev]

        '''
        This code snippet handle the single and double quotes. If the ending quotes is missing
        then the sentencification will be done in normal way. Otherwise, it will consider the 
        content within the quotes as single sentence.
        '''
        ### Checking for the quotes
        if words[i-1]=='"':
            temp_index = i
            while(temp_index<len(words)):
                if(words[temp_index]=='"'):
                    end = temp_index + 1
                    i = end
                    prev_word = words[i-1]
                    curr_word = words[i]
                    break
                temp_index += 1

        if prev_word=="'":
            temp_index = i
            while(temp_index<len(words)):
                if(words[temp_index]=="'"):
                    end = temp_index + 1
                    i = end
                    prev_word = words[i-1]
                    curr_word = words[i]
                    break
                temp_index += 1
        '''
        Quotation code ends here.
        '''


        ### Checking if the current word is a sentence break then previous word should not be an acronym.
        if((curr_word=='.' or curr_word=="\n" or curr_word=="\r") and i>0):
            temp = EndPunctuation.search(prev_word)
            match_word = ""
            if temp is not None:
                match_word = prev_word[temp.span()[0]:temp.span()[1]]
            if prev_word not in acronyms and match_word!=prev_word:
                end = i+1
                break_sen = True

        ### Breaking the sentence if the sentence break flag is set to TRUE.
        if break_sen:
            sent = " ".join(words[begin:end])
            sent = sent.replace("\n","")
            sent = sent.replace("\r","")
            sent = sent.strip()

            sentences.append(sent)
            begin = end
            break_sen = False


        ### index increment
        i += 1

    ### Remaining words (last sentence) considered as the last sentence.
    sent = " ".join(words[begin:])
    if(len(sent)>=1 and (sent!="\n" and sent!="\t" and sent!=" ")):
        sentences.append(sent)

    return sentences



def word_tokenize(sent_list):
    """Word tokenizer takes the list of sentences as input and return the list of list of tokens as output

    This word_tokenize method initially apply the indic word tokenizer.

    Args:
        sent_list (list): list of sentences (output of sentence_tokenize)

    Returns:
        list: list of tokens

    """

    ### Tokens, token break, previous word index, next word
    tokens = []
    break_wrd = True
    prev = 0
    next_word = ""
    
    for i in range(len(sent_list)):

        ### Extracting each sentence in a sentence list
        sent = sent_list[i]

        ### Applied the modified indic tokenizer for the sentence
        words = trivial_tokenize_indic(sent)

        ### Adding all tokens to the token list
        tokens.extend(words)
    return tokens


### Function to remove punctuations from the token list
def remove_punctuation(tokens):
    """This method takes the list of tokens as input and return the list of cleaned tokens (punctuations will be replaced with null) as output.

    Args:
        tokens (list): list of tokens (output of word_tokenize)

    Returns:
        list: list of cleaned tokens

    """

    cleaned_tokens = []
    pattern = re.compile(r"["+"".join(puncts)+"]+")
    for i in range(len(tokens)):
        token = tokens[i]

        ### Replacing the punctuations in the word with null 
        token = pattern.sub(r'',token)

        token = token.strip()
        if token!="":
            cleaned_tokens.append(token)

    return cleaned_tokens