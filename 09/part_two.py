import shapely
from typing import List

def dist(p1: shapely.Point,p2: shapely.Point):
    return (abs(p1.x - p2.x) + 1) * (1 + abs(p1.y - p2.y))

elements: List[shapely.Point] = []
line_to_point = lambda line: shapely.Point(int(line.strip().split(",")[0]),int(line.strip().split(",")[1]))
with open("input.txt") as f:
    elements = list(map(line_to_point,f.readlines()))
poly = shapely.geometry.Polygon([[p.x, p.y] for p in elements])
max_dist = 0
for i in range(len(elements) // 2 + 1):
    for j in range(i + 1,len(elements) // 2 + 1):
        p = elements[i]
        q = elements[j]
        [minx,miny,maxx,maxy] = [min(p.x,q.x),min(p.y,q.y),max(p.x,q.x),max(p.y,q.y)]
        rect = shapely.geometry.box(minx,miny,maxx,maxy)
        if max_dist > dist(p,q): continue
        if rect.boundary.within(poly):
            max_dist = dist(p,q)

print(int(max_dist))