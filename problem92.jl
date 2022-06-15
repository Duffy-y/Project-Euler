function next_number(n::Integer)
    out:: Integer = 0

    while n > 0
        out += (n % 10)^2
        n = floor(n / 10)
    end

    return out
end

function end_with_89(n::Integer)
    while n != 89 && n != 1
        n = next_number(n)
    end
    return n == 89
end

# println(next_number(85))

function main(limit)
    count = 0
    for i = 1:limit
        res = end_with_89(i)
        if res
            count += 1
        end
    end
    return count
end

@time res = main(10_000_000)
println(res)