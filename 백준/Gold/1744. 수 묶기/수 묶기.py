N = int(input())

m_l, p_l, one_l = [], [], []
res = 0

for i in range(N):
  num = int(input())
  if num > 1:
    p_l.append(num)
  elif num <= 0:
    m_l.append(num)
  else:
    one_l.append(num)

p_l.sort(reverse = True)
m_l.sort()

if len(p_l) % 2 == 1:
  res += p_l[-1]
  for i in range(0, len(p_l)-1, 2):
    res += p_l[i] * p_l[i+1]
else:
  for i in range(0, len(p_l), 2):
    res += p_l[i] * p_l[i+1]

if len(m_l) % 2 == 1:
  res += m_l[-1]
  for i in range(0, len(m_l)-1, 2):
    res += m_l[i] * m_l[i+1]
else:
  for i in range(0, len(m_l), 2):
    res += m_l[i] * m_l[i+1]

for i in range(len(one_l)):
  res += one_l[i]

print(res)