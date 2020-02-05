from goc.model.player import Player

'''
Class that manage the game rules
'''
class GameOfCoins:

    def __init__(self, nb_coins, nb_players):
        self.board = []
        self.players = []
        self.nb_coins = nb_coins
        self.nb_players = nb_players
        self.current_coin = 0
        self.start()

    def start(self):
        self.create_players(self.nb_players)
        self.board.append(self.current_coin)
        self.pick_coin()
        print(self.players)

    def create_players(self, nb_players):
        for i in range(1, nb_players+1,1):
            player = Player(i)
            self.players.append(player)

    def pick_coin(self):
        for i in range(1,self.nb_coins+1, 1):
            p = i % self.nb_players
            player = self.players[p-1]
            coin = i
            index = self.board.index(self.current_coin)
            if coin % 13 == 0:
                self.coin_13(coin, player,index)
            else:
                next_pos = index + 2
                if next_pos > len(self.board):
                    next_pos = 1
                self.current_coin = coin
                self.board.insert(next_pos, self.current_coin)

    def coin_13(self, coin, player, index):
        player.score += coin
        for i in range(0, 7, 1):
            if index > 0:
                index = index - 1
            else:
                index = len(self.board) - 1
        next_pos = index + 1
        if next_pos > len(self.board)-1:
            next_pos = 0
        self.current_coin = self.board[next_pos]
        player.score += self.board[index]
        del self.board[index]



