import nltk

# nltk.download()
# from gingerit.gingerit import GingerIt

# text = 'The smelt of fliwers bring back memories.'

# parser = GingerIt()
# while True:
#     text = input("Enter: ")
#     print(parser.parse(text)["result"])

print (nltk.translate.meteor_score.meteor_score(
    ["this is an apple", 'this was an apple...', 'That will be an apple...'], "an apple on this tree"))
print (nltk.translate.meteor_score.meteor_score(
    ["this is an apple", "that is an apple"], "a red color fruit"))