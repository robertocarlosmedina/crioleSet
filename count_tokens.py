import spacy

spacy_models = {
    "en": spacy.load("en_core_web_sm"),
    "pt": spacy.load("pt_core_news_sm"),
    "cv": spacy.load("pt_core_news_sm"),
    "fr": spacy.load("fr_core_news_sm")
}

def tokenize_en(sentence: str, languague: str):
    """
        Tokenizes Cap-Verdian text from a string into a list of strings
    """
    return [tok.text for tok in spacy_models[languague].tokenizer(sentence)]

def counte_languague_tokens(languague: str):
    tokens_list = []

    files = [f"train.{languague}", f"test.{languague}", f"val.{languague}"]

    for file in files:
        file_reader = open(file, "r")
        for line in file_reader.readlines():
            tokens = tokenize_en(line, languague)
            for token in tokens:
                if token not in tokens_list:
                    tokens_list.append(token)
    
    # print(tokens_list)
    return len(tokens_list)

print("\n\nNumber of tokens that the crioleSet languagues have:\n")
print("  * Criole cabo-verdiano: ", counte_languague_tokens("cv"))
print("  * Português: ", counte_languague_tokens("pt"))
print("  * Inglês: ", counte_languague_tokens("en"))
print("  * Francês: ", counte_languague_tokens("fr"))
