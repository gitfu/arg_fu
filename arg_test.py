import arg_fu

arg_fu.add_action('-p',print)
arg_fu.add_action('--print',print)

arg_fu.process()
print ("now with ordered")

arg_fu.process(ordered=['--print','-p'])
