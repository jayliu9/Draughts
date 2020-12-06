from binary import binary_search

def test_binary_exists():
    assert(binary_search([1], 1))
    assert(binary_search([1, 2], 1))
    assert(binary_search([1, 2], 2))
    assert(binary_search(['a'], 'a'))
    lst = ['a', 'a', 'b', 'c', 'd', 'e', 'f', 'f', 'g', 'h', 'i']
    assert(binary_search(lst, 'a'))
    assert(binary_search(lst, 'b'))
    assert(binary_search(lst, 'c'))
    assert(binary_search(lst, 'd'))
    assert(binary_search(lst, 'e'))
    assert(binary_search(lst, 'f'))
    assert(binary_search(lst, 'g'))
    assert(binary_search(lst, 'h'))
    assert(binary_search(lst, 'i'))

def test_binary_no_exist():
    assert(binary_search([1], -1) is False)
    assert(binary_search([1, 2], 3) is False)
    assert(binary_search([1, 2], -1) is False)
    assert(binary_search(['a'], 'b') is False)
    lst = ['a', 'a', 'b', 'c', 'd', 'e', 'f', 'f', 'g', 'h', 'i']
    assert(binary_search(lst, 'j') is False)
    assert(binary_search(lst, '') is False)
    assert(binary_search(lst, 'klm') is False)
    assert(binary_search(lst, 'n') is False)
    assert(binary_search([], 1) is False)