class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # coMap = {}  # Store the coordinates and distances
        # distances = []  # Store only distances to use heapq
        # finalPoints = []  # Store final k closest points

        # # Calculate distances for each point and store them
        # for point in points:
        #     x1, y1 = point
        #     dist = math.sqrt(x1 ** 2 + y1 ** 2)
        #     distances.append(dist)
        #     coMap[str(point)] = dist

        # heapq.heapify(distances)  # Heapify the distances for efficient popping
        # count = 0

        # # Retrieve k closest points
        # while count < k:
        #     count += 1
        #     val = heapq.heappop(distances)  # Get the smallest distance
        #     # Find the point associated with this distance
        #     for point_str, dist in list(coMap.items()):  # Iterating over a copy of coMap
        #         if dist == val:
        #             finalPoints.append(eval(point_str))  # Convert string back to list
        #             del coMap[point_str]  # Remove the point from the map to avoid duplicates

        # return finalPoints

        # #2nd Approach
        # heap = []  # Heap to store the k closest points

        # # Calculate the squared distances and store them in the heap
        # for point in points:
        #     dist = point[0] ** 2 + point[1] ** 2
        #     heapq.heappush(heap, (dist, point))

        # # Retrieve the k closest points from the heap
        # closest_points = []
        # for _ in range(k):
        #     closest_points.append(heapq.heappop(heap)[1])

        # return closest_points

        #3rd Approach

        minHeap = []

        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            minHeap.append([dist, x, y])
        
        heapq.heapify(minHeap)
        res = []

        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x,y])
            k -= 1
        
        return res
