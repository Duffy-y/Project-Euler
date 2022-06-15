using Printf

function generate_possible_value!(n::Integer, possible_value)
    push!(possible_value, [1//1])

    for m = 2:n
        @printf "Generating every way for n=%i capacitors \n" m
        m_value = []
        for k = 1:(floor(Integer, m/2))
            for C1 ∈ possible_value[k]
                for C2 ∈ possible_value[m - k]
                    parallel_capacity = C1 + C2
                    series_capacity = 1/(1/C1 + 1/C2)
                    append!(m_value, parallel_capacity)
                    append!(m_value, series_capacity)
                end
            end
        end
        unique = []
        get_unique!(m_value, unique)
        push!(possible_value, unique)
    end
end

function get_unique!(arr, out)
    flattened_array = collect(Iterators.flatten(arr))

    for val ∈ flattened_array
        if !(val ∈ out)
            push!(out, val)
        end
    end
end

function get_count(n)::Integer
    values = []
    generate_possible_value!(n, values)
    unique_values = []
    get_unique!(values, unique_values)
    return size(unique_values)[1]
end

limit = 18
possible_value = [[1//1]]
for m = 2:limit
    @printf "Generating every way for n=%i capacitors \n" m
    m_value = []
    for k = 1:(floor(Integer, m/2))
        for C1 ∈ possible_value[k]
            for C2 ∈ possible_value[m - k]
                parallel_capacity = C1 + C2
                series_capacity = 1/(1/C1 + 1/C2)
                append!(m_value, parallel_capacity)
                append!(m_value, series_capacity)
            end
        end
    end
    # unique = []
    # get_unique!(m_value, unique)
    push!(possible_value, m_value)
end

unique_values = []
get_unique!(possible_value, unique_values)
res = length(unique_values)
println("\nThere is exactly $res unique ways with $limit capacitors")