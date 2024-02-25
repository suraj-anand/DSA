def furthestBuilding(heights: list[int], bricks: int, ladders: int) -> int:
    n = len(heights)
    count = 0
    for i in range(n-1):
        if heights[i] >= heights[i+1]:
            count += 1
        
        else:
            if bricks <= 0 and ladders <= 0:
                break
            
            diff = heights[i+1] - heights[i]

            if diff <= bricks:
                bricks -= diff
                count += 1
            
            elif ladders != 0:
                ladders -= 1
                count += 1
            
            else:
                break
    
    return count


if __name__ == "__main__":
    h = [4,2,7,6,9,14,12]
    b, l = 5, 1

    # h = [4,12,2,7,3,18,20,3,19]
    # b, l = 10, 2
    r = furthestBuilding(h, b, l)
    print(r)

        