import pandas as pd


'''
'''

# filter dataframe by value of given column with operand 'op'
def filter_frameCol(df, col, op, val):
  new_df = df.query(col + op + str(val))
  print("# Pairs with %s %s %d : "%(col, op, val), new_df.shape[0])
  print("# Invalid pairs: ", df.shape[0] - new_df.shape[0])
  return new_df

def rangeFilter_frameCol(df, cols, ops, vals):
  new_df = df.query(cols[0] + ops[0] + str(vals[0]) and cols[1] + ops[1] + str(vals[1]))
  print("# Pairs with %s %s %d and %s %s %d : "%(cols[0], ops[0], vals[0], cols[1], ops[1], vals[1]), new_df.shape[0])
  print("# Invalid pairs: ", df.shape[0] - new_df.shape[0])
  return new_df

"""# **Intrinsic Metrics Functions**"""

# ## Compute the set of Extractive Fragments F(A, S) (the set of shared sequences of tokens in A and S)

def F(A,S, ng=0):
  F = []
  i = j = 0
  i_hat = 0
  while i<len(S):
    f = []
    while j<len(A):
      if S[i]==A[j]:
        i_hat = i
        j_hat = j
        while i_hat<len(S) and j_hat<len(A) and S[i_hat] == A[j_hat]:
          i_hat = i_hat + 1
          j_hat = j_hat + 1
        if (i_hat-i) > ng and len(f)<(i_hat - i):
          f = [S[n] for n in range(i, i_hat)]
        j = j_hat
      else:
        j = j + 1
    i = i + max(len(f),1)
    j = 0
    F.append(f)
  return set(tuple(e) for e in F)


# Compute compression & abstractivity scores for each pair
def add_Metrics(pairs, drop_index=False):

  final_pairs = []
  count = 0

  for each in pairs:

    article_sents = sentence_tokenize.sentence_split(each['text'], lang='te')
    
    summary_tokens = indic_tokenize.trivial_tokenize(each['summary'])
    article_tokens = indic_tokenize.trivial_tokenize(each['text'])
    title_tokens = indic_tokenize.trivial_tokenize(each.get('title', ''))


    article_len = len(article_tokens)
    summary_len = len(summary_tokens)
    title_len = len(title_tokens)

    total_stokens = len(summary_tokens)
    
    # Compression
    compression = round((100 - (len(summary_tokens)/len(article_tokens))*100), 2)

    # Abstractivity-0,1,2,3
    abstractivity = []
    for ng in range(4):
      matched_fragments = F(article_tokens, summary_tokens, ng=ng)
      
      sumF_abs = 0
      for f in matched_fragments:
        sumF_abs += len(f)
      abstractivity.append(round((100 - (sumF_abs/total_stokens)*100), 2))
    
    new_pair = dict(each)
    new_pair.update({'article_sentence_count': len(article_sents), 'article_token_count': article_len, 'summary_token_count': summary_len, 'title_token_count': title_len, 'compression': compression, 'abstractivity': abstractivity[0], 'abstractivity-1': abstractivity[1], 'abstractivity-2': abstractivity[2], 'abstractivity-3': abstractivity[3]})
    final_pairs.append(new_pair)
    
  return final_pairs

# # Count pairs with articles_tokens<40 or summary_tokens<10
# # Count pairs with compression % < 50
# filter both these out and save remaining

# def getMinLengthNdCompression(pairs):
#   if pairs == []:
#     print("Get some data!")
#     return
#   invalid_length_count = 0
#   low_compression_count = 0

#   valid_count = 0
#   valid_pairs = []
#   for each in pairs:

#     if each['article_len'] < 40 or each['summary_len'] < 10:
#       invalid_length_count += 1
#     else:
#       if each['compression'] < 50 :
#         low_compression_count += 1
#       else:
#         valid_count += 1
#         valid_pairs.append(each)

#   print("Length too short: ", invalid_length_count)
#   print("Compression% below 50: ", low_compression_count)
#   print("Valid pairs left: ", valid_count)
#   return valid_pairs

# # # Count pairs with compression % >= 90
# # filter both these out and save remaining
# def getMaxCompression(pairs, limit):

#   high_compression_count = 0
#   valid_count = 0
#   valid_pairs = []
#   invalid_pairs = []
#   for each in pairs:

#     if each['compression'] > limit:
#       high_compression_count += 1
#       invalid_pairs.append(each)
#     else:
#       valid_count += 1
#       valid_pairs.append(each)

#   print("Compression% > ",limit, ' : ', high_compression_count)
#   print("Valid pairs left: ", valid_count)
#   return valid_pairs, invalid_pairs

# # # Count pairs with articles_sents<4
# # filter it out and save remaining
# def getValidSentLength(pairs):
#   invalid_length_count = 0
#   valid_count = 0
#   valid_pairs = []
#   for i in range(len(pairs)):
#     article_content = pairs[i]['text']
#     article_sents = sentence_tokenize.sentence_split(article_content, lang='te')

#     if (len(article_sents) < 4):
#       invalid_length_count += 1
#     else:
#       valid_count += 1
#       valid_pairs.append(pairs[i])

#   print("Article sent Length too short: ", invalid_length_count)
#   print("Valid pairs left: ", valid_count)
#   return valid_pairs


"""## **All at once**"""

# New # Filter on abstractivity ranges 

# def absFilters(pairs):

#   valid_range_pairs = []
#   abs0_10 = 0
#   abs1_10 = 0
#   abs0_80 = 0
#   for each_pair in pairs:

#     if each_pair['Abs-0'] >= 10:
#       if each_pair['Abs-1'] >= 10:
#         if each_pair['Abs-0'] <= 80:
#           valid_range_pairs.append(each_pair)
#         else:
#           abs0_80 += 1
#       else:
#         abs1_10 += 1
#     else:
#       abs0_10 += 1

#   print("Valid pairs: ", len(valid_range_pairs))
#   print("Pairs removed by Abs0 > 10: ", abs0_10)
#   print("Pairs removed by Abs1 > 10: ", abs1_10)
#   print("Pairs removed by Abs0 <= 80: ", abs0_80)
#   print("Pairs removed total: ", (len(pairs)-len(valid_range_pairs)))
#   return valid_range_pairs

