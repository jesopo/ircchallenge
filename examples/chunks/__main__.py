import os
from ircchallenge import Challenge

ciphertexts = [
    "f9FI0b4qdzv6vtVIFTLe5f+eiQAJ4mOb0Rygef7Dn862RZYnzu6ZJPhaiCSHFLdIEg7bBMX1",
    "2E4S4wrgCXnMgth/9IjaQ0YX1UaeVarDEE/N7lDvdSTcMjhXB/dGEyDLE/g8K4RiQ35ULhdP",
    "f41wpunc0Rsfk6QH9aqKfEpeJ747p+RdNYpiKSHQFwPQDb6jhIqeeCGj2/uI/dYKfUsANAVt",
    "Oud9x6OXnJcPkt1TJT9jLd1d9As3kJxo76I8vh8w+E4JhDdS3wlmpBfn7+vG1+qdk2RveqIv",
    "hEnKDAelfBBWQdS4kKAzbZLjkeXKE2OjNuf8oC4m0Sk1Jzge4+Vttw=="
]

if __name__ == "__main__":
    dir  = os.path.dirname(os.path.realpath(__file__))
    file = os.path.join(dir, "chunks.key")

    challenge = Challenge(keyfile=file)
    for line in ciphertexts:
        challenge.push(line)
    print(challenge.finalise())
