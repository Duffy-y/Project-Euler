using Printf
using Logging

function search_minimal_x(D::Integer)
    y = 1
    int = sqrt(BigFloat(1 + D * y^2))
    while int % 2 != 0 && int % 2 != 1
        y += 1
        int = sqrt(BigFloat(1 + D * y^2))
    end

    return int
end

function is_square(n::Integer)
    root = sqrt(n) % 2
    return root == 0 || root == 1
end

io = open("log.txt", "w+")
logger = SimpleLogger(io)
global_logger(logger)

res_D = -1
max_x = -1

for D = 2:1000
    if !is_square(D)
        println(D)
        x = search_minimal_x(D)
        @info "Minimal x at D = $D is x = $x \n"
        if x >= max_x
            global max_x = x
            global res_D = D
        end
    end
end

println(res_D)
flush(io)
close(io)