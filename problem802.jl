using ProgressBars

function main()::Integer
    n_1::Int128 = 2
    n_2::Int128 = 2
    
    for i in ProgressBar(3:(10^7-1))
        n_1, n_2 = n_2, n_1 + n_2
    end

    return n_2 % 1_020_340_567
end

println(main())