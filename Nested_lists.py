if __name__ == '__main__':
    
    main_list = []
    score_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        main_list.append([name,score])
        score_list.append(score)
    
    sat = set(score_list)
    sor = sorted(sat)
    
    second_lowest = sor[1]

    name_list = []

    for i in main_list:
      if i[1] == second_lowest:
        name_list.append(i[0])


    sor2 = sorted(name_list)
    for j in sor2:
      print(j)
