def find():
    l1 = []
    n = int(input("\nEnter number of elements: "))
    for i in range(n):
        num = int(input("Enter number: "))
        l1.append(num)
    peak=l1[0]
    flag=0
    for i in range(n):
        if l1[i]>peak:
            peak=l1[i]
            flag=1
            for j in range(i+1,n):
                if l1[j]<peak:
                    flag=0
        if flag==1:
            break
    if flag==0:
        print("\nCondition not found in any case.")
    else:
        print("\nFirst case at position ",i," with value ",peak)
find()