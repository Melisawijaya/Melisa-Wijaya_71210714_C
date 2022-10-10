class PrefixConverter:
    def __init__(self):
        self.stackList = []
        self.prioritas = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        self.operator = []
        self.operand = []
        
    # method untuk menambahkan data baru
    def push(self,data):
        self.stackList.append(data)
        
    # method untuk melihat data paling atas
    def peek(self):
        if self.stackList:
            return self.stackList[-1]
        else:
            return "Isi Stack Kosong"
        
    # method untuk menghapus data palin atas
    def pop(self):
        if self.stackList:
            data = self.stackList.pop(-1)
            return data
        else:
            return "Isi Stack Kosong"
        
    def cekValidExpression(self,expression):
        for i in self.expression:
            if i == "(" or i == ")":
                return "Expresi Infix yang anda masukkan tidak valid !!"
            return
    
    def NotOperator(expression):
        return ((expression >= 'a' and expression <= 'z') and (expression >= '0' and expression <= '9') and (expression >= 'A' and expression <= 'Z'))
        
    def infixToPrefix(self,expression):
        for i in range (len(expression)):
            if self.NotOperator(i):
                self.operand.append(expression[i] + "")
            else:
                while (len(self.operator) != 0 and self.prioritas(expression[i] <= self.prioritas(self.operator[-1]))):
                    operand1 = self.operand[-1]
                    self.operand.pop()
                    
                    operand2 = self.operand[-1]
                    self.operand.pop()
                    
                    operator = self.operator[-1]
                    self.operator.pop()
                    
                    tampung = operator + operand2 + operand1
                    self.operand.append(tampung)
                self.operator.append(expression[i])
                
        while (len(self.operator) != 0):
            operand1 = self.operand[-1]
            self.operand.pop()
                    
            operand2 = self.operand[-1]
            self.operand.pop()
            
            operator = self.operator[-1]
            self.operator.pop()
            
            tampung = operator + operand2 + operand1
            self.operand.append(tampung)
        return self.operand[-1]
    

if __name__ == '__main__':
    expresi1 = PrefixConverter()
    print(expresi1.infixToPrefix("1+2+3*4/2-1"))
    print(expresi1.infixToPrefix("A * (B + C) / D"))
    print(expresi1.infixToPrefix("(1+2)*3"))
    print(expresi1.infixToPrefix("20 * 3 - 10 + 289"))
    print(expresi1.infixToPrefix("100 * 30 / 600 - 30 + 100 * 777"))
