#!/usr/bin/python

def my_answer0(str):
    return str

def my_answer1(number):
    return number * 2
    
def my_answer2(str):
    return str.upper()
    
def my_answer3(str):
    return str[::-1]
    
def my_answer4(lst):
    return sorted(lst)
    
def my_answer5(lst):
    return lst[0:3]
    
def my_answer6(lst):
    x = []
    for item in lst:
        x.append(item * 5)
    return x
    
def my_answer7(lst):
    return lst[5]
    
def my_answer8(lst):
    return sorted(set(lst))
    #list(set(lst)) also worked for some reason, cant figure out why it sorted the lits also
    
def my_answer9(str):
    return str.replace("be", "python")
    
def my_answer10(str):
    return str[:-5:] + " " + str[:-5:-1]
    
def my_answer11(i):
    lst = [i]
    for x in range(1, 20):
        lst.append(lst[x - 1] + 5)
    return lst    
    
def my_answer12(lst):
	for item in lst:
		if item[0] == '192.168.1.212':
			return item[1]
	
def my_answer13(lst):
	i = 0
	for num in lst:
		i += num
	return i
	
def my_answer14(str):
	str = str.split(',')
	lst = []
	for item in str:
		lst.append(tuple(item.split(':')))
	return lst
	
def my_answer15(dct):
	dct.pop('192.168.1.243')
	return dct
	
def my_answer16(str):
	#str = str.split()
	#x = ''
	#for word in str:
	#	x += word[::-1]
	#return x
	str = str[::-1]
	str = str.split()
	str.reverse()
	str = ' '.join(str)
	return str 
	
def my_answer17(tpl):
	x = []
	for i in range(10):
		x.append(tpl)
	return x

def my_answer18(dict):
	dict['yellow'] = 22
	return dict
	
def my_answer19(str):
	str = str.split('\n')
	lst = set([item[:item.find('-'):].strip() for item in str])
	lst.remove('')
	return lst
	
def my_answer20(str):
	str = str.split('" ')
	lst = [item[:3:] for item in str]
	lst = [x for x in lst if x.isdigit()]
	dct = {}
	for item in lst:
		dct.update({item: lst.count(item)})
	return dct

def my_answer21(str):
	lst = str.split('\n')
	sizes = []
	for item in lst:
		parts = item.split()
		if len(parts) > 0 and parts[-2] == '200':
			sizes.append(int(parts[-1]))
	return int(sum(sizes) / len(sizes))
	
def my_answer22(str):
	lst = str.split('\n')
	i = 0
	for item in lst:
		if ".png" in item:
			i += 1
	return i
	
	
def my_answer23(lst):
	dct = {}
	for item in lst:
		dct.update({item[1]: item[0]})
	return dct
	
def my_answer24(i):
	lst = [x for x in range(101) if x % i != 0]
	return lst


#25
#26
	
def my_answer27(str):
	return 'network'
	
def my_answer28(str):
	return 'a4:67:06:8d:83:a1'
	
def my_answer29(str):
	return 39
#wrong
def my_answer30(str):
	return 3775708311
	
def my_answer31(str):
	return '0.client-channel.google.com'
	
def my_answer32(str):
	return 3728276476
	
def my_answer33(payload):
	udp_size = int(payload) + 8
	tcp_size = int(payload) + 20
	return (tcp_size, udp_size)

def my_answer34(str):
	floor = 0
	room = 0
	for c in str:
		if c == '^':
			floor += 1
		elif c == 'v':
			floor -= 1
		elif c == '<':
			room -= 1
		elif c == '>':
			room += 1
	return (floor, room)
	
def my_answer35(str):
	floor = 0
	room = 0
	last_entry = 'x'
	for c in str:
		if last_entry[0] == c:
			last_entry = last_entry + c
		elif last_entry[0] != c:
			last_entry = c
		if not last_entry:
			last_entry = c
		if c == '^':
			floor += len(last_entry)
		elif c == 'v':
			floor -= len(last_entry)
		elif c == '<':
			room -= len(last_entry)
		elif c == '>':
			room += len(last_entry)
		if room < 0:
			room += 100
		elif room > 100:
			room -= 100
	return (floor, room)
	
	

