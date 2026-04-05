class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        """
        Count the frequency of each card in the hand.

        Sort the card values to help ensure we get cards which are continuosuly 
        increasing by 1.

        For each card (starting from the smallest), if the card is still available 
        (frequency > 0), we can try to create a group of consecutive numbers of 
        the required length.

        For each number in the group, decrease the frequency by the count of the starting 
        card. If any card in the group doesn't have enough count, return false.
        """

        if len(hand) % groupSize != 0:
            return False

        
        count = Counter(hand)

        for card in sorted(hand):
            if count[card] > 0:
                freq = count[card]
                for i in range(card, card + groupSize):
                    if count[i] < freq:
                        return False
                    count[i] -= freq

        return True