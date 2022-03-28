class PriorityQueue:
    """Priority queue implemented by heap"""
    
    def __init__(self):
        ## heap implemented by list
        self.heap = [None]
        return
    
    def _swap(self, index1, index2):
        """Swap data at index1 and index2"""
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]
        return
    
    def _reverse_heapify(self, index):
        """Check heap property of data from input index to root"""
        while index > 1:
            parent_index = index // 2
            if self.heap[parent_index] < self.heap[index]:
                self._swap(parent_index, index)
                index = parent_index
            else:
                break
        return
    
    def insert(self, data):
        """Insert new data at self.heap"""
        self.heap.append(data)
        self._reverse_heapify(len(self.heap)-1)
        return
    
    def _heapify(self, index):
        """Check heap property of data from input index to last index"""
        if 0 < index < len(self.heap):
            largest = index
            left_child_index = index * 2
            if 0 < left_child_index < len(self.heap) and\
                self.heap[left_child_index] > self.heap[largest]:
                largest = left_child_index
            right_child_index = index * 2 + 1
            if 0 < right_child_index < len(self.heap) and\
                self.heap[right_child_index] > self.heap[largest]:
                largest = right_child_index
            self._swap(index, largest)
            self._heapify(largest)
        return
    
    def __str__(self):
        return str(self.heap)


if __name__ == '__main__':
    # test code
    priority_queue = PriorityQueue()

    priority_queue.insert(6)
    priority_queue.insert(9)
    priority_queue.insert(1)
    priority_queue.insert(3)
    priority_queue.insert(10)
    priority_queue.insert(11)
    priority_queue.insert(13)

    print(priority_queue)