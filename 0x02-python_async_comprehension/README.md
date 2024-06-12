Async comprehensions in Python allow you to asynchronously iterate over an iterable and collect the results in a non-blocking manner. They are similar to regular comprehensions but are used with asynchronous iterators and coroutines.

Here's a brief overview of async comprehensions:

### Syntax:
```python
async for item in async_iterable:
    # Body of the loop
```

### Features:
1. **Async Iterables**:
   - Async comprehensions are used to iterate over async iterables, such as asynchronous generators or asynchronous iterators.

2. **Non-Blocking**:
   - Async comprehensions allow you to iterate over multiple asynchronous operations concurrently without blocking the event loop.

3. **Coroutine-based**:
   - The body of the async comprehension can contain awaitable expressions, such as coroutine function calls, allowing you to perform asynchronous operations within the comprehension.

### Example:
Suppose you have an asynchronous generator that yields random numbers asynchronously. You can use an async comprehension to collect a list of random numbers asynchronously:

```python
import asyncio
import random

async def generate_random_numbers(n):
    for _ in range(n):
        await asyncio.sleep(1)  # Simulate asynchronous operation
        yield random.randint(1, 100)

async def main():
    async_numbers = [num async for num in generate_random_numbers(5)]
    print(async_numbers)

asyncio.run(main())
```

In this example:
- We define an asynchronous generator `generate_random_numbers` that yields random numbers asynchronously using `asyncio.sleep`.
- We use an async comprehension to iterate over the asynchronous generator and collect the random numbers asynchronously into a list.
- We print the list of random numbers.

Async comprehensions are useful for collecting the results of multiple asynchronous operations or iterating over asynchronous data sources in a non-blocking manner. They are commonly used in asynchronous programming with asyncio to handle concurrent operations efficiently.
