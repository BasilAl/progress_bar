def p_bar(percentage: float, prefix: str = "progress: ", bars: str = "#", length: int = 10):
    # bar: progress: [####      ]  43%
    filled = percentage // (100 / length)
    percentage = round(percentage, 2)
    empty = length - filled
    pbar = f'{prefix} [{bars*int(filled)}{" "*int(empty)}] {percentage:.2f} %'
    print("\b" * (len(pbar)+1), end="")  # It seems that I have not accounted for an odd character above, going back an additional space solves it
    print(pbar, end="")


if __name__ == "__main__":
    # Example Use:
    max = 10000
    import time
    for i in range(max):
        time.sleep(0.001)
        p_bar(percentage=float(100*((i+1)/max)), prefix="Your Progress: ", bars="#", length=25)

