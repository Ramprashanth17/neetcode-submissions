class Solution:

    def encode(self, strs: List[str]) -> str:
        ## Replace "," with # symbol
        encoded_str = '#'.join(strs)
        return encoded_str

    def decode(self, s: str) -> List[str]:
        ## Remove the # symbol, and seperated them into a list
        decoded_str = s.split('#')
        return decoded_str
