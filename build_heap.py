# python3


def build_heap(data):
    swaps = []
    n = len(data)
    for i in range(n//2-1, -1, -1):
        j = i
        while True:
            left = 2*j + 1
            right = 2*j + 2
            sm = j
            if left < n and data[left] < data[sm]:
                sm = left
            if right < n and data[right] < data[sm]:
                sm = right
            if sm != j:
                data[j], data[sm] = data[sm], data[j]
                swaps.append((j,sm))
                j = sm
            else: 
                break
    return swaps


def main():
    
    mode = input("Type I or F: ").strip()
    if mode == "I":
        n = int(input())
        data = list(map(int, input().split()))
    else:
        file_name = input().strip()
        try: 
            with open('./tests/' + file_name, 'r') as file:
                n = int(file.readline())
                data = list(map(int, input().split()))
        except Exception as ex:
            print("File not found", str(ex))
            return

    assert len(data) == n
    swaps = build_heap(data)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
