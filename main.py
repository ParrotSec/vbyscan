
if __name__ == '__main__':
    from cores import utils
    verbose = True
    utils.program_banner()
    import sys
    import cores

    target = ""
    for arg in sys.argv:
        if arg.startswith("-"):
            if arg == "--verbose":
                verbose = True
            elif arg == "--silent":
                verbose = False
            elif arg == "--help" or arg == "-h" or arg == "-help":
                from cores.utils import help_banner
                help_banner(sys.argv[0])
                exit(0)
            else:
                print("Unknown option " + arg)
        else:
            if target:
                target = cores.verify_target(sys.argv[1])

    if not target:
        user_input = ""
        while not user_input:
            user_input = input("Enter target URL: ")
            if user_input:
                target = cores.verify_target(user_input)

    from cores import controller
    controller.main_logic(target, verbose)
