def play_with_asterisk(n):
    pyramid = ""
    for i in range(1, n + 1):
        pyramid += " " * (n - i)
        pyramid += "* " * i
        pyramid += "\n"
    return pyramid

if __name__ == '__main__':
    print(play_with_asterisk(5))
    """
        *
       * *
      * * *
     * * * *
    * * * * *
    """
