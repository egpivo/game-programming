import tkinter as tk
from typing import List


class GameObject:
    """
    Example
    -------
    >>> import tkinter as tk
    >>> root = tk.Tk()
    >>> frame = tk.Frame(root)
    >>> canvas = tk.Canvas(frame, width=600, height=400, bg="#4285F4")
    >>> item = canvas.create_rectangle(10, 10, 10, 10, fill="blue")
    >>> game_object = GameObject(canvas, item)
    >>> print(game_object.get_position())
    [10.0, 10.0, 10.0, 10.0]
    >>> game_object.move(20, -10)
    >>> print(game_object.get_position())
    [30.0, 0.0, 30.0, 0.0]    
    >>> game_object.delete()
    >>> print(game_object.get_position())
    []    
    """

    def __init__(self, canvas: tk.Canvas, item: int) -> None:
        self.canvas = canvas
        self.item = item

    def get_position(self) -> List[float]:
        return self.canvas.coords(self.item)

    def move(self, x: int, y: int) -> None:
        self.canvas.move(self.item, x, y)

    def delete(self) -> None:
        self.canvas.delete(self.item)
