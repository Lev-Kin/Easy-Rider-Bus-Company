def what_to_do(instructions):
    simon = "Simon says"
    if instructions.startswith(simon):
        return "I " + instructions[len(simon)+1:]
    elif instructions.endswith(simon):
        return "I " + instructions[:-len(simon)-1]
    else:
        return "I won't do it!"