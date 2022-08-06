from hypothesis import given
import hypothesis.strategies as some

@given(some.lists(some.integers()))
def test_list_size_is_invariant_across_sorting(a_list):
    original_len = len(a_list)
    a_list.sort()
    assert len(a_list) == original_len

