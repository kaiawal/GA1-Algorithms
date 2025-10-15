'''
    This file contains the template for Assignment1.  You should fill the
    function <majority_party_size>.  The function, recieves two inputs:
      (1) n: the number of delegates in the room, and
      (2) same_party(int, int): a function that can be used to check if two members are
      in the same party.

    Your algorithm in the end should return the size of the largest party, assuming
    it is larger than n/2.

    I will use <python3> to run this code.
'''


def majority_party_size(n, same_party):
    '''
        n (int): number of people in the room.
        same_party (func(int, int)): This function determines if two delegates
            belong to the same party.  same_party(i,j) is True if i, j belong to
            the same party (in particular, if i = j), False, otherwise.

        return: The number of delegates in the majority party.  You can assume
            more than half of the delegates belong to the same party.
    '''
    num_delegates = list(range(n))
    if n == 0:
        return 0
    def recursive_party(delegates):

        if len(delegates) == 1:
            return delegates[0]

        half1 = delegates[:len(delegates)//2]
        half2 = delegates[len(delegates)//2:]
        half1_candidate = recursive_party(half1)
        half2_candidate = recursive_party(half2)
        if same_party(half1_candidate, half2_candidate):
            return half1_candidate
        count_left = sum(1 for d in delegates if same_party(d, half1_candidate))
        count_right = sum(1 for d in delegates if same_party(d, half2_candidate))
        return half1_candidate if count_left > count_right else half2_candidate
        
    candidate = recursive_party(num_delegates)
    size = sum(1 for d in num_delegates if same_party(d, candidate))

    # Replace the following line with your code.
    return size
