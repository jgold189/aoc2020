import timeit

def mapListManip(items):
    return list(map(lambda x: int(x.strip()), items))

def standardListManip(items):
    return [int(x.strip()) for x in items]

if __name__ == "__main__":
    items = ["1", "2", "3", "4", "5", "99\n", "100\n", "355\n", "5603 \n", "43250 \n"]
    print(mapListManip(items))
    print(standardListManip(items))
    setup = "items = [\"1\", \"2\", \"3\", \"4\", \"5\", \"99\\n\", \"100\\n\", \"355\\n\", \"5603 \\n\", \"43250 \\n\"]"
    mapCode = "list(map(lambda x: int(x.strip()), items))"
    standardCode = "[int(x.strip()) for x in items]"
    print("Map:", timeit.timeit(setup = setup, stmt = mapCode, number=10000000))
    print("Standard", timeit.timeit(setup = setup, stmt = standardCode, number=10000000))