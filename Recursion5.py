def l_sum(n_list):
    if len(n_list) == 1:
        return n_list[0]
    else:
        return n_list[0] + l_sum(n_list[1:])

print(l_sum([2, 4, 5, 6, 7])) 