FROM haskell

RUN apt-get update && \
    apt-get install --no-install-recommends -y -q \
        make \
    && \
    apt-get clean

RUN cabal update
RUN cabal install --global cryptocipher HUnit
