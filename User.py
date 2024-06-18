class User :
    numOfUsers=0
    def __init__(self,*args):
        if len(args) ==7:
         self.User_id=args[0]
         self.User_name=args[1]
         self.User_DoB=args[2]
         self.Role=args[3]
         self.Active=args[4]
         self.Basket=args[5]
         self.Order=args[6]
         User.numOfUsers+=1
        elif len(args) == 5:
            self.User_id = args[0]
            self.User_name = args[1]
            self.User_DoB = args[2]
            self.Role = args[3]
            self.Active = args[4]
            User.numOfUsers += 1

