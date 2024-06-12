#!/usr/bin/env python3
from typing import Sequence, Any, Union

def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Return the first element of the list if it exists, otherwise return None."""
    if lst:
        return lst[0]
    else:
        return None
