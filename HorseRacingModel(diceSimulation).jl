using StatsPlots
using DataFrames

function horseRacingModel(numOfRaces)
    amountOfRaces = 0
    winRace = false
    raceParam = 0
    two = 0
    three = 0
    four = 0
    five = 0
    six = 0
    seven = 0
    eight = 0
    nine = 0
    ten = 0
    eleven = 0
    twelve = 0

    while raceParam != numOfRaces
        
        while winRace != true && raceParam != numOfRaces # winRace != true
            amountOfRaces += 1
            diceRoll = rand(1:6) + rand(1:6)

            if diceRoll == 2
                two += 1
                if two == 12
                    raceParam += 1
                    winRace == true
                    print("two ")
                end
            elseif diceRoll == 3
                three += 1
                if three == 12
                    raceParam += 1
                    winRace == true
                    print("three ")
                end
            elseif diceRoll == 4
                four += 1
                if four == 12
                    raceParam += 1
                    winRace == true
                    print("four ")
                end
            elseif diceRoll == 5
                five += 1
                if five == 12
                    raceParam += 1
                    winRace == true
                    print("five ")
                end
            elseif diceRoll == 6
                six += 1
                if six == 12
                    raceParam += 1
                    winRace == true
                    print("six ")
                end
            elseif diceRoll == 7
                seven += 1
                if seven == 12
                    raceParam += 1
                    winRace == true
                    print("seven ")
                end
            elseif diceRoll == 8
                eight += 1
                if eight == 12
                    raceParam += 1
                    winRace == true
                    print("eight ")
                end
            elseif diceRoll == 9
                nine += 1
                if nine == 12
                    raceParam += 1
                    winRace == true
                    print("nine ")
                end
            elseif diceRoll == 10
                ten += 1
                if ten == 12
                    winRace == true
                    print("ten ")
                end
            elseif diceRoll == 11
                eleven += 1
                if eleven == 12
                    raceParam += 1
                    winRace == true
                    print("eleven ")
                end
            elseif diceRoll == 12
                twelve += 1
                if twelve == 12
                    raceParam += 1
                    winRace == true
                    print("twelve ")
                end
            end



        end
    end





end
