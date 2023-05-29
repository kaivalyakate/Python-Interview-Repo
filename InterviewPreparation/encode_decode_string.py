from typing import List


class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded: str = ""
        for string in strs:
            encoded += str(len(string)) + '-' + string + ' '
        return encoded

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        strings: List[str] = []
        i = 0
        while i < len(s):
            length = self._get_length(s, i)
            strings.append(s[i+len(str(length))+1:i+len(str(length))+1+length])
            i += len(str(length)) + 2 + length
        return strings

    def _get_length(self, length_str, i):
        length = ''
        while length_str[i] != '-':
            length += length_str[i]
            i += 1
        return int(length)

codec = Codec()
print(codec.encode(["63/Rc","h","BmI3FS~J9#vmk","7uBZ?7*/","24h+X","O "]))
print(codec.decode(codec.encode(["63/Rc","h","BmI3FS~J9#vmk","7uBZ?7*/","24h+X","O "])))
