from hashtabel import HashTable


def left_join(left, right):
    joined_data = []
    for bucket in left._buckets:
        if bucket:
            current = bucket.head
            while current:
                left_column = [current.value[0], current.value[1]]
                right_value = right.get(current.value[0])
                left_column.append(right_value)
                current = current.next
            joined_data.append(left_column)
    return joined_data


if __name__ == '__main__':

    hashmap1 = HashTable()
    hashmap2 = HashTable()

    hashmap1.add('fond', 'enamored')
    hashmap1.add('wrath', 'anger')
    hashmap1.add('diligent', 'employed')
    hashmap1.add('outfit', 'garb')
    hashmap1.add('guide', 'usher')

    hashmap2.add('fond', 'averse')
    hashmap2.add('wrath', 'delight')
    hashmap2.add('diligent', 'idle')
    hashmap2.add('guide', 'follow')
    hashmap2.add('flow', 'jam')

    print(left_join(hashmap1, hashmap2))


