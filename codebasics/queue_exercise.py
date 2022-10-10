import time
import threading
from queue import Queue

food_place_order_queue = Queue()


def place_order(orders):
    print("Placing order for: ", orders)
    food_place_order_queue.enqueue(orders)
    time.sleep(0.5)


def serve_orders():
    time.sleep(1)
    while True:
        order = food_place_order_queue.dequeue()
        print("Now serving ", order)
        time.sleep(2)

