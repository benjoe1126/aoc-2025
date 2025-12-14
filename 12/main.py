from typing import Tuple, Dict, List


def from_file(fname: str) -> Tuple[Dict[int, int], List[Tuple[str, List[int]]]]:
    with open(fname) as f:
        tiles = {}
        dimensions = []
        idx = -1 # if you just delete the first line of the input could be 0
        for line in f:
            if "x" in line:
                separated = line.split(":")
                dimensions.append((separated[0].strip(), list(map(int, separated[1].strip().split(" ")))))
            elif ":" in line:
                idx += 1
            elif line.strip():
                tiles[idx] = tiles.get(idx, 0) + line.count("#")
    return tiles, dimensions


# turns out you can do this braindead shit and for the input it yields the correct result XD
def main() -> None:
    shapes_size, dimensions = from_file("input.txt")
    count = 0
    for (grid_size, indexes) in dimensions:
        h, w = list(map(int, grid_size.split("x")))
        grid_size_int = h * w
        size = sum([num * shapes_size[idx] for idx, num in enumerate(indexes)])
        if size <= grid_size_int:
            count += 1
    print(count)


if __name__ == "__main__":
    main()
