# python2

class JobQueue:
    def read_data(self):
        self.num_workers, m = map(int, raw_input().split())
        self.jobs = list(map(int, raw_input().split()))
        assert m == len(self.jobs)

    def write_response(self):
        for i in range(len(self.jobs)):
            print self.assigned_workers[i], self.start_times[i]

    def assign_jobs(self):
        # TODO: replace this code with a faster algorithm.
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)
        self.worker_queue = [{'index': i, 'next_free_time': 0} for i in range(self.num_workers)]
        for i in range(len(self.jobs)):
            worker, free_time = self.get_min()
            self.assigned_workers[i], self.start_times[i] = worker, free_time
            self.change_priority(free_time + self.jobs[i])

            #   next_worker = 0
            #   for j in range(self.num_workers):
            #     if next_free_time[j] < next_free_time[next_worker]:
            #       next_worker = j
            #   self.assigned_workers[i] = next_worker
            #   self.start_times[i] = next_free_time[next_worker]
            #   next_free_time[next_worker] += self.jobs[i]

    def get_min(self):
        print self.worker_queue
        return self.worker_queue[0]['index'], self.worker_queue[0]['next_free_time']

    def change_priority(self, free_time):
        self.worker_queue[0]['next_free_time'] = free_time
        self.sift_down(0)

    def sift_down(self, i):
        left_child = 2 * i + 1
        right_child = 2 * i + 2
        min_index = i
        if (left_child < self.num_workers) and (
            (self.worker_queue[left_child]['next_free_time'] < self.worker_queue[min_index]['next_free_time']) or (
                self.worker_queue[left_child]['next_free_time'] == self.worker_queue[min_index]['next_free_time'] and
                self.worker_queue[left_child]['index'] < self.worker_queue[min_index]['index'])):
            min_index = left_child
        if (right_child < self.num_workers) and (
            (self.worker_queue[right_child]['next_free_time'] < self.worker_queue[min_index]['next_free_time']) or (
                self.worker_queue[right_child]['next_free_time'] == self.worker_queue[min_index]['next_free_time'] and
                self.worker_queue[right_child]['index'] < self.worker_queue[min_index]['index'])):
            min_index = right_child
        if min_index != i:
            self.worker_queue[min_index], self.worker_queue[i] = self.worker_queue[i], self.worker_queue[min_index]
            self.sift_down(min_index)

    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()


if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()
