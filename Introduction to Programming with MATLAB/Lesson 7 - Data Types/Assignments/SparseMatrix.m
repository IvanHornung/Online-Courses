function matrix = sparse2matrix(cell_vector)
  matrix = ones(cell_vector{1}) * cell_vector{2};
  for i = 3:length(cell_vector)
      first = cell_vector{i}(1:2);
      fourth = first(1); second = first(2);
      third = cell_vector{i}(3);
      matrix(fourth, second) = third;
  end
end
