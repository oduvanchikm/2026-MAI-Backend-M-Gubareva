class LRUCache:
    def __init__(self, capacity: int = 10) -> None:
        self.capacity = capacity
        self.cache = {}

    def get(self, key: str) -> str:
        if key not in self.cache:
            return ''

        value = self.cache.pop(key)
        self.cache[key] = value
        return value

    def set(self, key: str, value: str) -> None:
        if key in self.cache:
            self.cache.pop(key)
        elif len(self.cache) >= self.capacity:
            oldest_key = next(iter(self.cache))
            self.cache.pop(oldest_key)

        self.cache[key] = value

    def rem(self, key: str) -> None:
        if key in self.cache:
            self.cache.pop(key)