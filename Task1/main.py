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


if __name__ == "__main__":
    main()