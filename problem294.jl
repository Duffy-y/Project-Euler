using Printf

function digit_sum(n::Integer)
    out:: Integer = 0

    while n > 0
        out += n % 10
        n = floor(n / 10)
    end

    return out
end

function is_valid(n::Integer)::Bool
    return digit_sum(n) == 23
end

function main()
    limit::Integer = 10^9
    i::Integer = 1
    multiple::Integer = 23
    count::Integer = 0

    n::Integer = multiple * i

    while n < 10^9
        if is_valid(n)
            @printf "i=%i with n=%i is valid \n" i n
            count += 1
        end
        i += 1
        n = multiple * i
    end

    @printf "S(9) = %i" count
end

main()