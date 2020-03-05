class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num
    

    def valid(self):
        bro = self.card_num
        #Luhn Number initial Validation
        
        bro = bro.replace(" ", "")
        
        if len(bro) <= 1:
            return False

        if not bro.isnumeric():
            return False

        bro = [int(char) for char in bro]

        #Double Every Digit Starting From the right
        for num in range(len(bro) - 2, -1, -2):
            bro[num] *= 2
            if bro[num] > 9:
                bro[num] -= 9

        total = sum(bro)

        return total % 10 == 0