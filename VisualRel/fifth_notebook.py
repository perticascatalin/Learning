from skimage import io, transform
import helpers as help
import pdb

# 6. Process grid cell image
def process_grid_cell(filename):
	# do not forget to read as dirname + filename
	splits = filename.split('.')[0].split('_')
	splits = splits[:-1] # ignore "cell"
	image_id = splits[0]
	row = splits[1]
	col = splits[2]
	if splits[3] == '':
		print 'nada'
		# cell class will be 0
	else:
		for i in range(3, len(splits)):
			print '+', splits[i]
			# compute uniques of ints

dirname = './grid_cells/'
f1 = '001156eb13f37194_2_5_49_cell.jpg' # car
f2 = '0007ad5c6245a41d_1_6_27_cell.jpg' # man
f3 = '00031197fb7b015d_2_0_11_11_cell.jpg' # 2 chairs
f4 = '00031197fb7b015d_0_2__cell.jpg' # nothing
f5 = '00031197fb7b015d_2_3_11_11_37_cell.jpg' # 2 chairs and a table

process_grid_cell(f4)