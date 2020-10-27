article = "Facebook has developed an artificial intelligence capable of accurately translating between " \
          "any pair of 100 languages " \
          "without relying on first translating to English, as many existing systems do. " \
          "The AI outperforms such systems by 10 points on a 100-point scale used by academics to " \
          "automatically evaluate the quality of machine translations. Translations produced by the model were also " \
          "assessed by humans, who scored it as around 90 percent accurate. Facebook’s system was trained on a data " \
          "set of 7.5 billion sentence pairs gathered from the web across 100 languages, " \
          "though not all the languages had an equal number of sentence pairs. What I really was interested in " \
          "was cutting out English as a middle man. Globally there are plenty of regions where they speak two " \
          "languages that aren’t English,” says Angela Fan of Facebook AI, who led the work. The model was trained " \
          "by focusing on languages that are commonly translated to and from each other, grouping languages into 14 " \
          "separate collections based on geography and cultural similarities. This was done to ensure high quality " \
          "translation of more commonly used connections, and to train the model more accurately."


def convert(string):
    string = string.replace(',', '')
    string = string.replace('.', '')
    li = list(string.split(" "))
    return li


article_list = convert(article)

lambda_1 = lambda x: x.index("Angela")
print(f'Returning the index of the specified name in the article: {lambda_1(article_list)}')

lambda_2 = lambda x: x.append("Article was taken from Journal of Machine Learning Research")
lambda_2(article_list)
print(f'Printing the last element of the list that was added: {article_list[-1]}')

lambda_3 = lambda x: x.count("AI")
print(f'Number of word AI in text: {lambda_3(article_list)}')


map_1 = list(map(lambda x: len(x), article_list))
print(f'Returning the len of each word: {map_1}')

map_2 = list(map(lambda x: x.upper(), article_list))
print(f'Making each word with upper case: {map_2}')

map_3 = list(map(lambda x: x if x != "Facebook" else "Amazon", article_list))
print(f'Replacing "Facebook: to "Amazon" in the article: {map_3}')



filter_1 = list(filter(lambda x: len(x) > 8, article_list))
print(f'Returning the words that have more than 8 letters: {filter_1}')

filter_2 = list(filter(lambda x: x.isnumeric(), article_list))
print(f'Returning all numbers from the article: {filter_2}')

filter_3 = list(filter(lambda x: x[0] in "aeiou", article_list))
print(f'Returns each word that starts from vowel: {filter_3}')