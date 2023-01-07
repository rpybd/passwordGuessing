init = False
r_list = []

def bi_search(a, x, l, r):
	if (l == r): return l
	mid = (l+r)/2
	if x > a[l]: return -1
	elif x >= a[mid+1]: return bi_search(a, x, l, mid)
	else: return bi_search(a, x, mid+1, r)

def monte_carlo(p, p_list):
	global init, r_list
	if not init:
		s = 0
		p_list.sort(reverse=True)
		for i in p_list:
			s += 1.0/i
			r = s/len(p_list)+1
			r_list.append(int(r))
		init = True
	k = bi_search(p_list, p, 0, len(r_list)-1)
	if k == -1: return 1
	else: return r_list[k]

if __name__ == '__main__':
	p_list = []
	fplist = open("sampleprobs.txt", "r") #probablity of sampled list
	for line in fplist:
		p_list.append(float(line))
	fplist.close()

	fp = open("testprobs.txt", "r") #probablity of test set
	fout = open("testguesscnt.txt", "w") #output
	for line in fp:
		line = line.strip('\n').strip('\r')
		r = monte_carlo(float(line), p_list)
		fout.write(str(r)+'\n')
	fp.close()
	fout.close()
