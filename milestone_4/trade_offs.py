def find_sum(target: int, li: list[int]) -> tuple[int, int]:
    for i in range (len(li)):
        for j in range (i+1, len(li)):
            if li[i] + li[j] == target:
                return (li[i],li[j])
# assert find_sum(5, [1, 2, 3, 4, 5]) in {(0, 3), (1, 2)}
# the AssertionError will arise as neither of the pairs in the set will be equal to the target
# but if we change the assertion comparison to different pairs in the set.....
assert find_sum(5, [1,2,3,4,5]) in {(1,4),(2,3)}
# no AssertionError will arise as to the returned values fitting into the pairs presented in the set

# Time complexity: 0(n^2) - nested loop
# Space complexity: 0(1) - nothing extra has been utilised

def find_sum_fast(target: int, li: list[int]) -> tuple[int, int]:
   iterated = set()
   for num in li:
       z = target - num
       if z in iterated:
           return z, num
       else:
           iterated.add(num)
assert find_sum(5, [1, 2, 3, 4, 5]) in {(0, 3), (1, 2)}
# assert find_sum(5, [1,2,3,4,5]) in {(1,4),(2,3)}
