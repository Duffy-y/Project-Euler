function is_prime(n::Integer)::Bool
    if n == 2
        return true
    end
    for divisor = 2:ceil(sqrt(n))
        if n % divisor == 0
            return false
        end
    end
    return true
end

function find_next_prime(n::Integer)::Integer
    found::Bool = false
    
    i::Integer = n + 1
    while !found
        if is_prime(i)
            return i
        end
        i += 1
    end
end

function main(limit::Integer)
    sum::Integer = 0

    for n = 2:limit
        if is_prime(n)
            sum += n
        end
    end

    println("Sum of primes below $limit is $sum")
end

main(2_000_000)