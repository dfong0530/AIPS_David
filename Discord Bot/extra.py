
#Check if product is expensive and worth buying

def is_exp_product(msg, lower_bound):

    lines = msg.split("\n")
    lines = [l for l in lines if len(l) > 0]

    for i in range(len(lines)):

        line = lines[i]

        try:

            line = line.strip()
            words = line.split(" ")
            if len(words) == 1:
                n = float(words[0])
                if n >= lower_bound:

                    return n, "\n\n".join(lines[0: i] + lines[i + 1:])
        except:
            print("Error")

    return -1, ""