import heapq
from typing import Generic, TypeVar
from collections.abc import Callable, Hashable

T = TypeVar("T", int, float)
H = TypeVar("H", bound=Hashable)
class AStar(Generic[T, H]):
    """Provides a generic A* algorithm implementation.

    Args:
        Generic_T (int | float): The cost and heuristic return type.
        Generic_H (Hashable): The type of the node.
        neighbour_func (Callable[[H], list[H]]): A function that returns the neighbours of a node.
        cost_func (Callable[[H, H], T]): A function that returns the cost between two nodes.
        heuristic_func (Callable[[H], T]): A function that returns the heuristic cost of a node.
    
    ## Description:
        ### How does A* work?
            1. Initialize a Priority Queue, setting the start node with a cost of 0.
            2. Initialize a Dictionary of Previous Nodes, setting the start node to None.
            3. Initialize a Dictionary of Costs, setting the start node to 0.
            4. Iterate until the queue is empty:
                1. Pop the node with the lowest cost from the queue. (Using heapq.heappop())
                2. If the popped node is the end node, break the loop.
                3. Iterate through the neighbours of the popped node:
                    1. new_cost = cost of popped node + cost from popped node to neighbour
                    2. If the neighbour has not been visited or new_cost < previous_cost:
                        1. Update the cost of the neighbour.
                        3. Push neighbour into queue with priority = new_cost + heuristic(neighbour).
                        4. Update the previous node of the neighbour to the popped node.
                        
            Estimated Time Complexity: `O(E + V log V)`, E = number of edges, V = number of vertices.
            Estimated Space Complexity: `O(V)`, V = number of vertices.
        ### How does getting the cost work?
            1. Return the cost of the end node from the costs dictionary.
            
            Estimated Time Complexity: `O(1)`.
            Estimated Space Complexity: `O(1)`.
        ### How does getting the path work?
            1. Initialize an empty list for the path.
            2. Set the current node to the end node.
            3. While the current node is not None:
                1. Append the current node to the path.
                2. Set the current node to the previous node of the current node. (using the previous dictionary)
            4. Return the path in reverse order.
            
            Estimated Time Complexity: `O(V)`, V = number of vertices.
            Estimated Space Complexity: `O(V)`, V = number of vertices.
        
    """
    def __init__(self,
                 neighbour_func: Callable[[H], list[H]],
                 cost_func: Callable[[H, H], T],
                 heuristic_func: Callable[[H], T]):
        self.cost_func = cost_func
        self.neighbour_func = neighbour_func
        self.heuristic_func = heuristic_func
        self.previous: dict[H, H] = {}
        self.costs: dict[H, T] = {}

    def find_path(self, start: H, end: H):
        queue: list[tuple[T, H]] = []
        queue.append([0,start])
        self.previous = {}
        self.previous[start] = None
        self.costs = {}
        self.costs[start] = 0

        while queue:
            _, current = heapq.heappop(queue)
            if current == end:
                break
            for neighbour in self.neighbour_func(current):
                new_cost = self.costs[current] + self.cost_func(current, neighbour)
                if neighbour not in self.costs or new_cost < self.costs[neighbour]:
                    self.costs[neighbour] = new_cost
                    priority = new_cost + self.heuristic_func(neighbour)
                    heapq.heappush(queue, [priority, neighbour])
                    self.previous[neighbour] = current
    def get_cost(self, end: H) -> T:
        return self.costs[end]
    def get_path(self, end: H) -> list[H]:
        path = []
        current = end
        while current:
            path.append(current)
            current = self.previous[current]
        return path[::-1]
