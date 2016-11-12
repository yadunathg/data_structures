# python2

class Request:
    def __init__(self, arrival_time, process_time):
        self.arrival_time = arrival_time
        self.process_time = process_time

# class Response:
#     def __init__(self, dropped, start_time):
#         self.dropped = dropped
#         self.start_time = start_time

class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time_ = []

    def Process(self, request):
        # write your code here
        while self.finish_time_ and request.arrival_time >= self.finish_time_[-1]:
            self.finish_time_.pop()
        if not self.finish_time_:
            self.finish_time_.insert(0, request.arrival_time + request.process_time)
            return request.arrival_time

        elif len(self.finish_time_) == self.size:
                return -1
        else:
            start_time = max(self.finish_time_[0], request.arrival_time)
            self.finish_time_.insert(0, start_time + request.process_time)
            return start_time



def ReadRequests(count):
    requests = []
    for i in range(count):
        arrival_time, process_time = map(int, raw_input().strip().split())
        requests.append(Request(arrival_time, process_time))
    return requests

def ProcessRequests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.Process(request))
    return responses

def PrintResponses(responses):
    for response in responses:
        print response

if __name__ == "__main__":
    size, count = map(int, raw_input().strip().split())
    requests = ReadRequests(count)

    buffer = Buffer(size)
    responses = ProcessRequests(requests, buffer)

    PrintResponses(responses)
