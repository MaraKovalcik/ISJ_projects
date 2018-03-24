#!/usr/bin/env python3

# @Author: Marek Kovalčík (xkoval14)

import collections

# vrátí vstupní položku item, pokud tato může být prvkem množiny v Pythonu, v opačném případě frozenset(item)
def can_be_a_set_member_or_frozenset(item):
    '''checking whether the item can be a member of a set'''
    if(isinstance(item, collections.Hashable)):
        return item
    return frozenset(item)

# na vstupu dostane seznam a pouze s použitím vestavěných funkcí (tedy bez použití "import") z něj vytvoří
# seznam, odpovídající množině všech podmnožin
def all_subsets(lst):
    '''finding all subsets in list'''
    result = [[]]
    for item in lst:
        result.extend([subset + [item] for subset in result])
    return result

# obdoba předchozího, ale při volání dostane prvky seznamu přímo jako argumenty a navíc má volitelný parametr exclude_empty, který,
# když není ve volání uveden, nebo je jeho hodnota True, vrátí výsledek bez prázdného seznamu.
# Pokud je hodnota tohoto argumentu False, je výsledek stejný jako u předchozí funkce.
def all_subsets_excl_empty(*args, exclude_empty=True):
    '''finding all subsets in list including/excluding empty member (depends on exclude_empty parameter)'''
    arguments = list(args)
    result = [[]]
    for item in arguments:
        result.extend([subset + [item] for subset in result])
    if(exclude_empty):
        result = [item for item in result if item != []]

    return result


def test():
    assert can_be_a_set_member_or_frozenset(1) == 1
    assert can_be_a_set_member_or_frozenset((1, 2)) == (1, 2)
    assert can_be_a_set_member_or_frozenset([1, 2]) == frozenset([1, 2])
    assert all_subsets(['a', 'b', 'c']) == [[], ['a'], ['b'], ['a', 'b'], ['c'], ['a', 'c'], ['b', 'c'], ['a', 'b', 'c']]
    assert all_subsets_excl_empty('a', 'b', 'c') == [['a'], ['b'], ['a', 'b'], ['c'], ['a', 'c'], ['b', 'c'], ['a', 'b', 'c']]
    assert all_subsets_excl_empty('a', 'b', 'c', exclude_empty=True) == [['a'], ['b'], ['a', 'b'], ['c'], ['a', 'c'], ['b', 'c'], ['a', 'b', 'c']]
    assert all_subsets_excl_empty('a', 'b', 'c', exclude_empty=False) == [[], ['a'], ['b'], ['a', 'b'], ['c'], ['a', 'c'], ['b', 'c'], ['a', 'b', 'c']]


if __name__ == '__main__':
    test()
