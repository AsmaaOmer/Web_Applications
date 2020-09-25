import anvil.server

anvil.server.connect("XF6FGZH2IDUDOGLC4X5WYBRK-2U3WV2BJWIRZB4LA")

@anvil.server.callable
def say_hello(name):
    print(f"Hello from your own machine, {name}!")

anvil.server.wait_forever()