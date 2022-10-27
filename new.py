import math
import re
from collections import Counter
from typing import Iterable


def preprocess_text(text: str) -> list[str]:
    text = re.split(r"[-;,.“\s]\s*", text.lower())
    filtered_text = list(filter(None, text))
    return filtered_text


def calc_tf(term: str, text: str) -> float:
    term = term.lower()
    text = preprocess_text(text)

    number_most_frequent = (Counter(text).most_common()[0])[1]  # counting how many times the most common term appears in our text

    count_of_our_term = 0           # counting how many times our term appears in our text
    for word in text:
        if word == term:
            count_of_our_term += 1

    word_count = len(text)

    frequency1 = count_of_our_term / word_count
    frequency2 = number_most_frequent / word_count

    result = 1/2 + (1/2 * frequency1 / frequency2)

    return result

# print(calc_tf('котиков', "Не ешьте котиков. Не ешьте мышь. Не ешьте сыр.")) output: 0.6666666666666666


def calc_idfs(corpus: Iterable[str]) -> dict:
    updated_text = []      # creating a list of docs with terms
    for string in corpus:
        updated_text.append(preprocess_text(string))

    number_of_docs = len(updated_text)   # calculating the number of documents

    words = []   # creating one list with all the terms
    for list in updated_text:
        for elem in list:
            if elem not in words:
                words.append(elem)

    dict_of_words = {}       # creating a dictionary (term)(number of docs with it)
    for word in words:
        count = 0           # the number of docs with this term
        for list in updated_text:
            if word in list:
                count += 1
        dict_of_words[word] = count

    for elem in dict_of_words:   # changing the values in dict to idfs
        dict_of_words[elem] = math.log((number_of_docs/(1 + dict_of_words[elem])), 2.7182818284)

    return dict_of_words


text_corpus = [
"Как выжить в современной России.",
"Никогда не берите в руки нож.",
"Не покупайте водку.",
"Просыпайся в 7 утра.",
"Никогда не ешьте котов",
"Не ешьте то, что не можете позволить себе купить.",
"Уберитесь в квартире.",
"В любой непонятной ситуации - ешь мясо!",
"Не ешьте мясо, если хотите жить долго и счастливо.",
"Не попадаться на глаза сотрудникам полиции. Выйти из дома с сумкой, на которой написано “Я не верблюд",
"Не ешьте камни. Не ешьте ничего, кроме собаки.",
"Не ешьте собаку.",
"Не ешьте мышей. Не ешьте кошек.",
"Не ешьте котиков. Не ешьте мышь. Не ешьте сыр.",
"Не ешьте никого. Не ешьте кота.",
"Покупать себе только то, что выгодно, например, покупать дешевый алкоголь в магазине, который находится в подвале.",
"Не иметь друзей.",
"Не говорить с незнакомцами. Не разговаривать с незнакомыми людьми.",
"Перестать бояться незнакомых людей, перестать бояться незнакомцев.",
"Не общаться с незнакомыми девушками. Не общаться со знакомыми девушками.",
"Не говорить девушкам, что они нравятся тебе. Не говорить, что нравишься им."
"Не говорить им, что любишь их. Не встречаться с ними. Не влюбляться в них. Не рассказывать им о своих чувствах.", 'В современных российских условиях вопрос выживания становится все более актуальным. И не столько для тех, кто живет "на земле", сколько для интеллигенции, представителей творческих профессий и, конечно, для студентов. В этой связи особенно важно, чтобы каждый из нас смог определить для себя жизненные ценности, которые помогут ему сохранить себя, свою человеческую сущность и остаться человеком в экстремальных условиях.',
'Как выжить в современной России. У нас есть три способа: 1) стать жертвой маньяка; 2) стать жертвой другого маньяка, которого мы убьем; 3) стать жертвой не маньяка.', 'Покупать все продукты в магазине "Магнит" и ходить в церковь.',
'Никогда не ложитесь спать, будучи голодными;',
'Кушать бублики с маком. Бубликов с маком много.',
'Не ходить в церковь; Не верить в бога; Не пить водку; Не работать.']


idfs = calc_idfs(text_corpus)


def calc_tfidf(term: str, text: str, precomputed_idfs: dict) -> float:
    result = calc_tf(term, text) * precomputed_idfs[term]
    return result


#print(calc_tfidf('котиков', "Не ешьте котиков. Не ешьте мышь. Не ешьте сыр.", idfs))  output: 1.7351264570006122
