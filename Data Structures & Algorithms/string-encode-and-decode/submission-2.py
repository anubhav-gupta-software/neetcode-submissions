class Solution:

    def encode(self, strs: List[str]) -> str:
        final = "₹".join(strs)
        return final
    def decode(self, s: str) -> List[str]:
        results = s.split("₹")
        return results
        