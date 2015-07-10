FROM haskell

RUN apt-get update -y
RUN apt-get install --no-install-recommends -y -q \
    make

RUN cabal update
RUN cabal install --global cryptocipher HUnit
