no_spec = int(input('Enter no.of specifications : '))
print (' Choose specifications : ')
temp_count = 0
specificationList = ['']*no_spec
while temp_count < no_spec:
    specificationList[temp_count] = input()
    temp_count += 1
