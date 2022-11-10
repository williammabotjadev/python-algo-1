# Find Dice Probabilities 

from collections import defaultdict, Counter 

def find_dice_probs(S, n_faces=6):
    if S > 2 * n_faces or S < 2:
        return None 
    
    cdict = Counter()
    ddict = defaultdict(list)

    for dice_one in range(1, n_faces + 1):
        for dice_two in range(1, n_faces + 1):
            t = [dice_one, dice_two]
            cdict[dice_one + dice_two] += 1 
            ddict[dice_one + dice_two].append(t)
    return [cdict[S], ddict[S]]

def tests(module_name="This Module"):
        n_faces = 6
        S = 5
        results = find_dice_probs(S, n_faces)
        print(results)
        assert(results[0] == len(results[1]))

if __name__ == "__main__":
    tests()
