from tqdm import tqdm

def most_frequent(List):
    counter = 0
    num = List[0]

    for i in List:
        curr_frequency = List.count(i)
        if (curr_frequency > counter):
            counter = curr_frequency
            num = i

    return num, counter


def is_dominant(n):
    s = str(n)
    return most_frequent(s)[1] > len(s) // 2

def D(n: int) -> int:
    out: int = -1
    for i in tqdm(range(10**n)):
        if is_dominant(i):
            out += 1 

    return out

print(D(7))

# 9
# 18
# 270
# 603
# 8307
# 19737
# 265257
