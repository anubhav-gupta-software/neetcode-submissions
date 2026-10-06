class Solution:

    def encode(self, strs: List[str]) -> str:
        final = "₹".join(strs)
        return final
    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        results = s.split("₹")
        return results
