import heapq


def merge_k_lists(lists):
    min_heap = []

    for i in range(len(lists)):
        if lists[i]:
            heapq.heappush(min_heap, (lists[i][0], i, 0))

    result = []

    while min_heap:
        value, list_idx, element_idx = heapq.heappop(min_heap)
        result.append(value)

        if element_idx + 1 < len(lists[list_idx]):
            heapq.heappush(min_heap, (lists[list_idx][element_idx + 1], list_idx, element_idx + 1))

    return result


lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)
