tensor = [[[i*j*k
            for i in range(1,4)]
           for j in range(1,4)]
          for k in range(1,4)]

print(*tensor, sep='\n')