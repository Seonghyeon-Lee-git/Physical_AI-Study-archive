import numpy as np
import math
import collections

new_car = np.array([0.55, 0.45, 0.62, 0.48])

data = np.array([
    [0.3, 0.2, 0.4, 0.7],
    [0.4, 0.25, 0.3, 0.8],
    [0.35, 0.22, 0.35, 0.75],
    [0.8, 0.7, 0.6, 0.4],
    [0.85, 0.75, 0.5, 0.3],
    [0.82, 0.72, 0.55, 0.35],
    [0.7, 0.6, 0.8, 0.2],
    [0.75, 0.65, 0.85, 0.15],
    [0.8, 0.7, 0.9, 0.1],
    [0.5, 0.5, 0.6, 0.5],
    [0.45, 0.48, 0.65, 0.55],
    [0.52, 0.51, 0.58, 0.52]
])
data_name = np.array(['승용차', '승용차', '승용차',
                      '버스', '버스', '버스',
                      '트럭', '트럭', '트럭',
                      'SUV', 'SUV', 'SUV'])

def Euclidean_distance (data1, data2):
    distance = 0
    for i in range(len(data1)):
        data = (data1[i] - data2[i]) ** 2
        distance += data
    return math.sqrt(distance)

def min_distance_classify(new_data, data):
    distances = []
    for i in range(len(data)):
        dist = Euclidean_distance(new_data, data[i])
        distances.append(dist)
        print(f"{data_name[i]}와의 거리: {dist:.4f}")

    min_index = np.argmin(distances)
    name = data_name[min_index]
    return name

def major_vote_classify(new_data, data, k):
    distances = []
    for i in range(len(data)):
        dist = Euclidean_distance(new_data, data[i])
        distances.append(dist)
        print(f"{data_name[i]}와의 거리: {dist:.4f}")
    sorted_distances = np.argsort(distances)
    nearest_index = sorted_distances[:k]
    nearest_data_name = data_name[nearest_index]

    name = collections.Counter(nearest_data_name).most_common(1)
    return name[0][0]

#print(f"최종 분류 결과: {min_distance_classify(new_car, data)}")
print(f"최종 분류 결과: {major_vote_classify(new_car, data, 3)}")