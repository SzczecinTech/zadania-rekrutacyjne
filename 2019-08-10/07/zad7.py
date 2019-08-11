def equal_slices(total, num, per_person):
  res = num * per_person
  if res <= total:
    return True
  return False


foo = equal_slices(11, 11, 1)
print(str(foo))


