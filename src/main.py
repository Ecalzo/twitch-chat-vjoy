from queue import Queue
from threading import Thread
from consumer import main_consumer
from producer import main_producer

if __name__ == "__main__":
    queue = Queue()
    producer = Thread(target=main_producer, args=(queue,))
    consumer = Thread(target=main_consumer, args=(queue,))
    producer.start()
    consumer.start()
