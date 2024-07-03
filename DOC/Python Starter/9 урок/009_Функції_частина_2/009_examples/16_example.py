def alphabet_position(text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    out = ""
    for symbol in text.lower():
        out += str((alphabet.find(symbol) + 1)) + " "
    return ''.join(out)


t = "YGwsaCLmUADyidytxiaUpUguwVBNpKPMSTInHRELscPJUIvsQncDVGAtgHRPfOIfpZDoHuOkiQoLloWcFxuSITxwUJlEPFNsknPp"
print(alphabet_position(t))
