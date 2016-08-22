# arg_fu
Python command line argument parser, super clean, super easy, and chicks dig it.

### How to use:
* Add a switch, a function to call, and an optional help message.
```python

arg_fu.add_action(switch, func, help_mesg)

```

* Process commandline 
```python

arg_fu.process()

```
* Example
 
```python

import arg_fu

arg_fu.add_action('-p',print)
arg_fu.add_action('--print',print,"print stuff")

arg_fu.process()

```
* ex. myscript.py -p hello calls print("hello") 

* -h and --help display switches and their help messages
```

# python arg_test.py  -h

-p   Show This
-h   print stuff
--print   print stuff
--help   Show This


```

* Set the order in which the switches are processed with the optional ordered list of switches
```python

arg_fu.process(ordered=['--print','-p'])

```

*  working example with ordered switches

```python

import arg_fu


arg_fu.add_action('--p',print,"print stuff")
arg_fu.add_action('--print',print,"print stuff")

print ("now with ordered \n")

arg_fu.process(ordered=['--print','-p'])


```

```

