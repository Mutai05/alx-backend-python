Variable annotations in Python allow you to add type hints to your variables, providing clarity and enabling type checking tools to verify your code's correctness. These annotations do not enforce type checking at runtime but serve as useful documentation and enable static analysis tools to catch potential type errors.

### Basic Syntax of Variable Annotations
In Python, you can annotate variables with their expected types using the following syntax:
```python
variable_name: type = value
```

### Examples of Variable Annotations
Here are some examples illustrating how to use variable annotations in Python:

#### Basic Annotations
```python
# Annotating basic types
name: str = "John Doe"
age: int = 30
height: float = 5.9
is_student: bool = True

# Annotating a list
scores: list[int] = [95, 85, 76]

# Annotating a dictionary
student_info: dict[str, int] = {"John": 90, "Alice": 85}
```

#### Function Annotations
You can also annotate function parameters and return types to indicate the expected types:
```python
def greet(name: str) -> str:
    return f"Hello, {name}!"

def add(a: int, b: int) -> int:
    return a + b

def get_student_score(student: str) -> int:
    return student_info.get(student, 0)
```

#### Annotations with Optional Types
Sometimes a variable can be of multiple types, or it might be optional. You can use the `Optional` type from the `typing` module for such cases:
```python
from typing import Optional

age: Optional[int] = None  # age can be an int or None
```

#### Using Union for Multiple Types
If a variable can be of more than one type, use `Union` from the `typing` module:
```python
from typing import Union

result: Union[int, float] = 10  # result can be an int or a float
```

#### Annotating Complex Data Structures
For more complex data structures, you can use generic types from the `typing` module:
```python
from typing import List, Dict, Tuple

coordinates: List[Tuple[float, float]] = [(10.0, 20.0), (15.5, 25.5)]
employee_records: Dict[str, Tuple[int, str]] = {
    "Alice": (1001, "Engineer"),
    "Bob": (1002, "Manager")
}
```

### Example: Annotating a Class
Annotations are also useful in class definitions to indicate the types of attributes and methods:
```python
from typing import List

class Student:
    def __init__(self, name: str, grades: List[int]):
        self.name: str = name
        self.grades: List[int] = grades

    def average_grade(self) -> float:
        return sum(self.grades) / len(self.grades)
```

### Tools for Type Checking
There are several tools available to perform static type checking in Python:
- **mypy**: A static type checker that can check your Python code for type consistency.
- **pytype**: Another type checker developed by Google.
- **Pyright**: A fast type checker used in Visual Studio Code.

### Using mypy for Type Checking
To use mypy, you can install it using pip:
```sh
pip install mypy
```
Then run mypy on your Python file:
```sh
mypy your_script.py
```

### Summary
Variable annotations in Python provide a way to specify the expected types of variables, function parameters, and return values. While they don't enforce type checking at runtime, they help improve code readability and enable static analysis tools to catch type errors, leading to more robust code.
