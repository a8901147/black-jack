class Game:

    def __init__(self, player, dealer, deck):
        self.player = player
        self.dealer = dealer
        self.bet = 0
        self.deck = deck

    def deal_cards(self):
        print("\n======== Dealer ========")
        self.dealer.add_cards(self.deck.remove_card(), False)
        print("======== Player ========")
        self.player.add_cards(self.deck.remove_card(), True)
        print("\n======== Dealer ========")
        self.dealer.add_cards(self.deck.remove_card(), False)
        print("======== Player ========")
        self.player.add_cards(self.deck.remove_card(), True)

    def start_game(self):
        want_play = True
        while want_play:
            # if player still has bet
            while self.player.get_bet:
                print("======== Game start!! ========")
                self.player.place_bet(self.deck)

                self.deck.shuffle()
                self.deal_cards()

                if max(self.player.get_pts) == 21 and max(self.dealer.get_pts) == 21:
                    print("\nGAME TIE!!!")
                    print("======== Player ========")
                    self.player.show_hands(True)
                    print("======== Dealer ========")
                    self.dealer.show_hands(True)
                    self.player.set_bet(self.deck.get_bet * 1)
                    break

                if max(self.player.get_pts) == 21:
                    print("\nPLAYER WIN: black jack")
                    print("======== Player ========")
                    self.player.show_hands(True)
                    self.player.set_bet(self.deck.get_bet*3)
                    break

                if max(self.dealer.get_pts) == 21:
                    print("\nDEALER WIN: black jack")
                    print("======== Dealer ========")
                    self.dealer.show_hands(True)
                    break

                if not self.player.make_move(self.deck.get_cards):
                    print("PLAYER LOSS")
                    # player loss bet
                    break

                if not self.dealer.make_move(self.deck.get_cards):
                    print("\nDEALER LOSS")
                    print("======== Dealer ========")
                    self.dealer.show_hands(True)
                    self.player.set_bet(self.deck.get_bet * 2)
                    # player get bet
                    break

                if max(self.dealer.get_pts) > max(self.player.get_pts):
                    print("\nDEALER WIN: black jack")
                else:
                    print("\nPLAYER WIN: black jack")
                    self.player.set_bet(self.deck.get_bet * 2)
                    
                print("======== Player ========")
                self.player.show_hands(True)
                print("======== Dealer ========")
                self.dealer.show_hands(True)

            self.deck.clear_deck()
            self.player.clear_hand()
            self.dealer.clear_hand()

            print("Player has {} bet.".format(self.player.get_bet))
            answer = input("Do you want to play again?")
            want_play = answer == "y" or answer == "Y"







