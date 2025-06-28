class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # Verificar filas
        for row in board:
            if not self.isValidUnit(row):
                return False
        
        # Verificar columnas
        for col in range(9):
            column = [board[row][col] for row in range(9)]
            if not self.isValidUnit(column):
                return False
        
        # Verificar sub-cajas 3x3
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                box = []
                for i in range(3):
                    for j in range(3):
                        box.append(board[box_row + i][box_col + j])
                if not self.isValidUnit(box):
                    return False
        
        return True
    
    def isValidUnit(self, unit):
        """
        Verifica si una unidad (fila, columna o sub-caja) es válida
        """
        seen = set()
        for cell in unit:
            if cell == '.':
                continue
            if cell in seen:
                return False
            seen.add(cell)
        return True
        