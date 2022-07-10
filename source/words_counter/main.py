from typing import List, Dict, Union


def words_frequency(words: List[str]) -> Union[Dict[str, int], List[str]]:
    """ Counts how often each word appears in the text and prints.

    Note:
        - words counter is case-sensitive.
        - return type List[str] denotes empty list
    """

    if isinstance(words, list) is False:
        raise ValueError

    if all(isinstance(word, str) for word in words) is False:
        raise ValueError

    if len(words) == 0:
        return []

    appearance_counter: Dict[str, int] = {}

    for word in words:
        if word not in appearance_counter.keys():
            appearance_counter[word] = 1
        else:
            appearance_counter[word] += 1

    return appearance_counter


if __name__ == '__main__':
    fake_input = ['word', 'word', 'left', 'up', 'John', 'Up', 'up']
    print(words_frequency(words=fake_input))
