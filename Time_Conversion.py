def timeConversion(s):
    if "am" in s.lower():
        if s[:2] == "12":
            split_s = s.split(":")
            split_s[0] = "00"
            return ":".join(split_s)[:-2]
        return s[:-2]

    elif "pm" in s.lower() and s[:2] == "12":
        return s[:-2]

    else:
        split_s = s.split(":")
        split_s[0] = str(int(split_s[0]) + 12)
        return ":".join(split_s)[:-2]
