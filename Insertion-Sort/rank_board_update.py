from tabulate import tabulate

class LeaderBoard:
    def __init__(self):
        self.rank_list =[]
    
    def add_score(self, name, college, mark):
        self.rank_list.append([name, college, mark])

        #inserton sort
        j = len(self.rank_list) - 1

        while j >= 1 and self.rank_list[j-1][2] < self.rank_list[j][2]:
            self.rank_list[j], self.rank_list[j-1] = self.rank_list[j-1], self.rank_list[j]
            j-=1

    def display_leader_board(self):
        print(tabulate(self.rank_list, headers = ["Name", "College", "Mark"], tablefmt="grid", showindex =range(1,len(self.rank_list) + 1)))


class Student:
    def __init__(self, name, college):
        self.name = name
        self.college = college
        self.marks = None

    def submit_test(self, mark, leaderBoard: LeaderBoard):
        self.mark = mark
        leaderBoard.add_score(self.name, self.college, self.mark)

def live_input(leaderboard):
    while True:
        name = input("\nEnter name (or 'exit' to quit): ").strip()
        if name.lower() == "exit":
            break

        college = input("Enter college: ").strip()

        try:
            score = int(input("Enter score: "))
        except ValueError:
            print("❌ Invalid score. Try again.")
            continue

        student = Student(name, college)
        student.submit_test(score, leaderboard)

        leaderboard.display_leader_board()

if __name__ == "__main__":
    cseLeaderBoard = LeaderBoard()
    live_input(cseLeaderBoard)
        