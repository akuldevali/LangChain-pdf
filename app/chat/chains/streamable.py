from queue import Queue
from threading import Thread
from app.chat.callbacks.stream import StreamingHandler



class StreamableChain:
    ##Overriding the stream function 
    def stream(self, input):

        queue= Queue()
        handler =  StreamingHandler(queue)

        # self(input)  This executes the chian but waits for all tokens to be assembled before executing next line, which defeats our purpuse of streaming from 
        #Can solve this by running it in a separate thread

        def task():
            self(input, callbacks=[handler]) #adding callbacks here from line31 so that

        Thread(target=task).start()

        while True:
            token = queue.get()
            if token is None:
                break
            yield token