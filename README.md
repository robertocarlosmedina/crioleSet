# CrioleSet dataset
### _CrioleSet is the first published Cape Verdean Creole dataset that includes phrases translated from Creole to other languages_

This dataset was made according to the need to have a dataset to complete my TM studies on Cape Verdean Creole. It is important to note that Cape Verde is divided into 10 islands and each island has its creole variant and in this dataset the data were collected according to the creole variants of the islands of São Vicente and Santo Antão.

> This project was made with the intention of being an integral part of my final final project.
> All aspects addressed in the implementation were made according to the needs of the project as a whole.
> Cape Verdean Creole is the mother language of Cape Verde, which is not an official language and is not well represented and known around the world. Therefore, it is a great honor to carry out studies and projects that contribute to its recognition and dissemination.

### Statistics

The dataset has more than 6000 pairs of translations from Cape Verdean Creole to Portuguese, English and French.
In the following table, you can see the token numbers for each language in the dataset:

| Language | Tokens Number |
| ----- | ----- |
| Cape Verdean Creole | 5154 |
| Portuguese | 5251 |
| English | 4135 |
| French | 4810 |

### Features / Execution

You can manipulate the amount of data to use for training, validate and test your model by running the main Python script on this dataset. And also you can choose to randomize the data or not.
for example you want to devide the datset like this:
```sh
python main.py -tr 95 -ts 2 -vl 3 -rd False
```
**Notes** that the parameters have the following meanings:
- **'-tr'** or **'--train'** is the percentage of the dataset to be used in training processes;
- **'-ts'** or **'--test'** is the percentage of the dataset to be used in testing processes;
- **'-vl'** or **'--val'** is the percentage of the dataset to be used in validation processes;
- **'-rd'** or **'--random'** to choose whether you want to randomize the dataset before splitting it or not;

In this code example we can see that we intend to use 95% of the dataset to train the model, 2% to test and 3% to validate it. And it is specified not to randomize the dataset before splitting it.

### All parts of the project into a whole
The whole project is divided into parts and each part has an essential function in it.
They are distributed as shown in the subtopics below.


#### Models implementation
This are the model used in the whole project:

- [Transformer model implementation]
- [GRU model implementation]
- [LSTM model implementation]
- [Models Training Graphs Generator]


#### Frontend test platform
This is a React App made to test all the translations made by the models, similar to the App [Google Translator]. 
Projects related to using the frontend application can be found at:

- [MT Models API implementation]
- [Cape Verdean Creole Translator Frontend test App]


#### Dataset
The dataset used to train, validate and test the model was the [CrioleSet dataset].
If the dataset is not in the project while executing any of the action commands, it will be downloaded and added to the project.

- [CrioleSet dataset]

### License

MIT


**Feel free to use and get in touch with any questions.**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [Transformer model implementation]: <https://github.com/robertocarlosmedina/attention-transformer-translator>
   [GRU model implementation]: <https://github.com/robertocarlosmedina/rnn-gru-attention-translator>
   [LSTM model implementation]: <https://github.com/robertocarlosmedina/rnn-lstm-translator>
   [MT Models API implementation]: <https://github.com/robertocarlosmedina/machine-translation-models-api>
   [CrioleSet dataset]: <https://github.com/robertocarlosmedina/crioleSet>
   [Cape Verdean Creole Translator Frontend test App]: <https://github.com/robertocarlosmedina/cv-creole-translator>
   [Models Training Graphs Generator]: <https://github.com/robertocarlosmedina/models-graphs-generator>
   [Google Translator]: <https://translate.google.com>