from random import randint
from typing import List, Optional

def list_generator(list_length: int) -> List[int]:
    """
    Generates a list of integers from 0 to list_length - 1.

    Args:
    list_length (int): The length of the list to be generated.

    Returns:
    List[int]: A list of integers.
    """
    if list_length < 0:
        raise ValueError("List length cannot be negative.")
    return [i for i in range(list_length)]


def two_sum(collection: List[int], target: int) -> Optional[List[int]]:
    """
    Finds two indices in the collection whose elements add up to the target value.

    Args:
    collection (List[int]): A list of integers.
    target (int): The target sum to find.

    Returns:
    Optional[List[int]]: A list of two indices if a solution is found, otherwise None.
    """
    coll_dict = {}
    for idx, itm in enumerate(collection):
        complement = target - itm
        if complement in coll_dict:
            return [coll_dict[complement], idx]
        coll_dict[itm] = idx
    return None


if __name__ == '__main__':
    # Generate a collection with a random length (0 to 9999).
    list_length = randint(0, 9999)
    collection = list_generator(list_length)
    
    # Define a random target value.
    target = randint(0, 9999)
    
    # Output the target for debugging purposes.
    print(f"Target is: {target}")

    # Find and print the solution.
    solution = two_sum(collection=collection, target=target)
    
    # If no solution is found, handle it gracefully.
    if solution:
        print(f"Indices of elements that sum to {target}: {solution}")
    else:
        print(f"No solution found for target {target} in the collection.")
