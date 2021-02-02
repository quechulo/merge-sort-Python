"""
    Implementation of merge sort algorithm
"""

def merge_sort(lo, hi, tab, a): # function to divide array and initialise recursive execution
    if hi > lo:
        mid = lo + (hi - lo) // 2
        merge_sort(lo, mid, tab, a)
        merge_sort(mid+1, hi, tab, a)
        merge_merge(lo, hi, mid, tab, a)
    return tab

def merge_merge(lo, hi, mid, tab, a):
    for k in range(lo, hi+1):
        a[k] = tab[k]
    i = lo
    j = mid+1

    for k in range(lo, hi+1):
        if i > mid:
            tab[k] = a[j]
            j += 1
        elif j > hi:
            tab[k] = a[i]
            i += 1
        elif a[i] > a[j]:
            tab[k] = a[j]
            j += 1
        else:
            tab[k] = a[i]
            i += 1

def run_merge_sort(tab):
    return merge_sort(0, len(tab)-1, tab, tab.copy())

