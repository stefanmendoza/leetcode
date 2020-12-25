class Solution:
    def frequencySort(self, s: str) -> str:
        mapping = {}
        for c in s:
            if c in mapping:
                mapping[c] += 1
            else:
                mapping[c] = 1

        tuples = []
        for key in mapping:
            tuples.append(Pair(key, mapping[key]))

        h = Heap(tuples)
        return h.get_sorted()


class Pair:
    def __init__(self, c, v):
        self.character = c
        self.frequency = v


class Heap:

    def __init__(self, f):
        self.tree = f

        last_parent_index = (len(self.tree) - 1) // 2

        for i in range(last_parent_index, -1, -1):
            self.shift_down(i)

    def swap(self, idx1, idx2):
        value1 = self.tree[idx1]
        self.tree[idx1] = self.tree[idx2]
        self.tree[idx2] = value1

    def shift_down(self, current_idx):
        left_idx = 2 * current_idx + 1
        right_idx = 2 * current_idx + 2

        largest_idx = current_idx
        if left < len(self.f) and self.tree[left].frequency >= self.tree[largest_idx].frequency:
            largest_idx = left_idx

        if right < len(self.f) and self.tree[right].frequency >= self.tree[largest_idx].frequency:
            largest_idx = right_idx

        if largest_idx != current_idx:
            swap(current_idx, largest_idx)
            self.shift_down(largest)

    def pop(self):
        frequency = self.tree[0]

        self.tree[0] = self.tree[-1]
        del self.tree[-1]

        self.shift_down(0)

        return frequency

    def get_sorted(self):
        s = ''
        while self.f != []:
            t = self.pop()
            s += t.character * t.frequency
