import arg_fu

arg_fu.add_action('-p',print,"print stuff")
arg_fu.add_action('--print',print,"print stuff")

arg_fu.process()
print ("now with ordered")

arg_fu.process(ordered=['--print','-p'])
