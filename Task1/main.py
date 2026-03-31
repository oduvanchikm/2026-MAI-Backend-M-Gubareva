from Task1.cache import LRUCache


def main():
    cache = LRUCache(100)
    cache.set('Jesse', 'Pinkman')
    cache.set('Walter', 'White')
    cache.set('Jesse', 'James')

    print(cache.get('Jesse'))

    cache.rem('Walter')
    print(cache.get('Walter'))

    print(cache.get('Jesse'))

    small_cache = LRUCache(2)
    small_cache.set('key1', 'value1')
    small_cache.set('key2', 'value2')
    small_cache.set('key3', 'value3')
    print(small_cache.get('key1'))
    print(small_cache.get('key2'))


if __name__ == "__main__":
    main()