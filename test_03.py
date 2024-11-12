class TimeMap:

    def __init__(self):
        self.string_dict = dict()
        self.int_dict = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.string_dict[(key, timestamp)] = value

    def get(self, key: str, timestamp: int) -> str:

        def find_max_value_less_than_me(l: list[int], test_val: int) -> int:
            l.sort()
            first = 0
            last = len(l) - 1

            while first < last:
                mid = first + (last - first) // 2
                if l[mid] <= test_val:
                    if l[mid + 1] <= test_val:
                        first = mid + 1
                    else:
                        return l[first]

                if l[mid] > test_val:
                    last = mid

            return l[first]

        val = 0
        while val == 0:
            val = self.string_dict.get((key, timestamp), 0)
            if val != 0:
                return self.string_dict[key, timestamp]
            if val == 0:
                love = [val[1] for val in self.string_dict.keys(
                ) if val[0] == key]
                max_value = find_max_value_less_than_me(love, timestamp)
                if max_value > timestamp:
                    return ""
                return self.string_dict[key, max_value]

            if timestamp < 1:
                return ""

        return ""

        # Your TimeMap object will be instantiated and called as such:
        # obj = TimeMap()
        # obj.set(key,value,timestamp)
        # param_2 = obj.get(key,timestamp)


def main() -> None:
    # value = 0
    # print('value: ', value)
    # print('type(value): ', type(value))
    obj = TimeMap()
    obj.set("foo", "bar", 10)
    # print(obj.string_dict)
    print(obj.get("foo", 10))
    print(obj.get("foo", 15))
    print(obj.get("foo", 3))

    obj.set("foo", "bar2", 4)
    print(obj.get("foo", 4))
    print(obj.get("foo", 5))


if __name__ == '__main__':
    main()

# TimeMap timeMap = new TimeMap();
# timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
# timeMap.get("foo", 1);         // return "bar"
# timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
# timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
# timeMap.get("foo", 4);         // return "bar2"
# timeMap.get("foo", 5);         // return "bar2"
