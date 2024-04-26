def deckRevealedIncreasing(deck: list[int]) -> list[int]:
    i = 0
    result = []
    while len(deck) != 0:
        if i >= len(deck):
            i = i % len(deck)
        result.append(deck[i])
        print(i)
        deck.pop(i)
        i += 1
    return result


if __name__ == "__main__":
    deck = [17,13,11,2,3,5,7]
    r = deckRevealedIncreasing(deck)
    print(r)