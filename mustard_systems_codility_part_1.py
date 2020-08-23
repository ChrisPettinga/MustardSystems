import string
from collections import defaultdict
from itertools import groupby

def solution(N, S):
	free_count = 0  # Number of free, 3-consecutive seats for families

	seat_matrix = defaultdict(list)
	seat_letters = list(string.ascii_uppercase)
	seat_letters.remove('I')

	# This edge case can be handled better
	if not S:
		return N * 3

	taken_seats = S.split(' ')

	# A list of dictionaries to represent each row in the airplane
	seat_matrix = [{} for i in range(N)]

	for row in seat_matrix:
		for letter in seat_letters[:10]:  # Splice by 10 as only goes up to K
			row[letter] = True  # All seats are free to begin with

	for taken_seat in taken_seats:
		column = taken_seat[-1] # Seat letter will always be the last character in the string
		row = taken_seat[:len(taken_seat) - 1] # Row number will be whatever is left
		try:
			seat_matrix[int(row) - 1][column] = False # Setting the relevant element in matrix as False (taken)
		except IndexError:
			print('asd')
	for row in seat_matrix:
		# Ideally this 'segmentation' of rows would be handled above when the initial matrix is created
		segmented_rows = [
			[row['A'], row['B'], row['C']],
			[row['D'], row['E'], row['F'], row['G']],
			[row['H'], row['J'], row['K']]
		]
		for segmented_row in segmented_rows:
			# If there are 3 in a row, then increase the free_count
			if all(segmented_row):
				# If they're all free, increment
				free_count += 1
			else:
				three_in_a_row = [list(y) for x,y in groupby(segmented_row)]
				if [True, True, True] in three_in_a_row:
					# If there are 3 True's in a row, then increment. Don't waste time doing the groupby if they're all free to begin with
					free_count += 1

	return free_count - 1
