def solution(commands):
    answer = []
    table = [['EMPTY'] * 51 for _ in range(51)]
    merge_group = []
    
    for command in commands:
      command_lst = list(command.split())
      if command.startswith('UPDATE'):
        print('update')
        if len(command_lst) == 4:
          r = int(command_lst[1])
          c = int(command_lst[2])
          value = command_lst[3]
          if merge_group:
            for (r1,c1,r2,c2) in merge_group:
              if r1 <= r <= r2 and c1 <= c <=- c2:
                for i in range(min(r1,r2),max(r1,r2)+1):
                  for j in range(min(c1,c2),max(c1,c2)+1):
                    table[i][j] = value
          else:
            table[r][c] = value
        else:
          value_1 = command_lst[1]
          value_2 = command_lst[2]
          for i in range(50):
            for j in range(50):
              if table[i][j] == value_1:
                table[i][j] = value_2
      elif command.startswith('MERGE'):
        print('merge')
        r1 = int(command_lst[1])
        c1 = int(command_lst[2])
        r2 = int(command_lst[3])
        c2 = int(command_lst[4])
        print(f'1234 : {(r1,c1,r2,c2)}')
        merge_group.append((r1,c1,r2,c2))
        value = 'EMPTY'
        if table[r1][c1] == 'EMPTY':
          if table[r2][c2] != 'EMPTY':
            value = table[r2][c2]
        else:
          value = table[r1][c1]
        for i in range(min(r1,r2),max(r1,r2)+1):
            for j in range(min(c1,c2),max(c1,c2)+1):
                table[i][j] = value
      elif command.startswith('UNMERGE'):
        print('unmerge')
        r = int(command_lst[1])
        c = int(command_lst[2])
        print(f'r:{r} , c : {c}')
        value_memo = table[r][c]
        print(f'value_memo : {value_memo}')
        pop_lst = set()
        print(f'merge_group : {merge_group}')
        cnt = 0
        while cnt <= len(merge_group):
          cnt += 1
          for idx in range(len(merge_group)):
            (r1,c1,r2,c2) = merge_group[idx]
            print(f'(r1,c1,r2,c2) : {(r1,c1,r2,c2)}')
            small_r = min(r1,r2)
            large_r = max(r1,r2)
            small_c = min(c1,c2)
            large_c = max(c1,c2)
            if small_r <= r <= large_r or small_c <= c <= large_c:
              print(f'test : {merge_group[idx]} ')
              for i in range(small_r,large_r+1):
                for j in range(small_c,large_c+1):
                  table[i][j] = 'EMPTY'
            pop_lst.add(idx)
        pop_lst = sorted(pop_lst)
        while pop_lst:
          print(f'idx : {pop_lst}')
          print(f'merge_G : {merge_group}')
          k = pop_lst.pop()
          merge_group.pop(k)

        table[r][c] = value_memo
      elif command.startswith('PRINT'):
        print('print')
        r = int(command_lst[1])
        c = int(command_lst[2])
        answer.append(table[r][c])
    
    return table

print(solution(["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]))
