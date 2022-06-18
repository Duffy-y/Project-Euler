function digit_sum(n::Integer)
    out::Integer = 0

    while n > 0
        out += n % 10
        n = n ÷ 10
    end

    return out
end

function s(n::Integer)::Integer
    i::Int64 = 0
    while digit_sum(i) != n
        i += 1
    end

    return i
end

function s_test(n::Integer)::Integer
    if n <= 10
        return n
    end
    return (n % 9) * 10^(n ÷ 9) + 9 * (10^((n-9) ÷ 9))
end

function S(k::Integer)::Integer
    for n in 1:k
        println("YEET")
    end
end

function main()::Integer
    sum::Int64 = 0
    fib_1::Int64 = 0
    fib_2::Int64 = 1
    
    for i = 2:90
        println("YEET")
    end
end

for i = 0:100
    res = s(i)
    s_t = s_test(i)
    println("i = $i | res = $res | test = $s_t")
end