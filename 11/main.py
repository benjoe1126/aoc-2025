from typing import List, Tuple, Dict


def dfs_util(vertices,node, finished):
    for neighbour in vertices[node]:
        if neighbour not in finished:
            dfs_util(vertices,neighbour, finished)
    finished.append(node)

def dfs(vertices,v):
    finished = []
    dfs_util(vertices, v,finished)
    return list(dict.fromkeys(finished))

def adjacency_matrix_from_file(fname: str, start: str = "you") -> Tuple[List[str],List[List[int]]]:
    nodes = []
    adj_list = {}
    with open(fname) as f:
        for line in f:
            separated = line.split(":")
            node = separated[0]
            neighbors = separated[1].strip().split(" ")
            nodes.append(node)
            adj_list[node] = neighbors
    nodes.append("out")
    adj_list["out"] = []
    can_order = list(reversed(dfs(adj_list,start)))
    return can_order,[[0 if can_order[i] not in adj_list[can_order[j]] else 1 for i in range(len(can_order))] for j in range(len(can_order))]

def num_paths_to(nodes, adj_matrix,offset: int = 0) -> int:
    helper_list = [0 for _ in nodes]
    helper_list[0] = 1
    for i in range(1, len(nodes)):
        for j in range(i):
            helper_list[i] += helper_list[j] * adj_matrix[j + offset][i + offset]
    return helper_list[-1]

def part_one() -> int:
    nodes, adj_matrix = adjacency_matrix_from_file("input.txt")
    return num_paths_to(nodes, adj_matrix)

def part_two() -> int:
    nodes, adj_matrix = adjacency_matrix_from_file("input.txt","svr")
    fft_idx, dac_idx = nodes.index("fft"), nodes.index("dac")
    first_endpoint_idx, second_endpoint_idx = min(dac_idx, fft_idx),max(fft_idx, dac_idx)
    svr_to_first = nodes[0:first_endpoint_idx + 1]
    first_to_second = nodes[first_endpoint_idx:second_endpoint_idx + 1]
    second_to_out = nodes[second_endpoint_idx:]
    first_offset = len(svr_to_first) - 1
    second_offset = first_offset + len(first_to_second) - 1
    return num_paths_to(svr_to_first, adj_matrix) * num_paths_to(first_to_second, adj_matrix, offset=first_offset) * num_paths_to(second_to_out, adj_matrix, offset=second_offset)

def main() -> None:
    print(part_one())
    print(part_two())

if __name__ == "__main__":
    main()