from nlpretext import Preprocessor
import sys
import os
from tqdm import tqdm
from nlpretext.basic.preprocess import (normalize_whitespace, remove_punct, remove_eol_characters,
remove_stopwords, lower_text, filter_non_latin_characters)
from nlpretext.social.preprocess import remove_mentions, remove_hashtag, remove_emoji
# text = "I just got the best dinner in my life @latourdargent !!! I  recommend 😀 #food #paris \n"
preprocessor = Preprocessor()
preprocessor.pipe(lower_text)
# preprocessor.pipe(remove_mentions)
# preprocessor.pipe(remove_hashtag)
preprocessor.pipe(remove_emoji)
# preprocessor.pipe(remove_eol_characters)
# preprocessor.pipe(remove_stopwords, args={'lang': 'en'})
preprocessor.pipe(remove_punct)
# preprocessor.pipe(filter_non_latin_characters)
preprocessor.pipe(normalize_whitespace)


def clean_file(file, ignore):
    cleaned = []
    with open(file, "r") as f:
        raw = f.readlines()
        N = len(raw)

    for i in tqdm(range(N)):
        if i in ignore:
            continue

        cleaned_i = preprocessor.run(raw[i])
        cleaned_i = ''.join([i for i in cleaned_i if not i.isdigit()])
        
        if len(cleaned_i) == 0 or cleaned_i == "\n":
            ignore.add(i)
            continue
        cleaned.append(cleaned_i + "\n")

    return cleaned, ignore

def write_file(name, data):
    with open(name + "_cleaned.txt", "w") as f:
        f.writelines(data)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        os.exit(1)

    file1 = sys.argv[1]
    file2 = sys.argv[2]

    ignore = set()
    clean1, ignore = clean_file(file1, ignore)
    clean2, ignore = clean_file(file2, ignore)

    write_file(file1, clean1)
    write_file(file2, clean2)


