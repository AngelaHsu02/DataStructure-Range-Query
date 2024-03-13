import random
class Node(object):
    '''
    Class to implement node
    '''
    def __init__(self, key, level):
        # 節點儲存的值
        self.key = key  
        # list to hold references to node of different level #節點儲存的層
        self.forward = [None]*(level+1)


class SkipList(object):
    '''
    Class for Skip list
    '''
    def __init__(self, max_lvl, P):
        # 最大層數
        self.MAXLVL = max_lvl

        # 往上copy的機率
        self.P = P

        # create header node and initialize key to -1
        self.header = self.createNode(self.MAXLVL, -1)

        # current level of skip list
        self.level = 0

    # create  new node
    def createNode(self, lvl, key):
        n = Node(key, lvl)
        return n

    # create random level for node 
    def randomLevel(self):
        lvl = 0
        # 如果隨機小數<P 且<最大層數，則層級+1。為什麼random.random()>0.5還會+1? #降P減少層數
        # 1/2 level1, 1/4 level2, 1/8 level3...
        # 節點是下層的1/2
        while random.random() < self.P and lvl < self.MAXLVL:
            #print(random.random(), self.P, lvl+1)
            lvl += 1
        return lvl

    # insert given key in skip list
    def insertElement(self, key):
        #print(key)
        # create update array and initialize it
        update = [None]*(self.MAXLVL+1)
        current = self.header


        '''
        search插入正確位置，從最高層開始過，如果遇到比自己小的前進，遇到比自己大往下一層
        start from highest level of skip list
        move the current reference forward while key 
        is greater than key of node next to current
        Otherwise inserted current in update and 
        move one level down and continue search
        '''
        # 從最上層開始，如果下一個節點存在&其鍵值小於插入的key->則繼續前進

        for i in range(self.level, -1, -1):  
            while current.forward[i] and \
                    current.forward[i].key < key:
                current = current.forward[i]
            update[i] = current  # update[1]存最高層插入的節點, update[0]存第0層插入的節點

        ''' 插入到level 0正確位置
        reached level 0 and forward reference to 
        right, which is desired position to 
        insert key.
        '''
        current = current.forward[0]

        '''如果current為空，表示已經到了0層最後一個節點，或者current的鍵值不等於要插入的鍵值->必須在update[0]和current node之間插入新節點。
        if current is NULL that means we have reached
           to end of the level or current's key is not equal
           to key to insert that means we have to insert
           node between update[0] and current node
       '''
        if current == None or current.key != key or current.key == key:
            # Generate a random level for node
            rlevel = self.randomLevel()

            '''
            If random level is greater than list's current
            level (node with highest level inserted in 
            list so far), initialize update value with reference
            to header for further use
            '''
            if rlevel > self.level:  # 新節點的層級>當前的最高層
                for i in range(self.level+1, rlevel+1):  
                    update[i] = self.header  # 更新update[1]頭節點，第一層頭節點
                self.level = rlevel  # 更新目前最高層

            # create new node with random level generated創建一個新節點n。
            n = self.createNode(rlevel, key) 
            #print(rlevel, key)

            # insert node by rearranging references加上新節點的每一層指針
            for i in range(rlevel+1):
                n.forward[i] = update[i].forward[i]
                update[i].forward[i] = n  # 更新update[i]的指針指向新節點n。
            #print("Successfully inserted key {}".format(key))

    # Display skip list level wise
    def displayList(self):
        print("\n*****Skip List******")
        head = self.header
        for lvl in range(self.level+1):  # 遍歷每一層
            print("Level {}: ".format(lvl), end=" ")  # 打印當前層級的標記。
            node = head.forward[lvl]  # 從頭節點的當前層級開始。
            while (node != None):  # 當節點不為空時，遍歷該層。
                print(node.key, end=" ")
                node = node.forward[lvl]  # 移動到該層的下一個節點
            print("")
    
    def searchElement(self, key):
        current = self.header
        '''
        start from highest level of skip list
        move the current reference forward while key 
        is greater than key of node next to current
        Otherwise inserted current in update and 
        move one level down and continue search
        '''
        for i in range(self.level, -1, -1):
            while (current.forward[i] and
                   current.forward[i].key < key):
                current = current.forward[i]

        # reached level 0 and advance reference to
        # right, which is possibly our desired node
        current = current.forward[0]

        # If current node have key equal to
        # search key, we have found our target node
        if current and current.key == key:
            print("Found key ", key)


if __name__ == '__main__':
    lst = SkipList(3, 0.5)
    lst.insertElement(3)
    lst.insertElement(6)
    lst.insertElement(3)
    #lst.insertElement(9)
    #lst.insertElement(12)
    #lst.insertElement(19)
    #lst.insertElement(17)
    #lst.insertElement(26)
    #lst.insertElement(21)
    #lst.insertElement(25)
    lst.displayList()
 
    ## Search for node 19
    lst.searchElement(3)
