p = 32.65

epsilon = 0.5

delta_p = p * epsilon / 100

bladPomiarudol = p - delta_p
bladPomiarugora = p + delta_p

print(f"Przedział, w którym zawarta jest wielkość p, wynosi: [{bladPomiarudol}, {bladPomiarugora}]")