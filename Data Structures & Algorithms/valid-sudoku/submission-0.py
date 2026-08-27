class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #row wise checking
        for i in range(len(board)):
            hash=defaultdict(int)
            for j in range(len(board[0])):
                hash[board[i][j]]+=1
            for n,c in hash.items():
                if c!=1 and n!=".":
                    return False
        #column wise checking
        for j in range(len(board[0])):
            hash=defaultdict(int)
            for i in range(len(board)):
                hash[board[i][j]]+=1
            for n,c in hash.items():
                if c!=1 and n!=".":
                    return False
        #grid checking
        iStart=0
        jStart=0     
        for k in range(9):
            
            if k ==3:
                jStart+=3
                iStart=0
            if k==6:
                jStart+=3
                iStart=0
            hash=defaultdict(int)
            for i in range(iStart,iStart+3):
                for j in range(jStart,jStart+3):
                    hash[board[i][j]]+=1
            for n,c in hash.items():
                if c!=1 and n!=".":
                    return False
            iStart+=3
        return True