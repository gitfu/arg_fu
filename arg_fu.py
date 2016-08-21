#!/usr/bin/env python

'''

arg_fu is py2py3

'''

import sys
import re

actions={}

def add_action(switch,func):
	'''
	add an action to be performed.	ex. args.add_action("-p",print)
	long form args work too.	ex. args.add_action('--print',print)
	'''
	sw=switch
	actions[sw]=func

def do_action(k,v):
	'''
	
	heads up, unknown args are ignored.

	./myscript.py -p hello call the print function with one argument "hello"

	'''
	if v is not '':
		actions[k](v)
	else:
		actions[k]()
						
def process(data=sys.argv,ordered=None):
	'''
	call args.process in your script to process the command line 
	@data defaults to sys.argv but can be any string 
	@ordered is a list to set order that args are processed ex. ['--print','-f','--with-cheese'] 
	Supports complex args like -f movie='fu.ts'[out0+subcc], however, quotes need escaping to preserve them.
	'''
	if type(ordered) is not list:
		ordered =actions.keys()
	for switch in ordered:
		args=" ".join(data)
		sa=args.split(" "+switch)[1:]
		for a in sa:
			v=a.split('-')[0]
			do_action(switch,v)
	
