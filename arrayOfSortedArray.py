class arrayOfSortedArray:
    def __init__(self):
        self.arrays = []  # An array of arrays, initially empty

    def insert(self, value):
        # Start by inserting the value into a new array
        temp = [value]
        #print(temp)        
        # Iterate through each level, merging if necessary
        for i in range(len(self.arrays)):
            #print(i, self.arrays, len(self.arrays),self.arrays[i])

            # If array is empty, place temp here
            if not self.arrays[i]: #如果i大於等於self.arrays的長度或self.arrays[i]為空
                self.arrays[i] = temp
                return  # Insertion done, exit the method
            
            # If there is an array, merge it with temp
            temp = sorted(self.arrays[i] + temp)
            #print(f'temp{temp}')
            # Clear the merged array position
            self.arrays[i] = None
        
        # If all positions are filled, append the new array at the end
        self.arrays.append(temp)
        #print(f'self.arrays{self.arrays}')

    def _print_structure(self):
        print("\n*****Array of Sorted Array******")
        # Helper function to visualize the structure
        for i, arr in enumerate(self.arrays):
            size = 2**i #if i < len(self.arrays) else "end"
            print(f"array{size}: {arr}")

# Example Usage
#aosa = arrayOfSortedArray()
#aosa.insert(5)
#aosa._print_structure()
#aosa.insert(1)
#aosa._print_structure()
#aosa.insert(3)
#aosa._print_structure()
#aosa.insert(2)
#aosa._print_structure()
#aosa.insert(4)
#aosa._print_structure()
#aosa.insert(6)
#aosa._print_structure() 
#aosa.insert(7)
#aosa._print_structure() 
#aosa.insert(8)
#aosa._print_structure() 
#aosa.insert(9)
#aosa._print_structure()  # This will print the internal structure with the inserted elements
#aosa.insert(10)
#aosa._print_structure() 
#aosa.insert(11)
#aosa._print_structure() 
#aosa.insert(12)
#aosa._print_structure() 









#if __name__ == '__main__':
#    file_path = './random_numbers.txt'
#    # Read the numbers from the file and store them in different data structures
#    arrayOfSortedArray = []
#    with open(file_path, 'r') as file:
#        for line in file:
#            number = int(line.strip())
#            arrayOfSortedArray.append(number)
#    print(arrayOfSortedArray)