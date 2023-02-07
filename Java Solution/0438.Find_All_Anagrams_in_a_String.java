//sliding window with a hashmap(fix window) or sliding window with a array

class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        List<Integer> res = new ArrayList<>();
        if (p.length() > s.length()) {
            return res;
        }

        Map<Character, Integer> pmap = new HashMap<>();
        for (int i = 0; i < p.length(); i++) {
            pmap.put(p.charAt(i), pmap.getOrDefault(p.charAt(i), 0) + 1);
        }

        int l = 0;
        Map<Character, Integer> wmap = new HashMap<>();
        for (int r = 0; r < s.length(); r++) {
            char rch = s.charAt(r);
            wmap.put(rch, wmap.getOrDefault(rch, 0) + 1);

            if (r >= p.length()) {
                char lch = s.charAt(l);
                wmap.put(lch, wmap.get(lch) - 1);
                if (wmap.get(lch) == 0) {
                    wmap.remove(lch);
                }
                l++;
            }

            if (wmap.equals(pmap)) {
                res.add(l);
            }
        } 
        return res;
    }
}


// Solution: sliding window of array

class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        int ns = s.length(), np = p.length();
        if (ns < np) return new ArrayList();

        int [] pCount = new int[26];
        int [] sCount = new int[26];

        for (char ch : p.toCharArray()) {
            pCount[ch - 'a']++;
        }

        List<Integer> output = new ArrayList<>();
        for (int i = 0; i < ns; i++) {
            sCount[s.charAt(i) - 'a']++;
            if (i >= np) {
                sCount[s.charAt(i - np) - 'a']--;
            }
            if (Arrays.equals(pCount, sCount)) {
                output.add(i - np + 1);
            }
        }
        return output;
    }
}
