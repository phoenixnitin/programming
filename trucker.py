def ks(n, weight, profit, W, unique_id):
    if W == 0 or n == 0:
        return [0, []]
    if weight[n-1] > W:
        return ks(n-1, weight, profit, W, unique_id)
    else:
        p1 = ks(n-1, weight, profit, W-weight[n-1], unique_id)
        p2 = ks(n-1, weight, profit, W, unique_id)
        if p1[0] + profit[n-1] > p2[0]:
            return [p1[0] + profit[n-1], p1[1] + [unique_id[n-1]]]
        else:
            return p2

# Complete the findTruckCargo function below.
def findTruckCargo(maxCargoWeight, cargoList):
    unique_id = []
    weights = []
    profit = []
    for item in cargoList:
        unique_id.append(item[0])
        weights.append(item[1])
        profit.append(item[2])
    total_p = ks(len(cargoList), weights, profit, maxCargoWeight, unique_id)
    return total_p[1] + [total_p[0]]
