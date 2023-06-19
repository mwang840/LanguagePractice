def romanNumEncoder(number)
    romanNums = {1=>"I", 4=>"IV", 5=>"V", 9=>"IX", 10=>"X", 50=>"L", 100=>"C", 500=>"D", 1000=>"M"}
    encoder = ""
    ##Logic for in case the number is exactly those criteria in the hash declared on line 2
    if number == 1
        puts "Number is one"
        encoder = encoder + romanNums[1]
    elsif number == 4
        encoder = encoder + romanNums[4]   
    elsif number == 5  
        encoder = encoder + romanNums[5]
    elsif number == 9
        encoder =  encoder + romanNums[9]   
    elsif number == 10
        encoder =  encoder + romanNums[10]
    elsif number == 50
        encoder =  encoder + romanNums[50]  
    elsif number == 100
        encoder =  encoder + romanNums[100]  
    elsif number == 500
        encoder =  encoder + romanNums[500]  
    elsif number == 1000
        encoder =  encoder + romanNums[1000]                        
    end
    return encoder
end


def main()
    puts romanNumEncoder(1)
end

main()
