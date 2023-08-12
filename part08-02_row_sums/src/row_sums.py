# Write your solution here
def row_sums(my_matrix: list):
    for item in my_matrix: #[1,2]/[3,4]
        list_sum=sum(item)
        #print(list_sum) #function
        item.append(list_sum)
        print(item)

 
if __name__ == "__main__":
    my_matrix = [[1, 2], [3, 4]]
    row_sums(my_matrix)