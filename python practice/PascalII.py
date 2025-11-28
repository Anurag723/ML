class PascalII:

    @staticmethod
    def getRow(rowIndex: int):
        row = [1]   # C(k, 0) = 1
        
        # C(k, i) = C(k, i-1) * (k - i + 1) // i
        for i in range(1, rowIndex + 1):
            prev = row[i - 1]
            next_val = prev * (rowIndex - i + 1) // i
            row.append(next_val)
        
        return row


if __name__ == "__main__":
    rowIndex = int(input("Enter rowIndex: "))
    result = PascalII.getRow(rowIndex)
    print(result)
