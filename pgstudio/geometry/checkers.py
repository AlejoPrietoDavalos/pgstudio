__all__ = []
import numpy as np

# Type chequer.

def is_arr(arr: np.ndarray) -> bool: return isinstance(arr, np.ndarray)
def assert_arr(arr: np.ndarray) -> None: assert is_arr(arr)



