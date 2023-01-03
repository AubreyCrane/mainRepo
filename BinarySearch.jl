function compguess(guessParam)
    guessCount = 0                    
    high = guessParam
    low = 0
    feedback = 1

    while feedback != 3
        guessCount += 1

        if low != high
        midpoint = round(((low + high)/2))
        else
           midpoint = high
        end
        println("is ", midpoint, " too low(1), high(2), or correct(3)? ")

        feedback = parse(Int8, readline())
        if feedback == 2
            high = midpoint - 1
        elseif feedback == 1
            low = midpoint + 1
        else
            return println("It took ", guessCount, " times to get ", midpoint)
        end
    
        if feedback != 1
            if feedback != 2
                if feedback != 3
                   return print("ERROR")
                end
            end
        end
    end
end
