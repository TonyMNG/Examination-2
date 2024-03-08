class Scoreboard:
    def __init__(self, filename):
        self.filename = filename

    def draw(self):
        self.display_scores()    

    def add_score(self, name, score):
        with open(self.filename, 'a') as file:
            file.write(f"{name.ljust(20)} {score}\n")

    def display_scores(self):
        with open(self.filename, 'r') as file:
            scores = file.readlines()
            print("======= Scoreboard =======")
            print("Player ============ Wins =")
            for line in scores:
                print(line.strip())
            print("==========================")


scoreboard = Scoreboard("scores.txt")