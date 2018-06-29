# Given an infinite number of quarters(25 cents), dimes(10 cents),
# nickles(5 cents) and pennies (1 cent), write code to calculate
# the number of ways of representing n cents

def make_change(target, denoms, index=None, map=None):
    if denoms is None or index is None or map is None:
        dimes = sorted(denoms, reverse=True)
        print dimes
        map = [[0 for i in range(len(dimes))] for j in range(target+1)]
        return make_change(target, denoms=dimes, index=0, map=map)

    if map[target][index] > 0:
        return map[target][index]

    if index >= len(denoms) - 1:
        return 1

    denomAmount = denoms[index]
    ways = 0
    i = 0
    while(i * denomAmount <= target):
        amountRemaining = target - i * denomAmount
        ways += make_change(amountRemaining,denoms, index + 1, map)
        i+=1

    map[target][index] = ways
    return ways


if __name__ == '__main__':
    print make_change(10, [2,5,3,6])
