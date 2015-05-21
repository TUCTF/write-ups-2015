import md5

hex_input = raw_input("Please input the string: ").decode('utf-8')
print hex_input
end_bits = '0'*15

r = 0
flag = True
while flag:
	hex_data = md5.new(hex_input + str(r)).hexdigest()
	print hex_data
	scale = 16 

	num_of_bits = len(hex_data) * 4

	binary_data = bin(int(hex_data, scale))

	if binary_data.endswith(end_bits):
		print "r of length " + str(r)  " succeeded!"
		flag = False
	else:
		print "tried r of length " + str(r) + ". No success "
		r += 1



