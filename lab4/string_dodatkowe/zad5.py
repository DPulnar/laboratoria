
zdanie = input("zdanie")

wyrazy = zdanie.split()

najdluzsze_slowo = max(wyrazy,key=len)
print(najdluzsze_slowo)