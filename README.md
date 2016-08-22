# arg_fu
Python command line argument parser, super clean, super easy, and chicks dig it.

### How to use:

```
import arg_fu
```

* add switches to parse, and a function to call like this 
```
arg_fu.add_action('-p',print)
```

* ex. myscript.py -p hello calls print("hello") 


* add an option help message
```
arg_fu.add_action('-p',print,"print stuff")
```

* add a long form and a help message
``` 
arg_fu.add_action('--print',print,"print stuff")
```
* call arg_fu.process() to process args
```
arg_fu.process()
```

* -h and --help display switches and their help messages
```
# python arg_test.py  -h

-p   Show This
-h   print stuff
--print   print stuff
--help   Show This

```

* Set the order in which the switches are processed with the optional ordered list of switches
```

arg_fu.process(ordered=['--print','-p'])

```

That's it. 

* full working example

```python


import arg_fu

arg_fu.add_action('-p',print,"print stuff")
arg_fu.add_action('--print',print,"print stuff")

arg_fu.process()

print ("now with ordered \n")

arg_fu.process(ordered=['--print','-p'])


```

