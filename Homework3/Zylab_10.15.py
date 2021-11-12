# Mudasir Haq
# 1834539

class Team:
    def __init__(self, teamname='none', team_wins=0, team_losses=0):
        self.teamname = teamname
        self.team_wins = team_wins
        self.team_losses = team_losses

    def get_win_percentage(self):
        # calculations are done
        return self.team_wins / (self.team_wins + self.team_losses)

    def output_statement(self):
        # result of calculations from line 13 are stored in get_win_percentage which is then stored in another variable win_pct
        win_pct = self.get_win_percentage()
        if win_pct > 0.5:
            # teamname is formatted within string into curly braces using .format()
            return print('Congratulations, Team {} has a winning average!'.format(self.teamname))
        elif win_pct < 0.5:
            return print('Team {} has a losing average.'.format(self.teamname))

if __name__ == "__main__":
    user_tm = input()
    user_tw = input()
    user_tl = input()
    # values are sent to the team class after input is gathered
    student_team = Team(user_tm, int(user_tw), int(user_tl))

    # execute the output_statement -> print according to win_pct
    student_team.output_statement()


