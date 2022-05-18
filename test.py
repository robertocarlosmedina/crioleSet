from gingerit.gingerit import GingerIt

text = 'The smelt of fliwers bring back memories.'

parser = GingerIt()
while True:
    text = input("Enter: ")
    print(parser.parse(text)["result"])