def romanNumEncoder(number)
    romanNums = {1000 => "M",
    900 => "CM",
    500 => "D",
    400 => "CD",
    100 => "C",
    90 => "XC",
    50 => "L",
    40 => "XL",
    10 => "X",
    9 => "IX",
    5 => "V",
    4 => "IV",
    1 => "I"}
    encoder = ""
    ##Logic for in case the number is exactly those criteria in the hash declared on line 2
    # for roman in romanNums
    romanNums.each do |val, roman|
        encoder << roman * (number / val)
        number = number % val
    end
   
    return encoder
end


def main()
    puts romanNumEncoder(1)
    puts romanNumEncoder(4)
    puts romanNumEncoder(6)
    puts romanNumEncoder(14)
    puts romanNumEncoder(21)
    puts romanNumEncoder(89)
    puts romanNumEncoder(91)
    puts romanNumEncoder(984)
    puts romanNumEncoder(1000)
end

main()
