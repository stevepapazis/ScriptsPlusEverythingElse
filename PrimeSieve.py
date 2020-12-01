
class PrimeSieve:


    def __init__(sieve, N, primelist = None, generatelist = False):
        sieve.__setup_sieve__(N, primelist)
        sieve.__generate_sieve__()
        if generatelist:
            sieve.__primes = sieve.getPrimes()

               
    def __setup_sieve__(sieve, N, primelist):
        sieve.__N = N
        sieve.__topIndex = N//2 + 1
        sieve.__oddPrimeSieve = bytearray( [1]*(sieve.__topIndex) )
        if primelist != None:
            for p in primelist:
                if p == 2: continue
                for multipleOfp in range(p**2//2, sieve.__topIndex, p):
                    sieve.__oddPrimeSieve[multipleOfp] = 0
        sieve.__oddPrimeSieve[0] = 0

        
    def __generate_sieve__(sieve):
        sqrt = sieve.__N**.5
        for k, isItPrime in enumerate(sieve.__oddPrimeSieve,1):
            odd = 2*k - 1
            if odd>sqrt:
                break
            if isItPrime:
                for multipleOfOdd in range(odd**2//2, sieve.__topIndex, odd):
                    sieve.__oddPrimeSieve[multipleOfOdd] = 0


    def __repr__(sieve):
        return str(sieve.getPrimes())

    
    def __len__(sieve):
        try:
            return sieve.__numberOfPrimes
        except AttributeError:
            sieve.__numberOfPrimes = len(sieve.getPrimes())
        return sieve.__numberOfPrimes


    def __getitem__(sieve, key):
        return sieve.getPrimes()[key]


    def isOddPrime(sieve, n):
        try:
            return bool( sieve.__oddPrimeSieve[n//2] )
        except IndexError:
            pass
        raise Exception( "n must be less than " + str(sieve.__N) )


    def isPrime(sieve, n):
        if n%2==0:
            if n==2:
                return True
            else:
                return False
        else:
            return sieve.isOddPrime(n)


    def topLimit(sieve):
        return sieve.__N


    def getPrimes(sieve):
        try:
            return sieve.__primes
        except AttributeError:
            sieve.__primes = [2]
            sieve.__primes.extend(
                [
                    2*n + 1 \
                    for n in range(len(sieve.__oddPrimeSieve)-1)\
                    if sieve.__oddPrimeSieve[n]
                 ]
                )
            return sieve.__primes

