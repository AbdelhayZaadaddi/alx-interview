#!/usr/bin/python3

def isWinner(x, nums):
    if x < 1 or not nums:
        return None

    # Find the maximum number in nums to limit the sieve
    max_num = max(nums)

    # Sieve of Eratosthenes to find all primes up to max_num
    sieve = [True] * (max_num + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not primes
    for start in range(2, int(max_num**0.5) + 1):
        if sieve[start]:
            for multiple in range(start*start, max_num + 1, start):
                sieve[multiple] = False

    primes = [i for i in range(max_num + 1) if sieve[i]]

    # Function to simulate a single game
    def play_game(n):
        if n < 2:
            return "Ben"

        primes_count = [0] * (n + 1)
        for prime in primes:
            if prime > n:
                break
            for multiple in range(prime, n + 1, prime):
                primes_count[multiple] += 1

        moves = sum(primes_count)
        # Maria wins if number of moves is odd, Ben wins if even
        return "Maria" if moves % 2 != 0 else "Ben"

    # Play x games and count wins
    maria_wins = 0
    ben_wins = 0
    for num in nums:
        winner = play_game(num)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
