if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        sublist = [name,score]
        records.append(sublist)
    min_value = min(records, key=lambda x:[1])[1]
    
    lowest_scores = [name for name, score in records if score == min_value]
    lowest_scores.sort()
    for scorer in lowest_scores:
        print(scorer)
        
        
"""
find the second lowest score
"""
if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])
    second_highest = sorted(set([score for name, score in records]))[1]
    print("\n".join(sorted([name for name, score in records if score == second_highest])))
    