# Activity 2 — Message Passing (Pseudocode)

**Activity label:** Activity 2 - Message passing

---

## Exercise 1 — Prime Sieve (Sieve of Eratosthenes)

### Background

The Sieve of Eratosthenes eliminates composites by filtering out multiples of each prime discovered. The concurrent (pipeline) version maps each sieve stage to a separate process: each stage receives a stream of numbers, keeps the first (which is prime), and passes on only numbers not divisible by that prime to the next stage.

### Concurrent Design

**How many threads/processes?**  
One thread for the number generator, plus one thread per discovered prime. If we want primes up to N, in the worst case we need π(N) filter threads (the prime-counting function). For N = 1000, that's 168 threads.

**How and when to terminate:**  
Each filter thread passes a **sentinel value** (e.g., -1) downstream when its input is exhausted. The main collector terminates when it receives the sentinel.

**How primes are identified and output:**  
The first value each filter stage receives is, by definition, a prime (it has passed all upstream filters). Each stage outputs this value; these outputs collected in order are the primes.

---

### Pseudocode — Version 1: Terminate after examining N numbers

```
PROCESS Generator(output_channel, limit):
    FOR n FROM 2 TO limit:
        SEND n TO output_channel
    SEND SENTINEL(-1) TO output_channel
    TERMINATE


PROCESS FilterStage(input_channel, output_channel):
    prime = RECEIVE FROM input_channel   // first value received is a prime
    PRINT prime
    
    LOOP:
        n = RECEIVE FROM input_channel
        IF n == SENTINEL:
            SEND SENTINEL TO output_channel
            TERMINATE
        IF n MOD prime != 0:             // filter out multiples
            SEND n TO output_channel


PROCESS Collector(input_channel):
    // optional: receive remaining primes if FilterStage outputs them
    LOOP:
        n = RECEIVE FROM input_channel
        IF n == SENTINEL:
            TERMINATE


MAIN:
    channels = dynamically created as stages are added
    
    SPAWN Generator(channels[0], limit=1000)
    
    current_channel = channels[0]
    
    LOOP:
        n = RECEIVE FROM current_channel
        IF n == SENTINEL:
            TERMINATE
        // n is a new prime
        PRINT n
        next_channel = NEW CHANNEL
        SPAWN FilterStage(current_channel, next_channel)
        current_channel = next_channel
```

---

### Pseudocode — Version 2: Terminate after finding K primes

```
MAIN:
    primes_found = 0
    target = 50                // e.g., find first 50 primes
    
    SPAWN Generator(channels[0], limit=INFINITY)
    current_channel = channels[0]
    
    LOOP:
        n = RECEIVE FROM current_channel
        primes_found += 1
        PRINT n
        
        IF primes_found == target:
            SEND KILL_SIGNAL to Generator     // stop producing
            TERMINATE ALL FILTER STAGES
            TERMINATE
        
        next_channel = NEW CHANNEL
        SPAWN FilterStage(current_channel, next_channel)
        current_channel = next_channel
```

---

### Analysis: Is this the most effective approach?

**Strengths:**
- Naturally concurrent — each prime gets its own filter stage
- Elegantly models the algorithm structure
- Message-based: no shared state, no locks needed

**Limitations:**
- Scales poorly: O(π(N)) threads, which for large N is significant thread overhead
- Each number must pass through *all* upstream filters sequentially — latency grows with each new prime
- Not memory-efficient: channels buffer numbers between stages
- Modern sieves (e.g., Atkin's sieve, segmented sieve) are faster in sequential form and do not have this overhead

**Conclusion:** The pipeline prime sieve is an excellent **teaching example** for message passing concurrency but is not the most efficient prime generator in practice. For real workloads, a segmented sieve with parallel chunk processing would be more effective.

---

## Exercise 2 — Chinese Whispers

### Background

A circular ring of processes, each passing a message to the next with a random chance of introducing an error. The starting process sends the original, and when the message returns, it is compared to the original.

### Concurrent Design

**Structure:** N processes arranged in a ring. Each process:
1. Blocks waiting to receive a message
2. Randomly decides whether to mutate it
3. Forwards the (possibly mutated) message to the next process

**Termination:** When the message returns to Process 0, it prints the comparison and terminates. A broadcast TERMINATE signal is sent around the ring to clean up.

---

### Pseudocode

```
CONSTANTS:
    N_PLAYERS = 7
    ERROR_CHANCE = 0.3   // 30% probability of introducing an error


FUNCTION introduce_error(message):
    // Randomly swap two characters
    IF length(message) < 2:
        RETURN message
    i, j = TWO RANDOM DISTINCT INDICES IN range(0, length(message))
    SWAP characters at positions i and j in message
    RETURN modified message


PROCESS Player(id, in_channel, out_channel, is_starter):
    
    IF is_starter:
        // Starter sends the original message first
        original = "The quick brown fox"
        SEND original TO out_channel
        
        // Then wait to receive it back
        received = RECEIVE FROM in_channel
        
        PRINT "Original: " + original
        PRINT "Received: " + received
        PRINT "Match: " + (original == received)
        
        // Send termination signal
        SEND TERMINATE TO out_channel
        TERMINATE
    
    ELSE:
        LOOP:
            msg = RECEIVE FROM in_channel
            
            IF msg == TERMINATE:
                SEND TERMINATE TO out_channel
                TERMINATE
            
            r = RANDOM FLOAT between 0.0 and 1.0
            
            IF r < ERROR_CHANCE:
                msg = introduce_error(msg)
                PRINT "Player " + id + " introduced error: " + msg
            ELSE:
                PRINT "Player " + id + " passed unchanged: " + msg
            
            SEND msg TO out_channel


MAIN:
    // Create N channels (one per link between players)
    channels = [NEW CHANNEL FOR i IN range(N_PLAYERS)]
    
    // Spawn all players
    FOR i FROM 0 TO N_PLAYERS - 1:
        in_ch  = channels[i]
        out_ch = channels[(i + 1) MOD N_PLAYERS]  // circular
        is_starter = (i == 0)
        
        SPAWN Player(i, in_ch, out_ch, is_starter)
    
    // All players are now blocking on receive, except Player 0 who sends first
    WAIT FOR ALL PLAYERS TO TERMINATE
```

---

### Design Notes

**Circular vs linear:**  
The activity specifies a circular network. The ring is formed by connecting the output of Player N-1 back to the input of Player 0. This is why the starting player both sends first *and* waits to receive — it acts as both sender and final receiver.

**Randomisation strategy choices:**
- Character swap (used above): preserves message length, subtle mutation
- Character deletion: changes message length
- Random character substitution: more aggressive corruption

**What this demonstrates:**
- Asynchronous message passing (sender does not wait for acknowledgement)
- Indirect asymmetric naming (each player only knows the next player's channel, not the sender's identity)
- Termination propagation via sentinel message around the ring
