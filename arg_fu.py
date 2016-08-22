#!/usr/bin/env python

import sys

actions={}

help_mesgs={'-h': 'Show This',
	'--help':'Show This'}
	
def add_action(switch,func,info=None):
	'''
	add an action to be performed.	ex. args.add_action("-p",print)
	long form args work too.	ex. args.add_action('--print',print)
	'''
	sw=switch
	actions[sw]=func
	if info:
		help_mesgs[switch]=info
		

def do_action(k,v):
	'''
	
	heads up, unknown args are ignored.

	./myscript.py -p hello call the print function with one argument "hello"

	'''
	if v is not '':
		actions[k](v)
	else:
		actions[k]()

def show_help():
	switches=list(help_mesgs.keys())
	mesgs=list(help_mesgs.values())
	switches.sort()
	l=len(switches)
	while l >0:
		l-=1
		print(switches[l],' ',mesgs[l])
		
		
						
def process(data=sys.argv,ordered=None):
	'''
	call args.process in your script to process the command line 
	@data defaults to sys.argv but can be any string 
	@ordered is a list to set order that args are processed ex. ['--print','-f','--with-cheese'] 
	Supports complex args like -f movie='fu.ts'[out0+subcc], however, quotes need escaping to preserve them.
	'''
	args=" ".join(data)
	if type(ordered) is not list:
		ordered =actions.keys()
	if '-h' or '--help' in args:
		show_help()
		sys.exit()
	for switch in ordered:
		sa=args.split(" "+switch)[1:]
		for a in sa:
			v=a.split('-')[0]
			do_action(switch,v)
	
