import pandas as pd
import json


# Read a jsonl file into list-of-dictionaries
def read_jsonl(filename):
    pairs = []
    for line in open(filename, 'r', encoding='utf-8'):
            pairs.append(json.loads(line))
    if len(pairs) == 1:
        pairs = pairs[0]
    print("\n# Samples: ", len(pairs))
    print("# Keys: ", pairs[0].keys())
    return pairs


# Save list-of-dictionaries as a jsonl file
def write_as_jsonl(out_filename, listOfDicts):
    with open(out_filename, 'w', encoding='utf-8') as outfile:
        for each in listOfDicts:
            json.dump(each, outfile, ensure_ascii=False)
            outfile.write('\n')


# Show first N samples from list-of-dicts
def show_first_nSamples(dictList, N=5):
    for each in dictList[:N]:
        for k,v in each.items():
            print(k, ' : ', v)
        print()


## ----------------------------- I/O with GZ Files ----------------------


# Read json.gz file as list-of-dictionaries
def read_json_gz(filename):
    sampleList = []
    with gzip.open(filename, 'rt', encoding='utf-8') as fin:
        for idx, line in enumerate(fin):
            sampleList.append(json.loads(line))
    print("\nNumber of samples : ", len(sampleList))
    print("Keys: ", sampleList[0].keys())
    return sampleList


# Show N samples from jsonl.gz file json.gz file
def show_jsonl_gz_samples(filename, N=5):
    with gzip.open(filename, 'rt', encoding='utf-8') as fin:
        ck = 0
        for idx, line in enumerate(fin):
            pair = json.loads(line)

            for k,v in pair.items():
                print(k, ' : ', v)
            print()
            ck += 1
            if ck == N:
                break


""" ------------------------- PANDAS DataFrames <==> JSONL ----------------------------- """

# Write pandas dataframe to JSONL file
def writeDF_to_jsonl(df, outfile):
    df.to_json(outfile, orient = 'records', lines=True, force_ascii=False, compression = 'infer')


# Read JSONL file
def read_jsonl_to_dataframe(infile):
    df = pd.read_json(infile, lines=True, compression = 'infer')
    return df


""" ------------------------- PANDAS DataFrames <==> JSON ----------------------------- 

# Write pandas dataframe to JSON file
def writeDF_to_json(df, outfile):
    result = df.to_json(orient = 'index', force_ascii=False, compression = 'infer')
    parsed = json.loads(result)
    json.dump(parsed, outfile, ensure_ascii=False)


# Read JSON file
def read_json_to_dataframe(infile):
    df = pd.read_json(infile, orient='records', encoding='utf-8')
    return df
"""

''' ** Initialize dataframe with list-of-dicts **

sample_data = [{'Geeks': 'dataframe', 'For': 'using', 'geeks': 'list'},
        {'Geeks':10, 'For': 20, 'geeks': 30}] 
    
# Creates DataFrame. 
df = pd.DataFrame(sample_data)

# Convert dataframe to list-of-dicts
sample_data = df.to_dict('records')



# compute frequency/count of each class (eg. number-of-sentences, number-of-questions etc.)
# class-weight = percentage of each class (frequency-of-class-A / total-number-of-samples)
# save class-weights to dataframe:
    option 1:
        class-A : frequency_Column = weight-A
        class-B : frequency_Column = weight-B
        ..
        use df.sample(n,weights=frequency_Column, random_state=1)

    option 2:
        ** make sub-frames based on class labels ------------
        dfa = df[df['class']=='A']
        dfb = df[df['class']=='B']
        dfc = df[df['class']=='C']

        compute: na = n * class-weightA
                 nb = n * class-weightB
        and then
                 dfa.sample(na, random_state=1)
                 dfb.sample(nb, random_state=1)

------------------------ Sampling with frquency column of DataFrames -------------------------

# df = your data as pandas dataframe
# n = number to samples to select
# weights = a column with frequency/weights; higher weights = higher probabilty of selection
# random_state = 1 for reproducability

df.sample(n=2, weights='frequency', random_state=1)

'''
