#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == "__main__":
    with open("ind_1.txt", "r", encoding="utf-8") as fileptr:
        puncList = [".", ";", ":", "!", "?", "/", ",", ")", "(", "\"", "\n"]
        text = fileptr.read()
        for i in text:
            if i in puncList:
                text = text.replace(i, "")
        words = text.split(" ")

        print([word for word in words if len(word) > 6])
        s = len([word for word in words if len(word) > 6])
        print(s)