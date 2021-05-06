SCORES = [43,50,105,62,105,85,105,105,105]
max_num = 0

SCORES.each_with_index do |score, index|
  puts "Bubble solution ##{index} score: #{score}"
  if score > max_num
    max_num = score
  end
end

max_index = SCORES.each_index.select { |index| SCORES[index] == max_num}

puts "Bubbles tests: #{SCORES.length}"
puts "Highest bubble score: #{max_num}"
puts "Solutions with highest score: #{max_index}"
