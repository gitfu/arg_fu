import arg_fu

arg_fu.add_action('-p',print,"print stuff")
arg_fu.add_action('--print',print," long print stuff")

arg_fu.process()

