class Scoreboard:
    def __init__(self, filename):
        self.filename = filename

    def draw(self):
        self.display_scores()    

    def add_score(self, name, score):
        with open(self.filename, 'a') as file:
            file.write(f"{name}: {score}\n")

    def display_scores(self):
        with open(self.filename, 'r') as file:
            scores = file.readlines()
            print("======= Scoreboard =======")
            for line in scores:
                print(line.strip())
            print("==========================")


scoreboard = Scoreboard("scores.txt")