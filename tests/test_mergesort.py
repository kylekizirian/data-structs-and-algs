from honey.mergesort import mergesort_iterative, mergesort_recursive


def test_mergesort_iterative():
    assert mergesort_iterative([]) == []
    assert mergesort_iterative([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


def test_mergesort_recursive():
    assert mergesort_recursive([]) == []
    assert mergesort_recursive([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
